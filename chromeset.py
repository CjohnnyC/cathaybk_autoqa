from selenium import webdriver
import os
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import ActionChains as AC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# import pyautogui
# import json
# from time import sleep, ctime

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation','enable-logging']) #不啟用自動化提示訊息
downloadpath=os.path.join(os.getcwd(), "download", "byChrome")
prefs={
    "profile.default_content_setting_values":{'notifications':2}, #不啟用開啟通知彈窗
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False, #不啟用儲存密碼彈窗
    "profile.default_content_settings.popups": 0, #下載檔案時不會出現下載視窗 #414
    "download.default_directory": downloadpath #從Chrome下載的檔案，預設存放位置
}
chrome_options.add_experimental_option('prefs', prefs)

#driver=webdriver.Chrome(options=chrome_options)
#driver.maximize_window()