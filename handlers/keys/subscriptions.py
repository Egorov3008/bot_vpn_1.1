import base64

import aiohttp
from aiohttp import web

from config import CLUSTERS
from logger import logger


async def fetch_url_content(url):
    """
    Получает содержимое по указанному URL и декодирует его из base64.

    :param url: URL, с которого нужно получить содержимое.
    :return: Список строк, полученных из декодированного содержимого, или пустой список в случае ошибки.
    """
    try:
        logger.debug(f"Получение URL: {url}")
        async with aiohttp.ClientSession() as session:
            async with session.get(url, ssl=False) as response:
                if response.status == 200:
                    content = await response.text()
                    logger.debug(f"Успешно получен контент с {url}")
                    return base64.b64decode(content).decode("utf-8").split("\n")
                else:
                    logger.error(
                        f"Не удалось получить {url}, статус: {response.status}"
                    )
                    return []
    except Exception as e:
        logger.error(f"Ошибка при получении {url}: {e}")
        return []


async def combine_unique_lines(urls, query_string):
    """
    Объединяет уникальные строки из содержимого, полученного по списку URL.

    :param urls: Список URL, из которых нужно получить содержимое.
    :param query_string: Строка запроса, которая будет добавлена к каждому URL.
    :return: Список уникальных строк, полученных из всех URL.
    """
    all_lines = []
    logger.debug(f"Начинаем объединение подписок для запроса: {query_string}")

    urls_with_query = [f"{url}?{query_string}" for url in urls]
    logger.debug(f"Составлены URL-адреса: {urls_with_query}")

    for url in urls_with_query:
        lines = await fetch_url_content(url)
        all_lines.extend(lines)

    all_lines = list(set(filter(None, all_lines)))
    logger.debug(
        f"Объединено {len(all_lines)} строк после фильтрации и удаления дубликатов"
    )

    return all_lines


async def handle_subscription(request):
    """
    Обрабатывает запрос на подписку и возвращает объединенные подписки для указанного email.

    :param request: Объект запроса, содержащий информацию о подписке.
    :return: Ответ с объединенными подписками в формате base64.
    """
    email = request.match_info["email"]
    logger.info(f"Получен запрос на подписку для email: {email}")

    urls = []
    for cluster in CLUSTERS.values():
        for server in cluster.values():
            server_subscription_url = f"{server['SUBSCRIPTION']}/{email}"
            urls.append(server_subscription_url)

    query_string = request.query_string
    logger.debug(f"Извлечен query string: {query_string}")

    combined_subscriptions = await combine_unique_lines(urls, query_string)

    base64_encoded = base64.b64encode(
        "\n".join(combined_subscriptions).encode("utf-8")
    ).decode("utf-8")

    headers = {
        "Content-Type": "text/plain; charset=utf-8",
        "Content-Disposition": "inline",
        "profile-update-interval": "7",
        "profile-title": email,
    }

    logger.info(f"Возвращаем объединенные подписки для email: {email}")
    return web.Response(text=base64_encoded, headers=headers)