import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import attachments
import telegram


def Verifica():
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
        print ("Pagina demorando mais que o normal para carregar...Tente novamente")
        driver.close()



    stt = driver.find_elements_by_xpath("//*[contains(text(), 'Last Online')]")
    stt_len = len(stt)

    listaOff = []
    listaTxt = []


    with open('status.txt', 'r') as f:
        listaTxt = [line.strip() for line in f]

    for i in range(stt_len):
        off = stt[i].text
        listaOff.append(off)

    print('***********\n\n')
    del listaOff[0]
    del listaOff[0]
    listaOff = [x.strip(' ') for x in listaOff]
    print(listaOff)

    len_off = len(listaTxt)
    len_list = len(listaOff)

    global valor

    if len_off > len_list:                     #lenoff  varreu
                                                # 3      3
                                                # 3      2   -- alguem voltou
                                                # 2      2   -- att txt


        valor = 'online'
        print('Algum MCC voltou!')
        attachments.EmailFicouOn()
        telegram.TeleMsgOn()


    elif len_off < len_list:
        valor = 'offline'
        print('Algum MCC saiu do ar.')
        attachments.EmailFicouOff()
        telegram.TeleMsgOff()

    else:
        print('Nada mudou.')



    print('***********\n\n')

    with open('status.txt', 'w') as f:
        for item in listaOff:
            f.write("%s\n" % item)




    print(listaTxt == listaOff)
    driver.close()

Verifica()

