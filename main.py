import PySimpleGUI as sg

sg.theme('DarkAmber')  # Dando um toque de cor

# Todas as coisas dentro da tela
layout = [[sg.Text('Texto 1')],
          [sg.Text('Texto 2'), sg.InputText()],
          [sg.Button('OK'), sg.Button('Cancel')]
          ]

# Criando a janela

janela = sg.Window('Primeira Janela', layout)

# Loop para processar os eventos e pegar os valores das entradas
while True:
    eventos, valores = janela.Read()
    if eventos == sg.WIN_CLOSED or eventos == 'Cancel':
        break
    print('Você entrou com o valor, ', valores[0])
janela.close()
