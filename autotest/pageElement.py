from selenium.webdriver.common.by import By

class PageElement:

    def __init__(self, driver):
        self.driver=driver

    def login(self):
        return self.driver.find_element(By.XPATH, "//input[@id='lblLoginText']")
    
    def menu(self):
        return self.driver.find_element(By.XPATH, "//a[@class='cubre-a-burger']")

    def prod_intro(self):
        return self.driver.find_element(By.XPATH, "//div[text()='產品介紹']")

    def credit_card(self):
        return self.driver.find_element(By.XPATH, "//div[@class='cubre-a-menuSortBtn'][text()='信用卡']")

    def credit_card_list(self):
        all_list=self.driver.find_elements(By.XPATH, "//a[@class='cubre-a-menuLink']")
        return all_list[4:12] #4~11th is for credit card list

    def card_intro(self):
        return self.driver.find_element(By.XPATH, "//a[text()='卡片介紹']")

    def recmd_card(self):
        return self.driver.find_element(By.XPATH, "//p[text()='推薦卡片']")

    def dead_card(self):
        return self.driver.find_element(By.XPATH, "//p[text()='停發卡']")

    def dead_card_group(self):
        dcg=[]
        dcg.append(self.driver.find_element(By.XPATH, "//img[@id='img_8761B214795949419DC51176802BF6E1']"))
        dcg.append(self.driver.find_element(By.XPATH, "//img[@id='img_9B6112FD24B948C99668101C08F8B675']"))
        dcg.append(self.driver.find_element(By.XPATH, "//img[@id='img_92C805AD70BA4B5EAD22B41FDD858B1D']"))
        dcg.append(self.driver.find_element(By.XPATH, "//img[@id='img_CAD5544A547F429CA7414EFE3814F85E']"))
        dcg.append(self.driver.find_element(By.XPATH, "//img[@id='img_AA5E3E225F74485EBAC0F16AEC06C072']"))
        dcg.append(self.driver.find_element(By.XPATH, "//img[@id='img_3B4E85E2B5224CFCBE78AE5D9250481D']"))
        dcg.append(self.driver.find_element(By.XPATH, "//img[@id='img_76FB9CA0074844B8B2871BF9BDD09DFB']"))
        return dcg
