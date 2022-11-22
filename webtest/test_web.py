import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
from datetime import datetime
from time import sleep

from pageElement import PageElement
from chromeset import chrome_options
from selfFunctions import *
from logConfig import *

class TestCathayApp:

    @classmethod
    def setup_class(cls):
        cls.driver=webdriver.Chrome(options=chrome_options)
        cls.size=cls.driver.get_window_size()
        cls.driver.set_window_size(cls.size["width"]/3, cls.size["height"])
        #Implicity wait for page and all elements. We can also use WebDriverWait to each element, or set sleep.
        cls.driver.implicitly_wait(10) 
        cls.pe=PageElement(cls.driver)
        cls.actions=ActionChains(cls.driver)
        cls.ccl=cls.pe.credit_card_list()
        cls.cil=cls.pe.card_intro_list()
        #stored by string, when executing to the element by coding eval(element)

    @classmethod
    def teardown_class(cls): 
        cls.driver.quit()

    def test1(self):
        self.driver.get("https://www.cathaybk.com.tw/cathaybk/")
        flag=True
        NTIME=datetime.now().strftime(TIME_FORMAT)
        screenshot(self.driver, "./screenshot/1_homepage", "homepage_"+NTIME+".png")
        assert flag==True

    def test2(self):
        self.pe.menu().click()
        self.pe.prod_intro().click()
        self.pe.credit_card().click()
        sleep(3)
        NTIME=datetime.now().strftime(TIME_FORMAT)
        screenshot(self.driver, "./screenshot/2_cardlist", "atop_"+NTIME+".png")
        
        #As vscroll function we difined, but eval can not work in function, need to script as below
        ccl_count=0
        while True:
            try:
                #self.driver.execute_script("arguments[0].scrollIntoView(true);", eval(self.ccl[count]))
                #self.actions.drag_and_drop(eval(self.ccl[count+1]), eval(self.ccl[count])).perform() worst efficiency
                self.actions.move_to_element(eval(self.ccl[ccl_count])).perform()
                ccl_count+=1
            except:
                logging.info("credit card list subfunction count = "+str(ccl_count))
                break
        
        NTIME=datetime.now().strftime(TIME_FORMAT)
        screenshot(self.driver, "./screenshot/2_cardlist", "bottom_"+NTIME+".png")

        #loop count should be the same as ccl count
        assert ccl_count==len(self.ccl)
        
    #@pytest.mark.skip("skip")
    def test3(self):
        self.actions.move_to_element(eval(self.ccl[0])).click().perform()
        
        #actions.move_to_element(pe.dead_card()).perform() can not execute
        #another way is to build for loop to drag each one to previous one
        #self.actions.drag_and_drop(self.pe.dptm_card(), self.pe.rcmd_card()).perform()
        '''
        self.driver.execute_script(
            'arguments[0].scrollIntoView({behavior:"auto", inline:"center"});', 
            self.pe.dead_card())
        '''
        cil_count=0
        while True:
            try:
                self.actions.drag_and_drop(eval(self.cil[cil_count+1]), eval(self.cil[cil_count])).perform()
                cil_count+=1
            except:
                #number of drag_and_drop is interval, need +1 to be the actual count
                cil_count+=1 
                logging.info("card intro list count = "+str(cil_count))
                break

        self.pe.dead_card().click()

        #In web it allows to save element first in list for DOM will find all element first
        #Android can NOT do like this, need eval(elements[i])
        dcg=self.pe.dead_card_group()
        screenshot_count=0
        for i in range(len(dcg)):
            sleep(1)
            NTIME=datetime.now().strftime(TIME_FORMAT)
            screenshot(self.driver, "./screenshot/3_deadcard", str(i+1)+"_"+NTIME+".png")
            screenshot_count+=1
            try:
                #self.actions.move_to_element(dcg[i+1]).perform() will not align to center
                self.driver.execute_script(
                    'arguments[0].scrollIntoView({behavior:"auto", block:"center", inline:"center"});', 
                    dcg[i+1])
            except:
                logging.info("dead card screenshot count = "+str(screenshot_count))
                break

        assert screenshot_count==len(dcg)

if __name__=="__main__":
    NTIME=datetime.now().strftime(TIME_FORMAT)
    html_report=file_path("./report", "result_"+NTIME+".html")
    pytest.main(["-v", ".", "--html="+html_report])
    #export html report


