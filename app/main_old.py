from fastapi import FastAPI
import asyncio
import aiohttp
from fastapi.params import Depends
import requests
from concurrent.futures import ThreadPoolExecutor

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


class HttpClient(object):

    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_)
        return class_._instance

    def __init__(self, url):
        self.url = url

    async def fetch(self, session):
        async with session.get(self.url) as response:
            return await response.json()


global_client = HttpClient("https://dog.ceo/api/breeds/image/random")


def get_client():
    return global_client


@app.get("/test-async")
async def send_concurrent_requests(client: HttpClient = Depends(get_client)):
    """ Use python requests with asyncio.gather to send concurrent requests
    """
    print('Client ID:', id(client))

    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(100):
            tasks.append(client.fetch(session))

        results = await asyncio.gather(*tasks)
        return results


@app.get("/test")
def send_sync_requests():
    """ Use python requests to send synchronous requests
    """

    URL = "https://dog.ceo/api/breeds/image/random"

    results = []
    for _ in range(50):
        results.append(requests.get(URL).json())

    return results


@app.get("/test-thread")
def send_threaded_requests():
    """ Use python requests with threading to send concurrent requests
    """

    URL = "https://dog.ceo/api/breeds/image/random"

    def fetch(url):
        return requests.get(url).json()

    with ThreadPoolExecutor(max_workers=200) as executor:
        results = executor.map(fetch, [URL for _ in range(100)])

    return list(results)
