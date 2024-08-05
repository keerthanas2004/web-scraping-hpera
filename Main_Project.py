from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


service = Service(executable_path='/Users/Keerthana/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')
options = webdriver.ChromeOptions()
driver = Chrome(service=service, options=options)
driver.get('https://hprera.nic.in/PublicDashboard')

time.sleep(35)

html = driver.page_source
soup = BeautifulSoup(html,"html.parser")

project_container = soup.find_all('div', {'class':'form-row'})
main_container = project_container[10]
driver.find_element(By.XPATH,'//*[@id="tab_project_main-filtered-data"]/ul/li[1]/a').click()

i = 0
gst = []
pan = []
name = []
addr = []
name_project = []
project_name = main_container.find_all('span',{'class':'font-lg fw-600'})
for project in project_name[:6]: 
    xpath = '//*[@id="reg-Projects"]/div/div/div['+str(i+1)+']/div/div/a'
    driver.find_element(By.XPATH,xpath).click()

    time.sleep(5)

    rows=1+len(driver.find_elements(By.XPATH,'//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr'))
    for j in range(1,rows,1):
        value = driver.find_element(By.XPATH,'//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr['+str(j)+']/td[1]').text
        if(value == "GSTIN No."):
            gst.append(driver.find_element(By.XPATH,'//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr['+str(j)+']/td[2]/span').text)
        if(value == "PAN No."):
            pan.append(driver.find_element(By.XPATH,'//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr['+str(j)+']/td[2]/span').text)
        if(value == "Name"):
            name.append(driver.find_element(By.XPATH,'//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr['+str(j)+']/td[2]').text)
        if(value == "Permanent Address"):
            addr.append(driver.find_element(By.XPATH,'//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr['+str(j)+']/td[2]/span').text)
    name_project.append(project_name[i].text)

    i = i+1

    driver.find_element(By.XPATH,'//*[@id="modal-data-display-tab_project_main"]/div/div/div[3]/button').click()

for k in range(0,6,1):
    print("PROJECT NUMBER ",(k+1))
    print("Name of the Project: ",name_project[k])
    print("GSTIN No.: ",gst[k])
    print("PAN Number: ",pan[k])
    print("Name: ",name[k])
    print("Permanent Address: ",addr[k])
    print()