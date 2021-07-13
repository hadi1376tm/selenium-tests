from selenium import webdriver

PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
page = input("enter your site (ex: https://www.digikala.com): " )
driver.get(page)
flag = False
print("searching for ERROR [Meta tags should not be used to refresh or redirect]:\n")

elems=driver.find_elements_by_xpath("//meta[@http-equiv='refresh']")
for elem in elems:
    print("content: "+elem.get_attribute("content"))
    flag = True
if not flag:
    print("NULL")
driver.close()
