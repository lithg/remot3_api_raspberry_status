import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


def Printer():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox()  # seu path do driver

    if options.headless == True:
        time.sleep(3)

    username =  'pedrosilva@vilatec.com.br'
    password = 'nbr5410!remot3'
    delay = 30       # delay para o wait until page load
    driver.get('https://app.remote.it/auth/#/sign-in') # URL ACESSADA PELO WEB DRIVER

    driver.find_element_by_id('sign-in-username').send_keys(username) #username
    driver.find_element_by_name('password').send_keys(password)       #senha
    driver.find_element_by_name('password').send_keys(Keys.ENTER)     #aperta enter
    time.sleep(4)

    try:
        driver.find_element_by_name('password').send_keys(Keys.ENTER)     #Se der erro de API, aperta ENTER e burla o erro
    except:
        pass

    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'EVO_')))  # Esperar page carregar
        driver.find_element_by_id('jqgh_table_bulk_Status').click()  # ordena por status
        time.sleep(3)
    except TimeoutException:
        time.sleep(10)
        driver.find_element_by_id('jqgh_table_bulk_Status').click()

    # VARRE TODOS OS DEVICES
    mcc = driver.find_elements_by_partial_link_text('EVO_')
    mcc_rows = len(mcc)
    #print(mcc_rows)

    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Scroll pro final da página
    #driver.find_element_by_id('jqgh_table_bulk_Status').click()             # Clica em status e ordena


    driver.get_screenshot_as_file('status.png')

    driver.close()

