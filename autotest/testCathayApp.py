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
        self.getPage=is_exist(self.pe.login()) #other page elements AND logic should be True
        NTIME=datetime.now().strftime(TIME_FORMAT)
        screenshot(self.driver, "./screenshot/homepage", "homepage_"+NTIME+".png")
        assert self.getPage is True #Confirm homepage displayed

    def test2_credit_card_list(self):
        self.pe.menu().click()
        self.pe.prod_intro().click()
        self.pe.credit_card().click()
        NTIME=datetime.now().strftime(TIME_FORMAT)
        screenshot(self.driver, "./screenshot/cardlist", "top_"+NTIME+".png")
        ccl=self.pe.credit_card_list()
        self.driver.drag_and_drop(ccl[0], ccl[7])
        #scroll_el1_to_el2(self.actions, ccl[0], ccl[7]) #TochAction not work on H5 page
        NTIME=datetime.now().strftime(TIME_FORMAT)
        screenshot(self.driver, "./screenshot/cardlist", "bottom_"+NTIME+".png")
        assert len(ccl)==8 #Confirm credit card list has 8 subfunctions

    def test3_deadcard_type(self):
        ccl=self.pe.credit_card_list()
        self.driver.drag_and_drop(ccl[7], ccl[0])
        ccl[0].click() #click card intro
        self.driver.drag_and_drop(self.pe.rcmd_card(), self.pe.dead_card())
        self.pe.dead_card().click()
        screenshot_count=0
        dcg=self.pe.dead_card_group()
        for i in range(len(dcg)):
            sleep(3)
            NTIME=datetime.now().strftime(TIME_FORMAT)
            screenshot(self.driver, "./screenshot/cardgroup", str(i+1)+"_"+NTIME+".png")
            screenshot_count+=1
            if i<len(dcg)-1:
                self.driver.drag_and_drop(dcg[i], dcg[i+1])
            else:
                break
        assert screenshot_count==len(dcg) #Confirm screenshot num equal to dead card num

if __name__=="__main__":
    NTIME=datetime.now().strftime(TIME_FORMAT)
    html_report=file_path("./report", "result_"+NTIME+".html")
    pytest.main(["-s", "-v", ".", "--html="+html_report])
    #export html report
