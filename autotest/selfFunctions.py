from pathlib import Path

#NTIME=datetime.now().strftime("%Y%m%d_%H%M%S") 
#Above NTIME need to call each time, can not package it or the time will be the same
TIME_FORMAT="%Y%m%d_%H%M%S"

def is_exist(page_element):
    flag=True
    try:
        page_element
        return flag
    except:
        flag=False
        return flag

def file_path(dir, file):
    Path(dir).mkdir(parents=True, exist_ok=True) 
    wholepath=Path(dir)/Path(file)
    return str(wholepath)

def screenshot(driver, dir, file):
    driver.get_screenshot_as_file(file_path(dir, file))

def swipe_card(driver, card_x, card_width, card_y):
    scroll_x=card_x+card_width
    driver.swipe(scroll_x, card_y, 0, card_y)


'''
def scroll_el1_to_el2(actions, el1, el2):
    actions.press(el1).move_to(el2).release().perform()
'''

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
