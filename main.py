from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import WebDriverWait
import os
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

#protect email and password
load_dotenv()

driver = webdriver.Chrome()
driver.get("https://tropamilionariatips.com/dashboard/login")


tab_email = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/input')
tab_email.send_keys(os.getenv("EMAIL"))

tab_senha = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[2]/div/input')
tab_senha.send_keys(os.getenv("SENHA"))

#trick to bypass "I'm not a robot" captcha...
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='reCAPTCHA']")))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))).click()
time.sleep(5)

botao_login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[4]')
botao_login.click()



