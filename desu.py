from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get("http://grymoire.com/Unix/sed.html")	

for tabledesu in driver.find_elements(By.TAG_NAME, "tr"):
	text1 = tabledesu.text
	print format(text1)