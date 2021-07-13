from selenium import webdriver

PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
page = input("enter your site (ex: https://www.digikala.com): " )
driver.get(page)
print("searching for ERROR [The 'style' attribute should not be used]:\n")

elems = driver.find_elements_by_xpath('//*[@style]')

if len(elems) == 0:
    print("NULL")
else:
    count = len(elems)
    print("Found" +{str(len(elems))}+" 'style' attributes ")

driver.close()
