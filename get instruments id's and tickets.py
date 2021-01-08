from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
#nice yassine
instruments_ids = dict()
nbrs=['02','04','06','08']
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 3)

def fct(xpath):
    driver.get("http://www.casablanca-bourse.com/bourseweb/Liste-Societe.aspx?IdLink=20&Cat=7")
    indice = driver.find_element_by_xpath(xpath)
    link=str(indice.get_attribute('href'))
    instru_id=int(link[72:link.index("&")])
    name=str(indice.text)
    instruments_ids[name] = [instru_id,'']
    indice.click()
    sleep(0.5)
    indice = driver.find_element_by_xpath('//*[@id="SocieteCotee1_LBFicheTech"]')
    indice.click()
    element = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="SocieteCotee1_FicheTechnique1_lblTicker"]')))    
    indice = driver.find_element_by_xpath('//*[@id="SocieteCotee1_FicheTechnique1_lblTicker"]')
    instruments_ids[name][1]=indice.text

try :
    for nbr in nbrs :
        xpath='//*[@id="ListSocieteControl1_ListSociete1_RptrScCote_ctl'+str(nbr)+'_A1"]'
        fct(xpath)
        
    for i in range(4,80,2):
        xpath='//*[@id="arial11bleu"]/tbody/tr['+str(i)+']/td[4]/a'
        fct(xpath)

    for i in range(10,78,2):
        xpath='//*[@id="ListSocieteControl1_ListSociete1_RptrScCote_ctl'+str(i)+'_A1"]'
        fct(xpath)

except Exception as e:
    print(instruments_ids)
    driver.close()
    print(e)

print(instruments_ids)
driver.close()