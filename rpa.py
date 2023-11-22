from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from PySimpleGUI import PySimpleGUI as sg
import pyautogui
import time

#criando navegador
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())

nav = webdriver.Chrome(service=service, options=options)

#entrando no prime

sg.theme('Reddit')
layout = [
    [sg.Text('Usuario Prime'), sg.InputText(default_text=sg.user_settings_get_entry('-usuario-'))],
    [sg.Text('Senha Prime'), sg.InputText(default_text=sg.user_settings_get_entry('senha_prime'), password_char='*')],
    [sg.Button('Entrar')]
]

janela = sg.Window('Tela de Login', layout)

while True:
    eventos, valores = janela.read()
        
        
    print('Login salvo', valores[0], valores[1])
    sg.user_settings_set_entry('-usuario-', valores[0])
    sg.user_settings_set_entry('senha_prime', valores[0])
    break

while True:
    eventos, valores = janela.read()

    if eventos == sg.WIN_CLOSED:
        break
    elif eventos == 'Entrar':
        janela.close()
        
        nav.get('https://596057.mannesoftprime.com.br/mannesoft/login.php')

        nav.find_element('xpath',
                        '//*[@id="USUARIO"]').send_keys(valores[0])

        nav.find_element('xpath',
                        '/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/form/table/tbody/tr[4]/td[2]/input').send_keys(valores[1])

        nav.find_element('xpath',
                        '//*[@id="edicao"]/table/tbody/tr[5]/td[2]/table/tbody/tr[1]/td[2]/img').click()

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
            [sg.Button('Aprovação de Alunos'), sg.Button('...')],
            [sg.Button('Matrícula'), sg.Button('...')],
            [sg.Button('Cadastro Curso'), sg.Button('...')],
            [sg.Button('Cadastro Disciplina'), sg.Button('...')],
            [sg.Button('Processo Seletivo'), sg.Button('...')],
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