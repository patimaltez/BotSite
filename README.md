# Automação de Cadastro em Site com Selenium e PyAutoGUI

Este projeto realiza a automação do processo de login e preenchimento de dados em um site utilizando as bibliotecas Selenium e PyAutoGUI em Python. Os dados a serem preenchidos são importados de um arquivo CSV.

## Pré-requisitos

Antes de executar o código, certifique-se de que você possui os seguintes itens instalados:

1. Python 3.x
2. Google Chrome
3. Chromedriver compatível com a versão do seu Google Chrome
4. As bibliotecas necessárias do Python (Selenium, PyAutoGUI e Pandas)

## Instalação

### 1. Instale o Python

Caso não tenha o Python instalado, você pode baixá-lo e instalá-lo a partir do site oficial: [Python.org](https://www.python.org/downloads/)

### 2. Instale o Google Chrome

Se o Google Chrome não estiver instalado, você pode baixá-lo e instalá-lo a partir do site oficial: [Google Chrome](https://www.google.com/chrome/)

### 3. Baixe o Chromedriver

Baixe a versão do Chromedriver compatível com a versão do seu Google Chrome a partir do site oficial: [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

### 4. Instale as Bibliotecas do Python

Para instalar as bibliotecas necessárias, execute os seguintes comandos no terminal:
    
    pip install selenium
    pip install pyautogui
    pip install pandas


## Configuração

### 1. Configurando o Chromedriver

Certifique-se de que o Chromedriver esteja localizado em um diretório que esteja no PATH do seu sistema, ou então especifique o caminho completo do Chromedriver no código, alterando a linha:

driver = webdriver.Chrome(options=chrome_options)
para:
driver = webdriver.Chrome(executable_path="caminho/para/o/chromedriver", options=chrome_options)

### 2. Configurando o Código

Atualize os IDs dos elementos HTML e as credenciais de login no código para que correspondam ao site em que você deseja automatizar o preenchimento.

campo_email = driver.find_element("id", "iddoelementonohtml")
campo_email.send_keys("seulogin")
campo_senha = driver.find_element("id", "password")
campo_senha.send_keys("sua senha")

### 3. Configurando o Arquivo CSV

Certifique-se de que o arquivo CSV (nomedoarquivo.csv) esteja no mesmo diretório do código ou especifique o caminho completo. Atualize os nomes das colunas no código para que correspondam aos nomes das colunas no seu arquivo CSV.

## Executando o Código

Após realizar todas as configurações, você pode executar o código usando o seguinte comando no terminal:

python nome_do_arquivo.py

O script abrirá o navegador Chrome, fará login no site especificado e começará a preencher os dados do arquivo CSV nos campos apropriados.

## Observações

- Certifique-se de que o site esteja acessível e os elementos HTML estejam visíveis no momento da execução.
- Dependendo do desempenho do seu sistema e da velocidade da internet, pode ser necessário ajustar os tempos de espera (time.sleep) no código.

## Licença

Este projeto é licenciado sob a GNU Affero General Public License v3.0.