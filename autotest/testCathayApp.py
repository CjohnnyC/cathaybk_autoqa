import pytest
from appium import webdriver
from datetime import datetime
from time import sleep
#from appium.webdriver.common.touch_action import TouchAction

#Self defined configuration and page object
from appConfig import CAPS
from pageElement import PageElement

#Self defined functions
from selfFunctions import *

class TestCathayApp:

    @classmethod
    def setup_class(cls):
        cls.driver=webdriver.Remote("http://localhost:4723/wd/hub", CAPS)
        cls.driver.implicitly_wait(10) #We can also use WebDriverWait to each element, or set sleep.
        cls.pe=PageElement(cls.driver)
        #cls.actions=TouchAction(cls.driver)

    @classmethod
    def teardown_class(cls): 
        cls.driver.quit()

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test1_homepage(self):
        self.driver.get("https://www.cathaybk.com.tw/cathaybk/")
        flag=True 
        #implicity wait for page loading completed, then executing next script
        #After page loading completed, then it executes flag=True
        NTIME=datetime.now().strftime(TIME_FORMAT)
        screenshot(self.driver, "./screenshot/homepage", "homepage_"+NTIME+".png")
        assert flag==True #Confirm homepage displayed

    def test2_credit_card_list(self):
        self.pe.menu().click()
        self.pe.prod_intro().click()
        self.pe.credit_card().click()
        NTIME=datetime.now().strftime(TIME_FORMAT)
        screenshot(self.driver, "./screenshot/cardlist", "top_"+NTIME+".png")
        
        ccl=self.pe.credit_card_list()
        self.driver.execute_script("arguments[0].scrollIntoView(flase)", ccl[7])
        #self.driver.scroll(ccl[i+1], ccl[i]) to scroll until show ccl[7]
        #self.driver.drag_and_drop(ccl[i+1], ccl[i]) to scroll until show ccl[7]
        #scroll_el1_to_el2(self.actions, ccl[7], ccl[0]) #TochAction not work on H5 page
        NTIME=datetime.now().strftime(TIME_FORMAT)
        screenshot(self.driver, "./screenshot/cardlist", "bottom_"+NTIME+".png")

        self.driver.execute_script("arguments[0].scrollIntoView(true)", ccl[0])
        # Pull back to ccl[0] (card_intro) for test3
        
        assert len(ccl)==8 #Confirm credit card list has 8 subfunctions

    def test3_deadcard_type(self):
        self.pe.card_intro().click()
        self.driver.scroll(self.pe.dptm_card(), self.pe.rcmd_card())
        #default right border (dptm_card) position to scroll to left border until show dead_card
        self.pe.dead_card().click()

        screenshot_count=0
        dcg=self.pe.dead_card_group()
        card_x=dcg[0].location['x'] #first card x-coordinate
        card_y=dcg[0].location['y'] #first card y-coordinate, and y will be fixed
        card_width=dcg[0].size['width'] #first card width
        for i in range(len(dcg)):
            sleep(3)
            NTIME=datetime.now().strftime(TIME_FORMAT)
            screenshot(self.driver, "./screenshot/cardgroup", str(i+1)+"_"+NTIME+".png")
            screenshot_count+=1
            
            if i<len(dcg)-1:
                swipe_card(self.driver, card_x, card_width, card_y)
                #self.driver.scroll(dcg[i+1], dcg[i]) 
                #concept is the same, but not sure the element out of screen
                dcg[i+1] #To check next card displayed (by inplicity wait)
            else:
                break
        
        assert screenshot_count==len(dcg) #Confirm screenshot num equal to dead card num

if __name__=="__main__":
    NTIME=datetime.now().strftime(TIME_FORMAT)
    html_report=file_path("./report", "result_"+NTIME+".html")
    pytest.main(["-s", "-v", ".", "--html="+html_report])
    #export html report
