import pytest
from appium import webdriver
from pathlib import Path
from time import sleep

#Slef defined configuration and page object
from appConfig import CAPS
from pageElement import PageElement

#Self defined functions
from selfFunctions import NTIME, screenshot, is_exist

class TestCathayApp:

    #Fixture start
    @classmethod
    def setup_class(cls):
        cls.driver=webdriver.Remote("http://localhost:4723/wd/hub", CAPS)
        cls.driver.implicitly_wait(10)
        cls.pe=PageElement(cls.driver)
        #We also can use WebDriverWait to each element, or set sleep.

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
        self.driver.scroll(self.pe.credit_card_list[0], self.pe.credit_card_list[7])
        screenshot(self.driver)
        count=len(self.pe.credit_card_list)
        assert count==8 #Confirm credit card list has 8 subfunctions

    def test3_deadcard_type(self):
        self.driver.scroll(self.pe.credit_card_list[7], self.pe.credit_card_list[0])
        self.pe.card_intro().click()
        self.driver.scroll(self.pe.recmd_card(), self.pe.dead_card())
        self.pe.dead_card().click()
        screenshot_count=0
        for d in self.pe.dead_card_group:
            sleep(3)
            screenshot(self.driver)
            screenshot_count+=1
            self.driver.scroll(d, d+1)
        assert screenshot_count==len(self.pe.dead_card_group) #Confirm screenshot num equal to dead card num

if __name__=="__main__":
    html_report=str(Path.cwd()/Path("report/result_"+NTIME+".html"))
    pytest.main(["-s", "-v", ".", "--html="+html_report])