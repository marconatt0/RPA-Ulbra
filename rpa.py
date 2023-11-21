from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from PySimpleGUI import PySimpleGUI as sg

#criando navegador
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())

nav = webdriver.Chrome(service=service, options=options)

#entrando no prime

sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'), sg.Input(key='usuario')],
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
                        '/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/form/table/tbody/tr[4]/td[2]/input').send_keys(valores['senha'])

        nav.find_element('xpath',
                        '//*[@id="edicao"]/table/tbody/tr[5]/td[2]/table/tbody/tr[1]/td[2]/img').click()

        #Página Inicial

        def pagina_inicial():
            nav.get('https://596057.mannesoftprime.com.br/mannesoft/sistema.php?ACAO=publico/caixa_de_trabalho.php&mnsSetRef=1')

        #Aprovação de candidatos

        def aprovacao_aluno():
            nav.execute_script("window.open('https://596057.mannesoftprime.com.br/mannesoft/sistema.php?ACAO=publico/vestibulando.selecao.php&mnsSetRef=1')")
            nav.execute_script("window.open('https://596057.mannesoftprime.com.br/mannesoft/sistema.php?ACAO=publico/dcto.lista.php&dcto=62')")

        #menu de opções de telas

        sg.theme('Reddit')
        layout = [
            [sg.Button('Aprovação de alunos')],
            [sg.Button('...')],
            [sg.Button('...')],
            [sg.Button('...')],
            [sg.Button('...')],
            [sg.Button('Sair')]
        ]

        janela = sg.Window('Menu de Telas', layout)

        while True:
            eventos, valores = janela.read()
            if eventos == sg.WIN_CLOSED or eventos == 'Sair':
                break
            elif eventos == 'Aprovação de alunos':
                aprovacao_aluno()
            