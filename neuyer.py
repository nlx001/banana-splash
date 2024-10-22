from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import subprocess
import random
import time

def list_servers():
    command = ["mullvad", "relay", "list"]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    server_listt = result.stdout.splitlines()
    server_list = []
    for server in server_listt:
        if "WireGuard" in server.strip() or "OpenVPN" in server.strip():
            server_list.append(server.strip().split(" ")[0])
    return server_list


def connect_server():
    server_list = list_servers()
    server_name = random.choice(server_list)
    
    command = ["mullvad", "relay", "set", "location", server_name.split("-")[0], server_name.split("-")[1], server_name]
    subprocess.run(command, check=True)
    command = ["mullvad", "connect"]
    subprocess.run(command, check=True)
    return server_name


links = [
"https://ouo.io/UOopAkC",
"https://ouo.io/AKOocS",
"https://ouo.io/cgfu5W",
"https://ouo.io/4f1cv1",
"https://ouo.io/Nn2jmI",
"https://ouo.io/WLqYOd",
"https://ouo.io/lMcFcf",
"https://ouo.io/pF2mTw",
"https://ouo.io/o15d4f3",
"https://ouo.io/ct46jb",
"https://ouo.io/xWLuZEi",
"https://ouo.io/Y1hctg",
"https://ouo.io/xT9yedP",
"https://ouo.io/70yuSK",
"https://ouo.io/Ba6Tg1z",
"https://ouo.io/Eoukd2",
"https://ouo.io/AIbxXBk",
"https://ouo.io/EJouZNQ",
"https://ouo.io/IkQy1al",
"https://ouo.io/UXv67GM",
"https://ouo.io/vwd5ZP",
"https://ouo.io/qO7R92",
"https://ouo.io/TCbS4w",
"https://ouo.io/fakBjF",
"https://ouo.io/3y9lfh",
"https://ouo.io/hAI4PPq",
"https://ouo.io/Ie8km8",
"https://ouo.io/XJl7jO",
"https://ouo.io/K7CIpi",
"https://ouo.io/Hl30gvf",
"https://ouo.io/dNQyMP",
"https://ouo.io/y1ljU1",
"https://ouo.io/nH4l4i",
"https://ouo.io/74TJyz",
"https://ouo.io/TjjY0N",
"https://ouo.io/HRRoBP9",
"https://ouo.io/NwSZiDN",
"https://ouo.io/0vwo3TJ",
"https://ouo.io/EA7kff",
"https://ouo.io/nFsTGC",
"https://ouo.io/2ABlAO",
"https://ouo.io/VGC9os",
"https://ouo.io/ntGv8c",
"https://ouo.io/tlHMxZw",
"https://ouo.io/2VYW4D",
"https://ouo.io/IzXcyN",
"https://ouo.io/r7LujoH",
"https://ouo.io/jTEjfU",
"https://ouo.io/xWTvzpW",
"https://ouo.io/q3Zm8Q",
"https://ouo.io/l24E4Bh",
"https://ouo.io/7TCY3F",
"https://ouo.io/VoPE8I",
"https://ouo.io/ctaHyh",
"https://ouo.io/hSjCREQ",

]


start_time = time.time()
##subprocess.run(["nmcli", "connection", "up", "us.protonvpn.udp"])
for i in range(500):
    time.sleep(random.randint(4,15))
    try:
        connect_server()
        options = Options()
        #options.add_argument('--headless')
        service = Service()
        driver = webdriver.Firefox(service=service, options=options)
        driver.set_page_load_timeout(20)
       # time.sleep(5000)
        driver.get("https://www.nulledbb.com")

        driver.get(random.choice(links))
        time.sleep(5)

        button = driver.find_element(By.XPATH, '//*[@id="btn-main"]')
        class_name = button.get_attribute("class")
        #print(class_name)

        button.click()
        time.sleep(5)
        state = True
        try:
            frame = driver.find_element(By.XPATH, "/html/iframe[2]")
            frame.click()
            time.sleep(random.randint(3,4))
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(1)
            state = False
            print("first frame found")
        except:
            print("first frame not found")
        time.sleep(1)
        try:
            frame = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(11)")
            frame.click()
            time.sleep(random.randint(3,4))
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(1)
            state = False
            print("first div11 found")
        except:
            print("first div11 not found")

        if state:
            try:
                ad = driver.find_element(By.XPATH, "//div[@style='text-align: center; padding-top: 48vh; font-size: 4vw; position: fixed; display: block; width: 100%; height: 100%; inset: 0px; background-color: rgba(0, 0, 0, 0); z-index: 300000;']")
                ad.click()
                time.sleep(random.randint(3,4))
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(1)
                print("first div10 found")
            except:
                print("first div10 not found")
        state = True
        try:
            frame = driver.find_element(By.XPATH, "/html/iframe[2]")
            frame.click()
            time.sleep(random.randint(3,4))
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(1)
            state = False
            print("second frame found")
        except:
            print("second frame not found")
        time.sleep(1)
        try:
            frame = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(11)")
            frame.click()
            time.sleep(random.randint(3,4))
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(1)
            state = False
            print("second div11 found")
        except:
            print("second d11 not found")

        if state:
            try:
                ad = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(10)")
                ad.click()
                time.sleep(random.randint(3,4))
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(1)
                print("second div 10 found")
            except:
                print("second div10 not found")
        #time.sleep(3000)
        html = driver.page_source
        button = driver.find_element(By.XPATH, '//*[@id="btn-main"]')
        button.click()
        time.sleep(3)
        driver.quit()
    except Exception as e:
        print(e)
        print(html)
        driver.quit()


end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken to run the function: {elapsed_time} seconds")
##subprocess.run(["nmcli", "connection", "down", "us.protonvpn.udp"])
        

# body > div:nth-child(11)