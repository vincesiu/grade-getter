from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


driver = webdriver.PhantomJS('C:\Users\Guava\Desktop\TestDir\phantomjs-1.9.8-windows\phantomjs-1.9.8-windows\phantomjs.exe')
driver.get("https://my.ucla.edu/")	
signin = driver.find_element_by_xpath("//*[@id='ctl00_signInLink']")
signin.click()
#driver.implicitly_wait(5)

try:
    element = WebDriverWait(driver, 10).until(
        EC.title_contains("UCLA Logon")
    )
except TimeoutException as excep:
	print "Timeout error"
	exit()
	

print "Success"