import requests
from bs4 import BeautifulSoup as bs
import asyncio
from pprint import pprint
from fake_useragent import UserAgent
from requests_html import HTMLSession


async def get_html(URL):
    response = requests.get(URL)
    return response.text


async def get_all_pages(html):
    soup = bs(html, "lxml")
    pages = [page.text for page in soup.find_all(class_="pagination-item-JJq_j")]
    return int(pages[1]), int(pages[-2]) + 1


async def get_page_links(html):
    soup = bs(html, "lxml")
    ads = soup.find(class_="items-items-kAJAg").find_all(class_="iva-item-content-UnQQ4")
    links = (link.a.get("href") for link in ads)
    return links


async def get_link_data(link):
    #TODO: добавить скачку фотографий
    soup = bs(await get_html(link), 'lxml')
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
    URL = "https://www.avito.ru/sankt-peterburg/nedvizhimost?cd=1&metro=155-156-157-158-160-162-163-164-165-169-173-174-175-176-178-179-180-181-185-187-189-190-191-199-201-202-203-205-209-210-211-1015-1016-1017-2122-2132"
    # await get_page_links(await get_html(URL))
    await get_all_pages(await get_html(URL))

if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    # loop.gather(main)
    asyncio.run(main())
    #asyncio.run(get_link_data('https://www.avito.ru/sankt-peterburg/kvartiry/kvartira-studiya_26m_1419et._2287333609'))
    # main()