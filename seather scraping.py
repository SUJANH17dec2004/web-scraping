from selenium import webdriver  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.chrome.options import Options

option = webdriver.ChromeOptions()
option.add_argument('headless')
PATH= 'C:\Program Files (x86)\chromedriver\chromedriver.exe'
drvr = webdriver.Chrome(PATH,options=option)

drvr.get("https://www.google.com/search?q=weather+in+bangalore&oq=weather+in+bangalore&aqs=chrome..69i57.3343j0j4&sourceid=chrome&ie=UTF-8")

temp_search = drvr.find_element_by_class_name("wob_t")
condition_search = drvr.find_element_by_id("wob_dc")

print(temp_search.text,"degrees")
print(condition_search.text)