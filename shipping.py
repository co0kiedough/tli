import requests, pyodbc, re, sys
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get('https://apps.commercehub.com/account/login?service=https://dsm.commercehub.com/dsm/shiro-cas')
assert "CommerceHub" in driver.title

un = driver.find_element_by_id('username')
pw = driver.find_element_by_id('password')
sub = driver.find_element_by_name('submit')
un.send_keys('tradelinker')
pw.send_keys('Traders14!')
sub.send_keys(Keys.RETURN)
driver.back()

driver.get('https://dsm.commercehub.com/dsm/gotoOrderSummary.do')

ac = ActionChains(driver)
olink = driver.find_element_by_partial_link_text('Activi')
ac.move_to_element(olink).click(olink).perform()

pos = driver.find_elements_by_css_selector('a.simple_link')
td = {}
import csv
upsfile = open('C:\\Users\\Selena\\Desktop\\UPS Export Files\\UPS_CSV_EXPORT.csv', 'r', newline='')
upscsv = csv.DictReader(upsfile)

for rows in upscsv:
    td[rows['PackageReference1']] = rows
inp = driver.find_elements_by_css_selector('tr.or_white_interstices')

from selenium.webdriver.support.ui import Select

sm = 2
ti = 1
af = 0
for i in range(len(pos)):
    track = td[pos[i].text]['PackageTrackingNumber']
    meth = td[pos[i].text]['ShipmentInformationServiceType']
    if meth == 'Ground':
        themeth = 'UG'
    else:
        themeth = 'UPSN_ST'
    
    trackinput = inp[ti].find_elements_by_css_selector('input')
    autofill = inp[af].find_element_by_name('autofill')
    shipmethod = inp[sm].find_elements_by_css_selector('select')
    ship = Select(shipmethod[0])
    trackinput[0].send_keys(str(track))
    autofill.click()
    ship.select_by_value(themeth)

    ti+=3
    af+=3
    sm+=3
    i+=1
    
    
    
    
