#Desafio proposto em Aula, proposta de fazer o código funcionar
#Corrigido por Einstein Davys, e criada a interface gráfica, mais detalhes no Sobre dentro de Ajuda.
#Aluno de Engenharia de Software
# 30 de Novembro de 2021


import PySimpleGUI as sg
sg.theme('Random')

#tamanho da tela
WIN_W = 30
WIN_H = 50


#Layout
menu_layout = [
    ['Arquivo',['Sair']],
    ['Ajuda',['Sobre']]
    ]

#Primeira linha - ROW 1
layout = [[sg.Menu(menu_layout)],
            [sg.Input('0', size=(int(WIN_W/2), 1), font=('Consolas', 20), key='Memoria'),#visor da calculadora                  
            sg.Button('CE', size=(int(WIN_W/10), 1), font=('Consolas',20), key='LimpaUltima'),
            sg.Button('C', size=(int(WIN_W/10), 1), font=('Consolas', 20), key='-CLEAR-')],

#Segunda linha - ROW 2
            [sg.Button('%', font=('Consolas', 20), key='Porcentagem'),
            sg.Button('²', font=('Consolas', 20), key='Potencia'),
            sg.Button('√', font=('Consolas', 20), key='Raiz'),
            sg.Button('÷', font=('Consolas', 20), key='Dividir')],
#Terceira linha - ROW 3
            [sg.Button('7', font=('Consolas', 20), key='Sete'),
            sg.Button('8', font=('Consolas', 20), key='Oito'),
            sg.Button('9', font=('Consolas', 20), key='Nove'),
            sg.Button('×', font=('Consolas', 20), key='Vezes')],
#Quarta linha - ROW 4
            [sg.Button('4', font=('Consolas', 20), key='Quatro'),
            sg.Button('5', font=('Consolas', 20), key='Cinco'),
            sg.Button('6', font=('Consolas', 20), key='Seis'),
            sg.Button('-', font=('Consolas', 20), key='Subtrair')],
#Quinta linha - ROW 5
            [sg.Button('1', font=('Consolas', 20), key='UM'),
            sg.Button('2', font=('Consolas', 20), key='Dois'),
            sg.Button('3', font=('Consolas', 20), key='Tres'),
            sg.Button('+', font=('Consolas', 20), key='Somar')],
#Sexta linha - ROW 6
            [sg.Button('0', font=('Consolas', 20), key='Zero'),
            sg.Button('.', font=('Consolas', 20), key='Ponto'),
            sg.Button('=', size=(int(WIN_W/3.5), 1), font=('Consolas', 20), key='Resultado')]]

#class
class App():
    def __init__(self):
        self.window = sg.Window('Calculadora em Python', layout=layout, margins=(0,0), resizable=True, return_keyboard_events=False)
        self.result = 0
        self.oper = ''
        self.window.read(timeout=1) #
        for i in range(1,7):
            for button in layout[i]:
                button.expand(expand_x = True, expand_y=True)

#função menu popup
    def about(self):
        sg.popup("Sobre", 'Na Faculdade me entregaram o código de uma calculadora com as 4 operações básicas da matemática, este para ser corrigido e melhorado se assim fosse possível. Bom, acressentei a %, Raíz Quadrada e Potencialização, corrigi erros de sintaxe que impediam a mesma funcionar, criei uma interface com SimpleGUI, e coloquei símbolos existentes numa calculadora convencional.')

        
#funções matemáticas
    def resulter(self):
        if self.oper == '+':
            return float(self.result) + float(self.values['Memoria'])
        if self.oper == '-':
            return float(self.result) - float(self.values['Memoria'])
        if self.oper == '×':
            return float(self.result) * float(self.values['Memoria'])
        if self.oper == '÷':
            return float(self.result) / float(self.values['Memoria'])
        if self.oper == '%':
            return float(self.values['Memoria']) * float(self.result) / 100
        if self.oper == '²':
            return float(self.result) ** 2
        if self.oper =='√':
            return float(self.result) ** 0.5
       
