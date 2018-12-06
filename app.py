import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from attachments import EmailAttOnline, EmailAttOffline

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path="geckodriver.exe")  # seu path do driver

print('*******************')
print ("API INICIALIZADA")
print('*******************\n\n')

if options.headless == True:
    print('Rodando script, por favor aguarde....')
    time.sleep(3)
    print("Pode levar alguns segundos até que o script varra todos os dados.")

username =  input("Digite seu username: ")
password = input("Digite sua senha: ")
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
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'MORADA')))  # Esperar page carregar
    print ("Pagina carregada!")
    driver.find_element_by_id('jqgh_table_bulk_Status').click()  # o ultimo device
    time.sleep(2)
except TimeoutException:
    print ("Pagina demorando mais que o normal para carregar...")

# VARRE TODOS OS DEVICES
mcc = driver.find_elements_by_partial_link_text('EVO_')
mcc_rows = len(mcc)
#print(mcc_rows)

        ############# TESTE #############
# stt = driver.find_elements_by_xpath('//i[@style="color:green"]')
# print('stt 0 ' + stt[0].text)ß
# print('stt 1 ' +  stt[1].text)


stt = driver.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div[3]/div[4]/div/table/tbody/tr[7]/td[4]/small')
stt_len = len(stt)

for i in range (stt_len):
    print(stt[i].text)


time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Scroll pro final da página
#driver.find_element_by_id('jqgh_table_bulk_Status').click()             # Clica em status e ordena

for i in range(mcc_rows):
    print('Dispositivos monitorados: ' + mcc[i].text)

try:
    driver.get_screenshot_as_file('status.png')
    print('Foto gravada em: status.png\n\n')

except:
    print('Print: FALHA\n\n')

if not stt:
    print('****************************')
    print('TODOS OS MCCs ESTÃO ONLINE!')
    print('****************************\n\n')
    EmailAttOnline()

else:
    print('Algum dispositivo esta OFFLINE! \n'
                   'Por favor, verificar.\n\n'
          'Enviando email, por favor aguarde...\n\n')
    EmailAttOffline()

time.sleep(2)
driver.close()

try:
    print('Email enviado!\n\n')
except:
    print('Email não enviado!\n\n')


