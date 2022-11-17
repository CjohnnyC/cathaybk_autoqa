import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from pathlib import Path
from time import sleep

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
        cls.actions=TouchAction(cls.driver)

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
        screenshot(self.driver)
        assert self.getPage is True #Confirm homepage displayed

    def test2_credit_card_list(self):
        self.pe.menu().click()
        self.pe.prod_intro().click()
        self.pe.credit_card().click()
        ccl=self.pe.credit_card_list()
        scroll_el1_to_el2(self.actions, ccl[0], ccl[7]) #scroll from card intro to apply credit card
        screenshot(self.driver)
        assert len(ccl)==8 #Confirm credit card list has 8 subfunctions

    def test3_deadcard_type(self):
        ccl=self.pe.credit_card_list()
        scroll_el1_to_el2(self.actions, ccl[7], ccl[0]) #scroll from apply credit card back to card intro
        ccl[0].click() #click card intro
        scroll_el1_to_el2(self.actions, self.pe.recmd_card(), self.pe.dead_card())
        self.pe.dead_card().click()
        screenshot_count=0
        dcg=self.pe.dead_card_group()
        for i in range(len(dcg)):
            sleep(3)
            screenshot(self.driver)
            screenshot_count+=1
            if i<len(dcg)-1:
                scroll_el1_to_el2(self.actions, dcg[i], dcg[i+1]) #TouchAction scroll to next card
            else:
                break
        assert screenshot_count==len(dcg) #Confirm screenshot num equal to dead card num

if __name__=="__main__":
    html_report=str(Path.cwd()/Path("report/result_"+NTIME+".html"))
    pytest.main(["-s", "-v", ".", "--html="+html_report])
    #export html report
