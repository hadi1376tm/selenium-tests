from selenium import webdriver

PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
page = input("enter your site (ex: https://www.digikala.com): " )
driver.get(page)
print("searching for ERROR [Links with identical texts should have identical targets]:\n")
flag = False
links = driver.find_elements_by_xpath("//a[@href]")

for i in range(len(links)):
    for j in range(i + 1, len(links)):
        if links[i].text == links[j].text and links[i].text!= "":
            if links[i].get_attribute('href') != links[j].get_attribute('href'):
                print(""+str(links[i].get_attribute('href')) + " (" + links[i].text + ") and " +
                      str(links[j].get_attribute('href')) + " (" + links[j].text +
                      ") have identical texts but not identical targets.")
                flag = True
if not flag:
    print("NULL")
driver.close()
