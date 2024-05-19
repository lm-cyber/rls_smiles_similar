



from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.common.by import By
from data_parser import parser_data
from fake_useragent import UserAgent
import undetected_chromedriver as uc
import json
from link_accepter import get_links, get_drug_link
# firefox_options = Options()
# driver = webdriver.Firefox(options=firefox_options)
# links = get_links(driver)
# # print(links)
# drug_links = get_drug_link(driver,links)
# with open("links.txt","w") as f:
#     for i in drug_links:
#         f.write(i+"\n")
import pandas as pd

from time import sleep
from random import randint
with open("links.txt","r") as f:
    drug_links = f.readlines()
import gc
drug_links = drug_links[689:]
# print(drug_links[0])
data_parsed = []
ua = UserAgent()
user_agent = ua.random

chrmium_opt = ChromiumOptions()
chrmium_opt.add_argument(f'user-agent={user_agent}')

driver = uc.Chrome(driver_executable_path="chromedriver",options=chrmium_opt)

last = 689
last_check = True

def get_drugs(now):
    global last, user_agent, chrmium_opt, driver, df, data_parsed, last_check
    for j, i in enumerate(drug_links):
        last = j
        sleep(randint(1, 3))
        driver.get(i)
        data = driver.find_element(by=By.CLASS_NAME, value="content")
        data_parsed.append(parser_data(data))
        if j > 23 and j % 25 == 0:
            driver.quit()
            user_agent = ua.random
            chrmium_opt = ChromiumOptions()
            chrmium_opt.add_argument(f'user-agent={user_agent}')
            driver = uc.Chrome(driver_executable_path="chromedriver", options=chrmium_opt)
        if j > 20 and j % 150 == 0:
            df = pd.DataFrame(data_parsed)
            df.to_csv(f"data_df/data{j+last}.csv", index=False)
            df = None
            data_parsed = []
            gc.collect()

    last_check = False

while last_check:
    try:
        get_drugs(last)
    except Exception as e:
        print(e)
        sleep(1800)



with open("last.txt","w") as f:
    f.write(str(last))
df = pd.DataFrame(data_parsed)
df.to_csv(f"data_df/data_LL{last}.csv",index=False)


# driver.get("https://www.rlsnet.ru/active-substance/abakavir-2441")
# data = driver.find_element(by=By.CLASS_NAME,value="content")
# print(parser_data(data))
#
# driver.get("https://www.rlsnet.ru/active-substance/ukazatel")
#
# data = driver.find_element(value="alphabet-ru").find_elements(by=By.CLASS_NAME,value="item")
# for i in data:
#     for j in i.find_elements(by=By.TAG_NAME,value="a"):
#         print(j.get_attribute("href"))
#         print(j.text)
