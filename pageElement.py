from selenium.webdriver.common.by import By

class PageElement:

    def __init__(self, driver):
        self.driver=driver
    
    def menu(self):
        return self.driver.find_element(By.XPATH, "//a[@class='cubre-a-burger']")

    def prod_intro(self):
        return self.driver.find_element(By.XPATH, "//div[text()='產品介紹']")

    def credit_card(self):
        return self.driver.find_element(By.XPATH, "//div[@class='cubre-a-menuSortBtn'][text()='信用卡']")

    def credit_card_list(self):
        ccl=[
            "self.driver.find_element(By.XPATH, '//a[text()=\"卡片介紹\"]')",
            "self.driver.find_element(By.XPATH, '//a[text()=\"刷卡優惠\"]')",
            "self.driver.find_element(By.XPATH, '//a[text()=\"小樹點(信用卡)\"]')",
            "self.driver.find_element(By.XPATH, '//a[text()=\"卡友登錄專區\"]')",
            "self.driver.find_element(By.XPATH, '//a[text()=\"卡友理財服務\"]')",
            "self.driver.find_element(By.XPATH, '//a[text()=\"卡友權益\"]')",
            "self.driver.find_element(By.XPATH, '//a[text()=\"行動支付\"]')",
            "self.driver.find_element(By.XPATH, '//a[text()=\"申請信用卡\"]')"]
        return ccl

    def card_intro(self):
        return self.driver.find_element(By.XPATH, "//a[text()='卡片介紹']")

    def card_intro_list(self):
        cil=[
                "self.driver.find_element(By.XPATH, '//p[text()=\"推薦卡片\"]')",
                "self.driver.find_element(By.XPATH, '//p[text()=\"熱門卡片\"]')",
                "self.driver.find_element(By.XPATH, '//p[text()=\"百貨購物\"]')",
                "self.driver.find_element(By.XPATH, '//p[text()=\"海外交通\"]')",
                "self.driver.find_element(By.XPATH, '//p[text()=\"整併卡\"]')",
                "self.driver.find_element(By.XPATH, '//p[text()=\"停發卡\"]')"
        ]
        return cil

    def rcmd_card(self):
        return self.driver.find_element(By.XPATH, "//p[text()='推薦卡片']")
    
    def dptm_card(self):
        return self.driver.find_element(By.XPATH, "//p[text()='百貨購物']")

    def kaga_card(self):
        return self.driver.find_element(By.XPATH, "//p[text()='海外交通']")

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

    '''
    def dead_card_slider(self):
        dcs=self.driver.find_element(By.XPATH, '//span[@class="swiper-pagination-bullet"][35:42]')
    '''    

    #------------------------------------------------------------------------------------------------------------
    
    def dead_card_icon(self):
        return self.driver.find_element(By.XPATH, "//img[@id='img_96D650D3089045C7B9EB3A1FD77B0999']")

    def search(self):
        return self.driver.find_element(By.XPATH,"//input[@class='gLFyf']")

    def login(self):
        return self.driver.find_element(By.XPATH, "//input[@id='lblLoginText']")
    
    def ref(self):
        return self.driver.find_element(By.XPATH, "//img[@id='img_B6B4C04BCC184B36B8D0E3521FFB1B7B']")
    
    def h3_first(self):
        return self.driver.find_element(By.XPATH,'//div[0]')

    def h3_seventh(self):
        return self.driver.find_element(By.XPATH,'//div[100]')