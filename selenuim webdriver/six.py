from selenium import webdriver

PATH = "C:\chromedriver.exe"
#PATH2 = "C:\ firefoxdriver.exe"
driver1 = webdriver.Chrome(PATH)
#driver2 = webdriver.firefox(PATH2)
#divers=[driver1,driver2]
divers=[driver1]
windows_sizes = [(800, 600), (1024, 768), (1448, 1072), (1600, 1200), (2048, 1536)]

flag = False

tags = ['input', 'select', 'textarea', 'button']
elements = []
for driver in divers:
    page = input("enter your site (ex: https://www.digikala.com): ")
    driver.get(page)
    print("searching for ERROR [Elements with overlap]:\n")
    for tag in tags:
        elements += driver.find_elements_by_xpath('//' + tag)
        for width, height in windows_sizes:
            driver.set_window_size(width, height)
            for i in range(len(elements)):
                for j in range(i + 1, len(elements)):
                    if elements[i].location['y'] >= elements[j].location['y']:
                        if elements[i].location['y'] <= elements[j].location['y'] + elements[j].size['height']:
                            if elements[i].location['x'] >= elements[j].location['x']:
                                if elements[i].location['x'] <= elements[j].location['x'] + elements[j].size['width']:
                                    print('There is an overlap between input elements at location ' +
                                          str(elements[i].location) + ' and location ' + str(elements[j].location))
                                    flag = True

                            elif elements[i].location['x'] + elements[i].size['width'] >= elements[j].location['x']:
                                if elements[i].location['x'] + elements[i].size['width'] <= \
                                        elements[j].location['x'] + elements[j].size['width']:
                                    print('There is an overlap between input elements at location ' +
                                          str(elements[i].location) + ' and location ' + str(elements[j].location))
                                    flag = True

                    elif elements[i].location['y'] + elements[i].size['height'] >= elements[j].location['y']:
                        if elements[i].location['y'] + elements[i].size['height'] <= \
                                elements[j].location['y'] + elements[j].size['height']:
                            if elements[i].location['x'] >= elements[j].location['x']:
                                if elements[i].location['x'] <= elements[j].location['x'] + elements[j].size['width']:
                                    print('There is an overlap between input elements at location ' +
                                          str(elements[i].location) + ' and location ' + str(elements[j].location))
                                    flag = True

                            elif elements[i].location['x'] + elements[i].size['width'] >= elements[j].location['x']:
                                if elements[i].location['x'] + elements[i].size['width'] <= \
                                        elements[j].location['x'] + elements[j].size['width']:
                                    print('There is an overlap between input elements at location ' +
                                          str(elements[i].location) + ' and location ' + str(elements[j].location))
                                    flag = True

if not flag:
    print("NULL")
driver.close()
