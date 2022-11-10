from appium.webdriver.common.touch_action import TouchAction
from datetime import datetime

NTIME=datetime.now().strftime("%Y%m%d_%H%M%S")

def is_exist(page_element):
    flag=True
    try:
        page_element
        return flag
    except:
        flag=False
        return flag

def screenshot(driver):
    driver.get_screenshot_as_file("./screenshot/homepage_"+NTIME+".png")

def scroll_el1_to_el2(driver, el1, el2):
    TouchAction(driver).press(el1).move_to(el2).release().perform()

'''
def get_size(driver):
    x=driver.get_window_size()["width"]
    y=driver.get_window_size()['height']
    return (x,y)

def swipe_up_down(driver,x,y1,y2,t):
    s=get_size(driver)
    x=int(s[0]*x)
    y1=int(s[1]*y1)
    y2=int(s[1]*y2)
    driver.swipe(x,y1,x,y2,t)

def swipe_left_right(driver,x1,x2,y,t):
    s=get_size(driver)
    x1=int(s[0]*x1)
    x2=int(s[0]*x2)
    y=int(s[1]*y)
    driver.swipe(x1,y,x2,y,t)
'''
