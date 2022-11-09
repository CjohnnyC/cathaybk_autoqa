from selenium.webdriver.common.by import By

class PageElement:

    def __init__(self, driver):
        self.driver=driver

    def search(self):
        return self.driver.find_element(By.XPATH,"//input[@class='gLFyf']")

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
        return self.driver.find_elements(By.XPATH, "//div[contains(text(),'(停發)')]")