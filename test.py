from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def downloadGradesToTextFile():
	driver = webdriver.Firefox()
	driver.get("https://be.my.ucla.edu/")	
	username = driver.find_element_by_xpath("(//input)[1]")
	password = driver.find_element_by_xpath("(//input)[2]")	
	#gonna store my stuff in a local file LOL I r stupid
	username.send_keys("howdy")
	password.send_keys("desu")
	password.send_keys(Keys.RETURN)
	driver.implicitly_wait(10)	

	#grades1 = driver.find_element_by_id("ctl00_MainContent_studyListDataList_ctl01_gradesButton")
	#print grades1
	#grades1.click()	

	classID_list = []
	for i in range(5):
		classID_list.append( "ctl00_MainContent_studyListDataList_ctl0" + `(2 * i + 1)` + "_gradesButton")
		print classID_list[i]	

	for i in range(5):
		grades = driver.find_element_by_id(classID_list[i])
		grades.click()
		driver.back()

	driver.close()



#downloadGradesToTextFile()
#WHY IT NO WORK AIYAH
#
classID_list = []
for i in range(5):
	classID_list.append( "ctl00_MainContent_studyListDataList_ctl0" + `(2 * i + 1)` + "_gradesButton")
	print classID_list[i]	
#driver = webdriver.Firefox()
driver = webdriver.PhantomJS('C:\Users\Guava\Desktop\TestDir\phantomjs-1.9.8-windows\phantomjs-1.9.8-windows\phantomjs.exe')
driver.get("https://my.ucla.edu/")	
signin = driver.find_element_by_xpath("//*[@id='ctl00_signInLink']")
signin.click()

driver.implicitly_wait(5)	
username = driver.find_element_by_xpath("(//input)[1]")
password = driver.find_element_by_xpath("(//input)[2]")	
username.send_keys("howdy")
password.send_keys("desu")
password.send_keys(Keys.RETURN)
driver.implicitly_wait(10)	

grades = driver.find_element_by_id(classID_list[0])
grades.click()
driver.implicitly_wait(20)	

#perhaps adding an explicit wait would be in order here
actualTitle = driver.current_url;
print actualTitle

actualTitle = driver.title;
print actualTitle

list_tablerows = driver.find_elements(By.TAG_NAME, "tr")
for row in list_tablerows:
	print format(row.text)
#driver.back()
#<a id="ctl00_MainContent_studyListDataList_ctl01_gradesButton" class="courseLink" href="javascript:__doPostBack('ctl00$MainContent$studyListDataList$ctl01$gradesButton','')">Grades</a>
#<a id="ctl00_MainContent_studyListDataList_ctl03_gradesButton" class="courseLink" href="javascript:__doPostBack('ctl00$MainContent$studyListDataList$ctl03$gradesButton','')">Grades</a>
#<a id="ctl00_MainContent_studyListDataList_ctl05_gradesButton" class="courseLink" href="javascript:__doPostBack('ctl00$MainContent$studyListDataList$ctl05$gradesButton','')">Grades</a>
#<a id="ctl00_MainContent_studyListDataList_ctl01_gradesButton" class="courseLink" href="javascript:__doPostBack('ctl00$MainContent$studyListDataList$ctl01$gradesButton','')">Grades</a>