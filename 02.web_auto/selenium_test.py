from selenium import webdriver

# 브라우저 꺼짐 방지 옵션
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# driver = webdriver.Chrome()
driver.get("https://www.naver.com")
# driver = webdriver.Chrome("C:/chromedriver.exe")
