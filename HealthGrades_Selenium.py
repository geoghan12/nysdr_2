from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv
import time

#<a href="javascript:document.frmMain.action.value='display_physician_info';document.frmMain.PhysicianID.value=12094889;document.frmMain.submit();" title="For more information, click here.">AHMED, SHAMIM</a>
driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.get(r"https://www.healthgrades.com/usearch?what=Obstetrics%20%26%20Gynecology&entityCode=PS574&searchType=PracticingSpecialty&spec=45&category=Provider&where=NYC%2C%20NY&pt=40.6501038%2C%20-73.9495823&distances=10&pageNum=1&source=Osm&city=NYC&state=NY")

dr_link=driver.find_elements_by_class_name('uCard')#uCard__Name')
dr_link[0].text
#dr_link=driver.find_element_by_xpath('//*[@id="card-carousel-search"]/div[2]/ul/li[1]/div/div/div[1]/div/div[2]/h3/a')
#'//*[@id="card-carousel-search"]/div[2]/ul/li[4]/div/div/div[1]/div/div[2]/h3/a'
print(dr_link)
#dr_link.click()

#driver.close()