import aiohttp
import asyncio
from collections import namedtuple
import os


class Randomduk:
    def __init__(self):
        self.user_agent = 'randomduk.py/v0.1'
        loop = asyncio.get_event_loop()
        self.session = aiohttp.ClientSession(loop=loop)

    async def random(self, *args, **kwargs):
        content_type = kwargs.get('type', None)
        if content_type is None:
            query = ''
        elif content_type is 'gif':
            query = '?type=gif'
        elif content_type is 'jpg':
            query = '?type=jpg'
        else:
            query = '?type={}'.format(type)
        async with self.session.get('https://random-d.uk/api/v1/random{}'.format(query)) as r:
            if r.status == 200:
                body = await r.json()
                response = namedtuple('Response', ['message', 'url'])
                return response(message=body['message'], url=body['url'])
            else:
                raise CouldNotGetDuckError(r.status)

    async def getimg(self, number):
        return 'https://random-d.uk/api/v1/images/{}.jpg'.format(number)

    async def getgif(self, number):
        return 'https://random-d.uk/api/v1/gifs/{}.gif'.format(number)

    async def httpduck(self, number):
        return 'https://random-d.uk/api/v1/http/{}.jpg'.format(number)

    async def upload(self, file):
        sending_file = open(file, 'rb')
        async with self.session.post("https://random-d.uk/api/v1/add",data={"data": sending_file}) as r:
            os.remove(file)
            if r.status == 200:
                return 'File uploaded!'
            else:
                result = await r.json()
                message = result['message']
                raise CouldNotUploadError(r.status, message)


class CouldNotGetDuckError(Exception):
    pass


class CouldNotUploadError(Exception):
    def __init__(self, status, message):
        self.status = status
        self.message = message

