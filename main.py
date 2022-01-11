import json
import requests
from bs4 import BeautifulSoup as bs
import asyncio
from pprint import pprint
import logging
# from fake_useragent import UserAgent
# from fake_useragent import UserAgent
# from requests_html import HTMLSession


class ToManyRequests(BaseException):
    """
    Кастомное исключение, которое дает понять, что мы отправили слишком много запрозов
    и нас не надолго забанили)
    """
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"Reuqests error: {self.message}"
        else:
            return "Нас немножко забанили)"


class Avito:

    def __init__(self):
        self.base_url = "https://www.avito.ru/sankt-peterburg/nedvizhimost?cd=1&metro=155-156-157-158-160-162-163-164-165-169-173-174-175-176-178-179-180-181-185-187-189-190-191-199-201-202-203-205-209-210-211-1015-1016-1017-2122-2132"
        # self.ua = UserAgent(verify_ssl=False, use_cache_server=False, cache=False)
        # self.ua = UserAgent()

    async def get_html(self, url):
        response = requests.get(url)
        if response.status_code == 429:
            raise ToManyRequests
        else:
            return response.text

    async def get_all_pages_links(self) -> tuple[str]:
        """
        Берем номера страниц из пагинации и добавляем к каждоый ссылке.
        Вормирвуем список ссылок
        :return:
        """
        html = await self.get_html(self.base_url)
        # logging.info(type(html))
        soup = bs(html, "lxml")
        pagination = [page.text for page in soup.find_all(class_="pagination-item-JJq_j")]
        pagination_interval = [int(pagination[i]) for i in (1, -2)]
        #Костыль, надо попровить!)
        pagination_interval[1] += 1
        #Тестируем на небольшом пуле страниц, пока не поймем как сделать так, чтобы нас не банили)
        all_pages_links = (f"{self.base_url}&p={page}" for page in range(1, 2))
        return all_pages_links

    async def get_page_links(self, url) -> tuple[str]:
        """
        Получаем список ссылок объявлений для каждой странице
        :param url:
        :return:
        """
        html = await self.get_html(url)
        soup = bs(html, "lxml")
        try:
            ads = soup.find(class_="items-items-kAJAg").find_all(class_="iva-item-content-UnQQ4")
        except AttributeError:
            logger.error(f"{url}", exc_info=True)
        links = tuple(link.a.get("href") for link in ads)
        return links

    async def get_link_data(self, link) -> dict:
        """
        Получаем данные из объявления
        :param link:
        :return:
        """
        #TODO: добавить скачку фотографий
        soup = bs(await self.get_html(link), 'lxml')
        item_params = {}
        item_param_list = (item.text.strip() for item in soup.find_all(class_='item-params-list-item'))

        for param in item_param_list:
            key, value = param.replace(u'\xa0', u' ').split(": ")
            item_params.update({key: value})

        data = {
            'title': soup.find(class_='title-info-title-text').text.strip().replace(u'\xa0', u' '),
            'price': soup.find(class_='js-item-price').text.strip().replace(u'\xa0', u' '),
            'item-param_list': item_params,
            'description': soup.find(class_='item-description-text').text.strip().replace(u'\xa0', u' '),
            'link': link,
        }

        return data

    @staticmethod
    def to_json(data):
        with open("data.json", 'a') as file:
            json_data = json.dumps(data)
            file.write(json_data)


async def main() -> None:
    a = Avito()
    all_pages_links = await a.get_all_pages_links()
    page_links_tasks = (asyncio.create_task(a.get_page_links(link)) for link in all_pages_links)
    page_links = await asyncio.gather(*page_links_tasks)
    ads_links = ("".join(("https://www.avito.ru", url)) for page in page_links for url in page)
    ads_data_tasks = [asyncio.create_task(a.get_link_data(ad_link)) for ad_link in ads_links]
    all_ads_data = await asyncio.gather(*ads_data_tasks)
    a.to_json(all_ads_data)


if __name__ == "__main__":
    logging.basicConfig(level="INFO")
    logger = logging.getLogger("Avito parser")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())