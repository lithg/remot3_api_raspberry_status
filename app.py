import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from attachments import EmailAttOnline, EmailAttOffline
from Printer import Printer
from verifica import Verifica

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

def Main():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)  # seu path do driver

    print('*******************')
    print ("API INICIALIZADA")
    print('*******************\n\n')


        #############################################################################################
        ########################### INICIALIZACAO DO DRIVER  / LOGIN URL ############################
        #############################################################################################


    if options.headless == True:
        print('Rodando script, por favor aguarde....')
        time.sleep(3)
        print("Pode levar alguns segundos até que o script varra todos os dados.")

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
        print('Passou sem error de API')
        pass

    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'EVO_')))  # Esperar page carregar
        print ("Pagina carregada!")
        time.sleep(5)
        driver.find_element_by_id('jqgh_table_bulk_Status').click()  # o ultimo device
    except TimeoutException:
        print ("Pagina demorando mais que o normal para carregar...")
        time.sleep(5)
        driver.find_element_by_id('jqgh_table_bulk_Status').click()  # o ultimo device


    #############################################################################################
    ################################## VARRE TODOS OS DADOS #####################################
    #############################################################################################



    # VARRE TODOS OS DEVICES
    mcc = driver.find_elements_by_partial_link_text('EVO_')
    mcc_rows = len(mcc)
    #print(mcc_rows)

            ############# TESTE #############
    # stt = driver.find_elements_by_xpath('//i[@style="color:green"]')
    # print('stt 0 ' + stt[0].text)ß
    # print('stt 1 ' +  stt[1].text)



    stt = driver.find_elements_by_xpath("//*[contains(text(), 'Last Online')]")
    stt_len = len(stt)

    listaOff = []

    for i in range (stt_len):
        off = stt[i].text
        listaOff.append(off)


    print('***********\n\n')
    listaOff.pop(0)
    listaOff.pop(0)
    print(listaOff)
    print('***********\n\n')


    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Scroll pro final da página
    #driver.find_element_by_id('jqgh_table_bulk_Status').click()             # Clica em status e ordena

    for i in range(mcc_rows):
        print('Dispositivos monitorados: ' + mcc[i].text)



        #############################################################################################
        ################################## PRINT E ENVIO DO EMAIL ###################################
        #############################################################################################



    try:
        driver.get_screenshot_as_file('status.png')
        print('Foto gravada em: status.png\n')
        print('Preparando envio do email...\n\n')


    except:
        print('Print: FALHA\n\n')
    if not stt:
        EmailAttOnline()
        print('Email enviado!\n\n')

    else:
        EmailAttOffline()
        print('Email enviado!\n\n')

    time.sleep(2)
    driver.close()

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(Verifica, 'interval', minutes=10)
    scheduler.add_job(Main, 'interval', days=1)
    scheduler.add_job(Printer, 'interval', minutes=5)
    print('SCRIPT INICIADO')
    scheduler.start()
    Main()