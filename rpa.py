from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from PySimpleGUI import PySimpleGUI as sg
import pyautogui

#criando navegador
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())

nav = webdriver.Chrome(service=service, options=options)

#entrando no prime

sg.theme('Reddit')
layout = [
    [sg.Text('Usuario Prime'), sg.Input(key='usuario')],
    [sg.Text('Senha Prime'), sg.Input(key='senha_prime', password_char='*')],
    [sg.Text('Email'), sg.Input(key='email')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Button('Entrar')]
]

janela = sg.Window('Tela de Login', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    elif eventos == 'Entrar':
        janela.close()
        nav.get('https://596057.mannesoftprime.com.br/mannesoft/login.php')

        nav.find_element('xpath',
                        '//*[@id="USUARIO"]').send_keys(valores['usuario'])

        nav.find_element('xpath',
                        '/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/form/table/tbody/tr[4]/td[2]/input').send_keys(valores['senha_prime'])

        nav.find_element('xpath',
                        '//*[@id="edicao"]/table/tbody/tr[5]/td[2]/table/tbody/tr[1]/td[2]/img').click()

        nav.execute_script("window.open('https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=ASKXGp39raIgsOjfrBdzsCVKymIYqifIPB0scbaOya-Sn5QlhZznDQWA4UJ1ehPCNzATzIXyU6H1Ug&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-2062608840%3A1700595883599523&theme=glif')")

        pyautogui.write(valores['email'])
                            
        nav.find_element('xpath', 
                        '//*[@id="identifierNext"]/div/button/span').click()

        nav.find_element('xpath', 
                        '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(valores['senha'])
        
        nav.find_element('xpath', 
                        '//*[@id="passwordNext"]/div/button/span').click()

        while email == "sim":
            try:
                img = pyautogui.locateCenterOnScreen('email_token.PNG', confidence=0.7)
                pyautogui.click(img.x, img.y)
                time.sleep(2)
                email = "não"
            except:
                print('não encontrei')

        # login = [valores['usuario'], valores['senha']]

        # with open('login.txt', 'w') as arquivo:
        #     for valor in login:
        #         arquivo.write(str(valor) + '\n')

        #Aprovação de candidatos

        def aprovacao_aluno():
            nav.execute_script("window.open('https://596057.mannesoftprime.com.br/mannesoft/sistema.php?ACAO=publico/vestibulando.selecao.php&mnsSetRef=1')")
            nav.execute_script("window.open('https://596057.mannesoftprime.com.br/mannesoft/sistema.php?ACAO=publico/dcto.lista.php&dcto=62')")

        #Matrícula de alunos

        def matricula():
            nav.execute_script("window.open('https://596057.mannesoftprime.com.br/mannesoft/sistema.php?ACAO=publico/aluno.selecao.php&mnsSetRef=1')")
            nav.execute_script("window.open('https://drive.google.com/file/d/1sxF95U0aEned5wYToZTyeu2NZiPfQKLI/view')")

        #cadastros

        def cadastro_curso():
            nav.execute_script("window.open('https://596057.mannesoftprime.com.br/mannesoft/sistema.php?ACAO=publico/curso.selecao.php&mnsSetRef=1')")
            nav.execute_script("window.open('https://596057.mannesoftprime.com.br/mannesoft/sistema.php?ACAO=publico/dcto.lista.php&dcto=53')")

        def cadastro_disciplina():
            nav.execute_script("window.open('https://596057.mannesoftprime.com.br/mannesoft/sistema.php?ACAO=publico/disc.selecao.php&mnsSetRef=1')")
            nav.execute_script("window.open('https://596057.mannesoftprime.com.br/mannesoft/sistema.php?ACAO=publico/dcto.lista.php&dcto=54')")

        #Processo seletivo
        def processo_seletivo():
            nav.execute_script("window.open('https://596057.mannesoftprime.com.br/mannesoft/sistema.php?ACAO=4&TRANSID=transaction1078119092655cec83dc127')")
            nav.execute_script("window.open('https://596057.mannesoftprime.com.br/mannesoft/sistema.php?ACAO=publico/dcto.lista.php&dcto=41')")

        #menu de opções de telas

        sg.theme('Reddit')
        layout = [
            [sg.Button('Aprovação de Alunos')],
            [sg.Button('Matrícula')],
            [sg.Button('Cadastro Curso')],
            [sg.Button('Cadastro Disciplina')],
            [sg.Button('Processo Seletivo')],
            [sg.Button('Sair')]
        ]

        janela = sg.Window('Menu de Telas', layout)

        while True:
            eventos, valores = janela.read()
            if eventos == sg.WIN_CLOSED or eventos == 'Sair':
                break
            elif eventos == 'Aprovação de Alunos':
                aprovacao_aluno()
            elif eventos == 'Matrícula':
                matricula()
            elif eventos == 'Cadastro Curso':
                cadastro_curso()
            elif eventos == 'Cadastro Disciplina':
                cadastro_disciplina()
            elif eventos == 'Processo Seletivo':
                processo_seletivo()