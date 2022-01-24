from collections import namedtuple
import time
import asyncio
from concurrent.futures import FIRST_COMPLETED
from aiohttp import ClientSession
import socket


Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)

async def fetch_ip(service, session):
    async with session.get(service.url) as response:
        json = await response.json()
        return json[service.ip_attr]


async def asynchronous():
    async with ClientSession() as session:
        tasks = [asyncio.create_task(fetch_ip(service, session))
                 for service in SERVICES]
        done, pending = await asyncio.wait(tasks, timeout=None,
                                           return_when=FIRST_COMPLETED)
        for i in done:
            print(i.result())

ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())

# 46.242.14.68