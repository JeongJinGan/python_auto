from selenium import webdriver

# 자동입력 문자 알림창 방지
import pyperclip
import pyautogui
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")
driver.maximize_window() # 화면 최대화

# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, "#id")
id.click()
pyperclip.copy("rksaudwls123")
pyautogui.hotkey("ctrl","v")
# id.send_keys("rksaudwls123")
time.sleep(3)

pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click()
pyperclip.copy("shjydp10601^^")
pyautogui.hotkey("ctrl","v")
# id.send_keys("shjydp10601^^")
time.sleep(3)

# 로그인 버튼
driver.find_element(By.CSS_SELECTOR, "#log\.login").click()
time.sleep(3)

# 브라우저 꺼짐 방지
input()