import subprocess
import asyncio
import nodriver as uc
import random
import requests
import os.path
import os

async def main():
    #connect_server()
    await asyncio.sleep(1)
    browser = await uc.start()
    page = await browser.get('https://www.google.com')
    await asyncio.sleep(20000000)


uc.loop().run_until_complete(main())


