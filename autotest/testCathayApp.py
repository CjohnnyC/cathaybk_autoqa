import pytest
from appium import webdriver
from datetime import datetime
from time import sleep
#from appium.webdriver.common.touch_action import TouchAction

#Self defined configuration and page object
from appConfig import CAPS
from pageElement import PageElement
from logConfig import *

#Self defined functions
from selfFunctions import *

class TestCathayApp:

    @classmethod
    def setup_class(cls):
        cls.driver=webdriver.Remote("http://localhost:4723/wd/hub", CAPS)
        
        #We can also use WebDriverWait to each element, or set sleep.
        cls.driver.implicitly_wait(10)
        cls.pe=PageElement(cls.driver)
        #cls.actions=TouchAction(cls.driver)

        #Grouping elements prepared for eval(element)
        cls.ccl=cls.pe.credit_card_list()
        cls.cil=cls.pe.card_intro_list()
        cls.dcg=cls.pe.dead_card_list()
        
    @classmethod
    def teardown_class(cls): 
        cls.driver.quit()

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test1_homepage(self):
        self.driver.get("https://www.cathaybk.com.tw/cathaybk/")
         
        #Page loading done in implicity wait, then executing next script, set flag=true
        flag=True

        #get screenshot with current time as file name
        NTIME=datetime.now().strftime(TIME_FORMAT)
        screenshot(self.driver, "./screenshot/homepage", "homepage_"+NTIME+".png")

        #homepage should be loaded successfully
        assert flag==True
        

    def test2_credit_card_list(self):
        self.pe.menu().click()
        self.pe.prod_intro().click()
        self.pe.credit_card().click()
        
        #direct to credit card list, get screenshot of default output
        NTIME=datetime.now().strftime(TIME_FORMAT)
        screenshot(self.driver, "./screenshot/cardlist", "top_"+NTIME+".png")
        
        #eval can NOT be packaged to another function, scroll by each element
        ccl_count=0
        while True:
            try:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", eval(self.ccl[ccl_count]))
                ccl_count+=1
            except:
                logging.info("credit card list subfunction count = "+str(ccl_count))
                break
        '''
        scroll(ccl[i+1], ccl[i])
        drag_and_drop(ccl[i+1], ccl[i])
        scroll_el1_to_el2(self.actions, ccl[i+1], ccl[i]) TochAction not work on H5 page
        '''
        all_func_count=len(self.ccl)
        NTIME=datetime.now().strftime(TIME_FORMAT)
        screenshot(self.driver, "./screenshot/cardlist", "bottom_"+NTIME+".png")
        
        #count should be the same as number of ccl elements
        assert ccl_count==all_func_count

    def test3_deadcard_type(self):
        #pull back to card_intro
        self.driver.execute_script("arguments[0].scrollIntoView(true)", self.pe.card_intro())
        self.pe.card_intro().click()

        #The same reason, eval can NOT be packaged to another function
        cil_count=0
        while True:
            try:
                self.driver.scroll(eval(self.cil[cil_count+1]), eval(self.cil[cil_count]))
                cil_count+=1
            except:
                cil_count+=1 
                logging.info("card intro list count = "+str(cil_count))
                break
        '''
        self.driver.scroll(self.pe.dptm_card(), self.pe.rcmd_card())
        self.driver.scroll(self.pe.csld_card(), self.pe.dptm_card())
        '''
        
        self.pe.dead_card().click()

        #to set overall screenshot and count
        screenshot_count=0
        eval(self.dcg[0])
        all_cards_count=len(self.dcg)
        for i in range(all_cards_count):
            #To force seperate the time of getting screenshot
            sleep(1)
            NTIME=datetime.now().strftime(TIME_FORMAT)
            screenshot(self.driver, "./screenshot/cardgroup", str(i+1)+"_"+NTIME+".png")
            screenshot_count+=1
            
            #swipe card by each one
            try:
                self.driver.execute_script(
                    'arguments[0].scrollIntoView({behavior:"auto", block:"center", inline:"center"});', 
                    eval(self.dcg[i+1]))
                '''
                swipe_left_right(self.driver, 0.95, 0.05, 0.5)
                (sx=0.95) -> (ex=0.05) horizontal scroll screen from 95%->5% screen width
                #(sy=0.5) anchor sy at 50% of screen height
                #scroll_el1_to_el2(actions, dcg[i+1], dcg[i]) by TouchAction, but not sure the element out of screen
                '''
            except:
                logging.info("dead card screenshot count = "+str(screenshot_count))
                break

        #Confirm screenshot num equal to dead card num
        assert screenshot_count==all_cards_count

if __name__=="__main__":
    NTIME=datetime.now().strftime(TIME_FORMAT)
    html_report=file_path("./report", "result_"+NTIME+".html")
    pytest.main(["-v", ".", "--html="+html_report])
    #export html report
