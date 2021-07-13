from selenium import webdriver

flag = False

def check_attribute(tags, attribute):

    for tag in tags:
        elements = driver.find_elements_by_xpath('//' + tag + '[@' + attribute + ']')
        if len(elements) != 0:
            print("attribute " + attribute + " in tag " + tag )
            flag = True

attribute_tags_list = list()
attribute_tags_list.append([['form'], 'accept'])
attribute_tags_list.append([['caption', 'col', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'iframe', 'div', 'embed'
                        , 'img', 'object', 'p', 'table', 'tbody', 'thead', 'tfoot', 'td', 'input', 'legend'
                        , 'th', 'tr'], 'align'])
attribute_tags_list.append([['td', 'th'], 'axis'])
attribute_tags_list.append([['body', 'table', 'thead', 'tbody', 'tfoot', 'tr', 'td', 'th'], 'background'])
attribute_tags_list.append([['body', 'table', 'td', 'th', 'tr'], 'bgcolor'])
attribute_tags_list.append([['body'], 'alink'])
attribute_tags_list.append([['iframe'], 'allowtransparency'])
attribute_tags_list.append([['object'], 'archive'])
attribute_tags_list.append([['object'], 'border'])
attribute_tags_list.append([['table'], 'bordercolor'])
attribute_tags_list.append([['table'], 'cellpadding'])
attribute_tags_list.append([['table'], 'cellspacing'])
attribute_tags_list.append([['object'], 'classid'])
attribute_tags_list.append([['col', 'tbody', 'thead', 'tfoot', 'td', 'th', 'tr'], 'char'])
attribute_tags_list.append([['col', 'tbody', 'thead', 'tfoot', 'td', 'th', 'tr'], 'charoff'])
attribute_tags_list.append([['a', 'link'], 'charset'])
attribute_tags_list.append([['br'], 'clear'])
attribute_tags_list.append([['object'], 'code'])
attribute_tags_list.append([['object'], 'codebase'])
attribute_tags_list.append([['object'], 'codetype'])
attribute_tags_list.append([['hr'], 'color'])
attribute_tags_list.append([['dl', 'ol', 'ul'], 'compact'])
attribute_tags_list.append([['a'], 'coords'])
attribute_tags_list.append([['a', 'applet', 'button', 'div', 'fieldset', 'frame', 'iframe', 'img', 'input', 'label'
                           , 'legend', 'select', 'span', 'textarea', 'marquee', 'object', 'param'], 'datafld'])
attribute_tags_list.append([['button', 'div', 'input', 'label', 'legend', 'marquee', 'object', 'option', 'select'
                        , 'span', 'table'], 'dataformatas'])
attribute_tags_list.append([['table'], 'datapagesize'])
attribute_tags_list.append([['a', 'applet', 'button', 'div', 'frame', 'iframe', 'img', 'input', 'label'
                           , 'legend', 'marquee', 'object', 'option', 'select', 'span', 'textarea'], 'datasrc'])
attribute_tags_list.append([['object'], 'declare'])
attribute_tags_list.append([['script'], 'event'])
attribute_tags_list.append([['script'], 'for'])
attribute_tags_list.append([['table'], 'frame'])
attribute_tags_list.append([['iframe'], 'frameborder'])
attribute_tags_list.append([['td', 'th'], 'height'])
attribute_tags_list.append([['embed', 'iframe', 'img', 'input', 'object'], 'hspace'])
attribute_tags_list.append([['input'], 'ismap'])
attribute_tags_list.append([['body'], 'link'])
attribute_tags_list.append([['img'], 'lowsrc'])
attribute_tags_list.append([['body'], 'marginbottom'])
attribute_tags_list.append([['body', 'iframe'], 'marginheight'])
attribute_tags_list.append([['body'], 'marginleft'])
attribute_tags_list.append([['body'], 'marginright'])
attribute_tags_list.append([['body'], 'margintop'])
attribute_tags_list.append([['body', 'iframe'], 'marginwidth'])
attribute_tags_list.append([['a', 'link'], 'methods'])
attribute_tags_list.append([['td', 'th'], 'nowrap'])
attribute_tags_list.append([['head'], 'profile'])
attribute_tags_list.append([['table'], 'rules'])
attribute_tags_list.append([['embed', 'img', 'option'], 'name'])
attribute_tags_list.append([['area'], 'nohref'])
attribute_tags_list.append([['hr'], 'noshade'])
attribute_tags_list.append([['meta'], 'scheme'])
attribute_tags_list.append([['td'], 'scope'])
attribute_tags_list.append([['iframe'], 'scrolling'])
attribute_tags_list.append([['body'], 'text'])
attribute_tags_list.append([['li', 'param', 'ul'], 'type'])
attribute_tags_list.append([['a', 'link'], 'urn'])
attribute_tags_list.append([['input'], 'usemap'])
attribute_tags_list.append([['col', 'tbody', 'thead', 'tfoot', 'td', 'th', 'tr'], 'valign'])
attribute_tags_list.append([['param'], 'valuetype'])
attribute_tags_list.append([['html'], 'version'])
attribute_tags_list.append([['body'], 'vlink'])
attribute_tags_list.append([['embed', 'iframe', 'img', 'input', 'object'], 'vspace'])
attribute_tags_list.append([['col', 'hr', 'pre', 'table', 'td', 'th'], 'width'])

PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
page = input("enter your site (ex: https://www.digikala.com): ")

driver.get(page)
print("searching for ERROR [Attributes deprecated in HTML5 should not be used]:\n")
for attribute_tag in attribute_tags_list:
    check_attribute(attribute_tag[0], attribute_tag[1])
if not flag:
    print("NULL")
driver.close()
