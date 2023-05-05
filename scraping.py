from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options
import chromedriver_binary


#options.add_argument('--headless')
driver = webdriver.Chrome()
try:
    driver.get('https://www.google.co.jp/')
    
finally:
    driver.close()
    driver.quit()
