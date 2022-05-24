from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:/Users/shiss/OneDrive/Desktop/class127/chromedriver")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers = ["name", "distance", "mass", "radius"]
    stars = []
    for i in range(0, 428):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for tr in soup.find_all("td", attrs={"class", "mw-parser-output"}):
            td = tr.find_all("td")
            temp_list = []
            for index, td in enumerate(td):
                if index == 0:
                    temp_list.append(td.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(td.contents[0])
                    except:
                        temp_list.append("")
            stars.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(stars)
scrape()
