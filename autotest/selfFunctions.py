from pathlib import Path

TIME_FORMAT="%Y%m%d_%H%M%S"
'''
#NTIME=datetime.now().strftime("%Y%m%d_%H%M%S") 
#Above NTIME need to call each time, can not package it or the time will be the same
'''

def file_path(dir, file):
    Path(dir).mkdir(parents=True, exist_ok=True) 
    wholepath=Path(dir)/Path(file)
    return str(wholepath)

def screenshot(driver, dir, file):
    driver.get_screenshot_as_file(file_path(dir, file))

'''
def is_exist(page_element):
    flag=True
    try:
        page_element
        return flag
    except:
        flag=False
        return flag
'''

'''
def vertical_scroll_each(driver, elements_list):
    count=0
    while True:
        try:
            driver.execute_script("arguments[0].scrollIntoView(true)", eval(elements_list[count]))
            count+=1
        except:
            break
    return count

def horizontal_scroll_each(driver, elements_list):
    count=0
    while True:
        try:
            driver.sroll(eval(elements_list[count+1]), eval(elements_list[count]))
            count+=1
        except:
            break
    return count
'''

'''
def scroll_el1_to_el2(actions, el1, el2):
    actions.press(el1).move_to(el2).release().perform()

def get_size(driver):
    x=driver.get_window_size()["width"]
    y=driver.get_window_size()['height']
    return (x,y)

def swipe_up_down(driver,x_ratio,sy_ratio,ey_ratio,t):
    s=get_size(driver)
    x=int(s[0]*x_ratio)
    sy=int(s[1]*sy_ratio)
    ey=int(s[1]*ey_ratio)
    driver.swipe(x,sy,x,ey,t)

def swipe_left_right(driver,sx_ratio,ex_ratio,y_ratio,t):
    s=get_size(driver)
    sx=int(s[0]*sx_ratio)
    ex=int(s[0]*ex_ratio)
    y=int(s[1]*y_ratio)
    driver.swipe(sx,y,ex,y,t)
'''