#Start de funcionamento
    def start(self):
        while True:
            event, self.values = self.window.read()

            if event in (None, 'Sair', sg.WINDOW_CLOSED):
                break

            if event in ('Sobre'):
                self.about()

            if event in ('UM'):
                if self.values['Memoria'] == '0':
                    self.window['Memoria'].update(value='1')
                
                else:
                    self.window['Memoria'].update(value=self.values['Memoria'] + '1')

            if event in ('Dois'):
                if self.values['Memoria'] == '0':
                    self.window['Memoria'].update(value='2')
                
                else:
                    self.window['Memoria'].update(value=self.values['Memoria'] + '2')
            
            if event in ('Tres'):
                if self.values['Memoria'] == '0':
                    self.window['Memoria'].update(value='3')
                
                else:
                    self.window['Memoria'].update(value=self.values['Memoria'] + '3')

            if event in ('Quatro'):
                if self.values['Memoria'] == '0':
                    self.window['Memoria'].update(value='4')
                
                else:
                    self.window['Memoria'].update(value=self.values['Memoria'] + '4')
            
            if event in ('Cinco'):
                if self.values['Memoria'] == '0':
                    self.window['Memoria'].update(value='5')
                
                else:
                    self.window['Memoria'].update(value=self.values['Memoria'] + '5')
                
            if event in ('Seis'):
                if self.values['Memoria'] == '0':
                    self.window['Memoria'].update(value='6')
                
                else:
                    self.window['Memoria'].update(value=self.values['Memoria'] + '6')
            
            if event in ('Sete'):
                if self.values['Memoria'] == '0':
                    self.window['Memoria'].update(value='7')
                
                else:
                    self.window['Memoria'].update(value=self.values['Memoria'] + '7')

            if event in ('Oito'):
                if self.values['Memoria'] == '0':
                    self.window['Memoria'].update(value='8')
                
                else:
                    self.window['Memoria'].update(value=self.values['Memoria'] + '8')

            if event in ('Nove'):
                if self.values['Memoria'] == '0':
                    self.window['Memoria'].update(value='9')
                
                else:
                    self.window['Memoria'].update(value=self.values['Memoria'] + '9')

            if event in ('Zero'):
                if self.values['Memoria'] == '0':
                    self.window['Memoria'].update(value='0')
                
                else:
                    self.window['Memoria'].update(value=self.values['Memoria'] + '0')
            
            if event in('Ponto'):
                if self.values['Memoria'] == '.':
                    self.window['Memoria'].update(value='.')

                else: 
                    self.window['Memoria'].update(value=self.values['Memoria'] + '.')

#FUNÇÕES DE APAGAR ÚLTIMO E GERAL    
            if event in ('-CLEAR-'):
                self.result = 0
                self.window['Memoria'].update(value = self.result)

            if event in ('LimpaUltima'):
                self.window['Memoria'].update(value = self.values['Memoria'][:-1])

# + , - , * ,  / 
            if event in ('Somar'):
                if self.oper != '':
                    self.result = self.resulter()

                else: 
                    self.oper = '+'
                    self.result = self.values['Memoria']    
                self.window['Memoria'].update(value='')
            
            if event in ('Subtrair'):
                if self.oper != '':
                    self.result = self.resulter()

                else: 
                    self.oper = '-'
                    self.result = self.values['Memoria']    
                self.window['Memoria'].update(value='')
            
            if event in ('Dividir'):
                if self.oper != '':
                    self.result = self.resulter()

                else: 
                    self.oper = '÷'
                    self.result = self.values['Memoria']    
                self.window['Memoria'].update(value='')
            
            if event in ('Vezes'):
                if self.oper != '':
                    self.result = self.resulter()

                else: 
                    self.oper = '×'
                    self.result = self.values['Memoria']    
                self.window['Memoria'].update(value='')

            if event in ('Porcentagem'):
                if self.oper != '':
                    self.result = self.resulter()
                
                else:
                    self.oper = '%'
                    self.result = self.values['Memoria']
                self.window['Memoria'].update(value='')
            
            if event in ('Potencia'):
                if self.oper !='':
                    self.result = self.resulter()
                
                else:
                    self.oper ='²'
                    self.result = self.values['Memoria']
                self.window['Memoria'].update(value='')

            if event in ('Raiz'):
                if self.oper !='':
                    self.result = self.resulter()
                
                else:
                    self.oper ='√'
                    self.result = self.values['Memoria']
                self.window['Memoria'].update(value='')    

            if event in ('Resultado'):
                self.result = self.resulter()
                self.window['Memoria'].update(value = self.result)
                self.result = 0
                self.oper = ''


App().start()



