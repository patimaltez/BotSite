# importar as bibliotecas a serem usadas
import pyautogui
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# abrir o navegador chrome maximizado
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)
pyautogui.PAUSE = 0.3
driver.get("https://seusite.com/")
time.sleep(5)

# faça login no site, use o id dos elementos no HTML inspecionando o site
campo_email = driver.find_element("id", "iddoelementonohtml")
campo_email.click()
campo_email.send_keys("seulogin")
campo_senha = driver.find_element("id", "password")
campo_senha.click()
campo_senha.send_keys("sua senha")
campo_senha.submit()
time.sleep(5)

# Importar a base de dados a serem preenchidos usando arquivo csv
import pandas as pd
tabela = pd.read_csv("nomedoarquivo.csv")
print(tabela)

# Um exemplo de cadastramento ficticio para mostrar funções úteis ao cadastramento
for linha in tabela.index:
    # clicar no primeiro campo a ser preenchido
    campo_codigo = driver.find_element("id", "iddoelementonohtml")
    campo_codigo.click()
    # pegar da tabela o valor do campo que a gente quer preencher no site
    codigo = tabela.loc[linha, "nomedacoluna"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "nomedacoluna"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "nomedacoluna"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "nomedacoluna"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "nomedacoluna"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "nomedacoluna"]))
    pyautogui.press("tab")
    # lidando com uma coluna de observações que pode ter células vazias
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    # após preencher diversos campos, verificar como o site salva os dados, no exemplo, click no enter salva
    pyautogui.press("enter")
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Repetir o processo de cadastro até o fim da tabela

sys.exit()