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

# https://www.pysimplegui.org/en/latest/#user-settings-api

layout=[[sg.Text('login')]]
layout+=[[sg.Text(i+1),sg.Input(key=('infos',i))] for i in range(2)]
layout+=[[sg.Button('Entrar'),sg.Button('Salvar Login')]]

janela=sg.Window('Login',layout,finalize=True)
sg.user_settings_filename(path='.')
Login=sg.user_settings_get_entry('login')
if Login != None:
    for i in range(2):
        janela[('infos',i)].update(Login[i])
while True:
    events,values= janela.read()
    print (values)
    if events == 'Entrar':
        Login=[values[('infos',i)] for i in range(2)]
        print(Login)
        pass

        #janela.close()

        nav.get('https://596057.mannesoftprime.com.br/mannesoft/login.php')

        nav.find_element('xpath',
                        '//*[@id="USUARIO"]').send_keys(values[('infos',0)])

        nav.find_element('xpath',
                        '/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/form/table/tbody/tr[4]/td[2]/input').send_keys(values[('infos',1)])

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

        def documentos_oficiais():
            nav.execute_script("window.open('https://596057.mannesoftprime.com.br/mannesoft/sistema.php?ACAO=publico/modelo_documento.selecao.php&mnsSetRef=1')")
            nav.execute_script("window.open('https://596057.mannesoftprime.com.br/mannesoft/sistema.php?ACAO=publico/dcto.lista.php&dcto=51')")

        def relatorio_demanda():
            nav.execute_script("window.open('')")
            nav.execute_script("window.open('https://596057.mannesoftprime.com.br/mannesoft/sistema.php?ACAO=publico/dcto.lista.php&dcto=39')")

        def precificacao():
            nav.execute_script("window.open('https://596057.mannesoftprime.com.br/mannesoft/sistema.php?ACAO=publico/gc.selecao.php&mnsSetRef=1')")
            nav.execute_script("window.open('https://596057.mannesoftprime.com.br/mannesoft/sistema.php?ACAO=publico/dcto.lista.php&dcto=1')")

        def condicoes_pagamento():
            nav.execute_script("window.open('')")
            nav.execute_script("window.open('https://596057.mannesoftprime.com.br/mannesoft/sistema.php?ACAO=publico/dcto.lista.php&dcto=5')")
        
        def contas_correntes():
            nav.execute_script("window.open('')")
            nav.execute_script("window.open('https://596057.mannesoftprime.com.br/mannesoft/sistema.php?ACAO=publico/dcto.lista.php&dcto=12')")
        
        def descontos():
            nav.execute_script("window.open('')")
            nav.execute_script("window.open('https://596057.mannesoftprime.com.br/mannesoft/sistema.php?ACAO=publico/dcto.lista.php&dcto=13')")

        def acordo():
            nav.execute_script("window.open('')")
            nav.execute_script("window.open('https://596057.mannesoftprime.com.br/mannesoft/sistema.php?ACAO=publico/dcto.lista.php&dcto=21')")
        
        def contas_correntes2():
            nav.execute_script("window.open('')")
            nav.execute_script("window.open('https://596057.mannesoftprime.com.br/mannesoft/sistema.php?ACAO=publico/dcto.lista.php&dcto=29')")

        def webpolo():
            nav.execute_script("window.open('')")
            nav.execute_script("window.open('https://596057.mannesoftprime.com.br/mannesoft/sistema.php?ACAO=publico/dcto.lista.php&dcto=55')")

        def processos_semestre():
            nav.execute_script("window.open('')")
            nav.execute_script("window.open('https://596057.mannesoftprime.com.br/mannesoft/sistema.php?ACAO=publico/dcto.lista.php&dcto=63')")
        
        def a():
            nav.execute_script("window.open('')")
            nav.execute_script("window.open('')")

        #menu de opções de telas

        sg.theme('Reddit')
        layout = [
            [sg.Button('Aprovação de Alunos'), sg.Button('Documentos Oficiais'), sg.Button('Contas Correntes(em construção)')],
            [sg.Button('Matrícula'), sg.Button('Relatório Demanda'), sg.Button('WebPolo')],
            [sg.Button('Cadastro Curso'), sg.Button('Precificação Graduação'), sg.Button('Processos Semestre Letivo')],
            [sg.Button('Cadastro Disciplina'), sg.Button('Condições Pagamento'), sg.Button('...')],
            [sg.Button('Processo Seletivo'), sg.Button('Contas Correntes'), sg.Button('...')],
            [sg.Button('Descontos'), sg.Button('Acordo'), sg.Button('...')],
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
            elif eventos == 'Documentos Oficiais':
                documentos_oficiais()
            elif eventos == 'Relatório Demanda':
                documentos_oficiais()
            elif eventos == 'Precificação Graduação':
                precificacao()
            elif eventos == 'Condições Pagamento':
                condicoes_pagamento()
            elif eventos == 'Contas Correntes':
                contas_correntes()
            elif eventos == 'Descontos':
                descontos()
            elif eventos == 'Acordo':
                acordo()
            elif eventos == 'Contas Corrente(em construção)':
                contas_correntes2()
            elif eventos == 'WebPolo':
                webpolo()
            elif eventos == 'Processos Semestre Letivo':
                processos_semestre()
        
    if events == 'Salvar Login':
        Login=[values[('infos',i)] for i in range(2)]
        sg.user_settings_set_entry('login',Login)
    
    if events == sg.WIN_CLOSED:
        break
        