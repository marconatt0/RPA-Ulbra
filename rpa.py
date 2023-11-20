#criando navegador

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())

nav = webdriver.Chrome(service=service, options=options)

#input para usuario

usuario = input('Coloque seu usuário: ')
senha = input('Coloque sua senha: ')

#entrando no prime

nav.get('https://596057.mannesoftprime.com.br/mannesoft/login.php')

nav.find_element('xpath',
                 '//*[@id="USUARIO"]').send_keys(usuario)

nav.find_element('xpath',
                 '/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/form/table/tbody/tr[4]/td[2]/input').send_keys(senha)

nav.find_element('xpath',
                 '//*[@id="edicao"]/table/tbody/tr[5]/td[2]/table/tbody/tr[1]/td[2]/img').click()

#aprovação de candidatos

def aprovacao_aluno():
    nav.find_element('xpath', '/html/body/div[2]/div/ul/li[2]/ul/li[10]/ul/li[4]/a').click()

#menu de opções de telas

op = 0

while op != 5:
    print('''
          Qual tela deseja ir?

          1. Aprovação de alunos
          2. ...
          3. ...
          4. ...
          5. Sair
          ''')
    op = int(input('Qual opção? '))
    if op == 1:
       aprovacao_aluno()
    if op == 5:
        print('Saindo...')
        break
    else:
        print('opção inválida')

