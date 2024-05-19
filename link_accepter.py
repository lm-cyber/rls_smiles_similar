from selenium.webdriver.common.by import By
from data_parser import parser_data




def get_links(driver, url="https://www.rlsnet.ru/active-substance/ukazatel"):
    driver.get(url)

    data = driver.find_element(value="alphabet-ru").find_element(by=By.CLASS_NAME,value="head")
    links = []
    for j in data.find_elements(by=By.TAG_NAME,value="a"):
        links.append(j.get_attribute("href"))
    return links

def get_drug_link(driver, links):
    links_drug=[]
    for link in links:
        driver.get(link)
        data = driver.find_elements(by=By.CLASS_NAME,value="b-alphabet-list")
        for i in data:
            for j in i.find_elements(by=By.TAG_NAME,value="a"):
                links_drug.append(j.get_attribute("href"))
    return links_drug
