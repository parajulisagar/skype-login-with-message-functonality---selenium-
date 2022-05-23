
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--disable-notifications")
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

path="C:\\Users\\intern13\\Desktop\\driver\\chromedriver.exe"
driver = webdriver.Chrome(path, chrome_options=options)

driver.get("https://web.skype.com/")
driver.maximize_window()
email=driver.find_element_by_name("loginfmt")
email.send_keys("example@gmail.com")
time.sleep(4)
next=driver.find_element_by_id("idSIButton9").click()
wait = WebDriverWait(driver, 10)
password=driver.find_element_by_name("passwd")
password.send_keys("examplepassword")
time.sleep(4)
next=driver.find_element_by_id("idSIButton9").click()
time.sleep(4)
next=driver.find_element_by_id("idSIButton9").click()
time.sleep(10)
next=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div[2]/button/div").click()
next=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/input").send_keys("Bivek Khatiwada")
time.sleep(20)
next=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div[1]").click()

for i in range(10):
    next=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div").send_keys("k xa sir khabar")
    time.sleep(4)
    next=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/button/div").click()
    time.sleep(2)











