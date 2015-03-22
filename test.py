from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException





# def downloadGradesToTextFileAlphaVersion():
# 	driver = webdriver.Firefox()
# 	driver.get("https://be.my.ucla.edu/")	
# 	username = driver.find_element_by_xpath("(//input)[1]")
# 	password = driver.find_element_by_xpath("(//input)[2]")	
# 	loginInfo = extractPasswords()
# 	username.send_keys(loginInfo[0])
# 	password.send_keys(loginInfo[1])
# 	password.send_keys(Keys.RETURN)
# 	try:
# 		element = WebDriverWait(driver, 10).until(
# 			EC.title_is("UCLA Logon")
# 			)
# 	except TimeoutException:
# 		print "Timeout error"
# 		driver.quit()
# 		exit()
# 	#
# 	driver.implicitly_wait(10)	
# 	#grades1 = driver.find_element_by_id("ctl00_MainContent_studyListDataList_ctl01_gradesButton")
# 	#print grades1
# 	#grades1.click()	

# 	classID_list = []
# 	for i in range(5):
# 		classID_list.append( "ctl00_MainContent_studyListDataList_ctl0" + `(2 * i + 1)` + "_gradesButton")
# 		print classID_list[i]	

# 	for i in range(5):
# 		grades = driver.find_element_by_id(classID_list[i])
# 		grades.click()
# 		driver.back()

# 	driver.close()



def downloadGradesToTestFile():
	print "Getting grades from myucla"
	classID_list = []
	for i in range(5):
		classID_list.append( "ctl00_MainContent_studyListDataList_ctl0" + `(2 * i + 1)` + "_gradesButton")

	driver = webdriver.PhantomJS('C:\Users\Guava\Desktop\TestDir\phantomjs-1.9.8-windows\phantomjs-1.9.8-windows\phantomjs.exe')
	driver.get("https://my.ucla.edu/")	
	signin = driver.find_element_by_xpath("//*[@id='ctl00_signInLink']")
	signin.click()
	try:
		element = WebDriverWait(driver, 10).until(
			EC.title_is("UCLA Logon")
			)
	except TimeoutException:
		print "Timeout error"
		driver.quit()
		exit()
	username = driver.find_element_by_xpath("(//input)[1]")
	password = driver.find_element_by_xpath("(//input)[2]")	
	loginInfo = extractPasswords()
	username.send_keys(loginInfo[0])
	password.send_keys(loginInfo[1])
	password.send_keys(Keys.RETURN)
	try:
		element = WebDriverWait(driver, 10).until(
			EC.title_contains("Study List")
			)
	except TimeoutException:
		print "Timeout error"
		driver.quit()
		exit()
	fp_curgrades = open('grades.txt', 'w')
	try:
		for gradelink in classID_list:
			grades = driver.find_element_by_id(gradelink)
			grades.click()
			try:
				element = WebDriverWait(driver, 20).until(
					EC.title_contains("Exam and Homework Grades")
					)
			except TimeoutException:
				print "Timeout error"
				driver.quit()
				exit()

			lectureName = driver.find_element_by_class_name("term_display")
			class_title = "------------------------------------------\n%s\n------------------------------------------\n" % (lectureName.text,)
			fp_curgrades.write(class_title)

			list_tablerows = driver.find_elements(By.TAG_NAME, "tr")
			for row in list_tablerows:
				fp_curgrades.write(format(row.text) + "\n")
			driver.back()
			fp_curgrades.write("\n\n\n")
			driver.get("https://be.my.ucla.edu/studylist.aspx")

			try:
				element = WebDriverWait(driver, 20).until(
					EC.title_contains("Study List")
					)
			except TimeoutException:
				print "Timeout error"
				driver.quit()
				fp_curgrades.close()
				exit()
	except NoSuchElementException:
		print "Finished!"
		driver.quit()
		fp_curgrades.close()
		exit()


def extractPasswords():
	fp = open('logininfo.txt', 'r')
	info = []
	info.append((fp.readline()).strip())
	info.append((fp.readline()).strip())
	fp.close()
	return info




if __name__ == "__main__":
	downloadGradesToTestFile()