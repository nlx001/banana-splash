import subprocess
import asyncio
import nodriver as uc
import random
import requests
import os.path
import os

my_user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"

async def main():
    #connect_server()
    await asyncio.sleep(1)
    browser = await uc.start(browser_args=[f"--user-agent={my_user_agent}", "--window-size=1920,1080"])
    page = await browser.get('https://www.google.com')
    await asyncio.sleep(20000000)


uc.loop().run_until_complete(main())


