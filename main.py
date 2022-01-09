import requests
from bs4 import BeautifulSoup as bs
import asyncio
from pprint import pprint
import logging
from fake_useragent import UserAgent
# from fake_useragent import UserAgent
# from requests_html import HTMLSession


class Avito:

    def __init__(self):
        self.base_url = "https://www.avito.ru/sankt-peterburg/nedvizhimost?cd=1&metro=155-156-157-158-160-162-163-164-165-169-173-174-175-176-178-179-180-181-185-187-189-190-191-199-201-202-203-205-209-210-211-1015-1016-1017-2122-2132"
        # self.ua = UserAgent(verify_ssl=False, use_cache_server=False, cache=False)
        # self.ua = UserAgent()

    async def get_html(self, url):
        # logger.info(self.ua.chrome)
        response = requests.get(url)
        return response.text

    async def get_all_pages_links(self):
        """
        Берем номера страниц из пагинации и добавляем к каждоый ссылке.
        Вормирвуем список ссылок
        :return:
        """
        html = await self.get_html(self.base_url)
        logging.info(html)
        soup = bs(html, "lxml")
        pagination = [page.text for page in soup.find_all(class_="pagination-item-JJq_j")]
        logging.info(f"{pagination=}")
        pagination_interval = [int(pagination[i]) for i in (1, -2)]
        #Костыль, надо попровить!)
        pagination_interval[1] += 1
        all_pages_links = [f"{self.base_url}&p={page}" for page in range(*pagination_interval)]
        return all_pages_links

    async def get_page_links(self, url):
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

    async def get_link_data(self, link):
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

        pprint(data)
        return data


async def main():
    a = Avito()
    all_pages_links = await a.get_all_pages_links()
    pprint(all_pages_links)
    page_links_tasks = [await a.get_page_links(link) for link in all_pages_links]
    page_links = await asyncio.gather(*page_links_tasks)
    pprint(page_links)

if __name__ == "__main__":
    logging.basicConfig(level="INFO")
    logger = logging.getLogger("Avito parser")
    asyncio.run(main())