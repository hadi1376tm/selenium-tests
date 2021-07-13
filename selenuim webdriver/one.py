from selenium import webdriver

imgs = [".png", ".jpg" ".img ", "gif", "svg", '.tif', '.tiff','.png']
PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
page = input("enter your site (ex: https://www.digikala.com): " )
driver.get(page)
print("ERROR [Links should not directly target images]:\n")
flag = False
elems = driver.find_elements_by_xpath("//a[@href]")

for elem in elems:
    for img in imgs:
        if (elem.get_attribute("href").endswith(img)):
            print(elem.get_attribute("href"))
            flag = True
if not flag:
    print("NULL")

driver.close()
