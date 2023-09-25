import tkinter as tk # tkinter para interfaces graficas, das mais simples as mais complexas
from tkinter import * # outra forma de importar o tk

# variaveis de numero vazias ate receberem a entrada. variaveis das operações false ate passarem pelo if sendo true
numero1 = ''
numero2 = ''
adicao = FALSE
subtracao = FALSE
multiplicacao = FALSE
divisao = FALSE

# variaveis para customizar a interface da calc
root = Tk()
root.title('Sua calculadora')
root.geometry("408x355")
root.maxsize(408, 355)
root.minsize(408, 355)


root.configure(background='#282828') # configurar a cor do background

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF',
          bg='#a7a28f', font=('futura', 25, 'bold'), justify=CENTER)
e.grid( # usa o conceito de linhas e colunas para organizar os widgets(elementos de interacao tipo janelas, botoes)
    row=0,
    column=0,
    columnspan=4, # quantidade de colunas q ele ocupa dos botoes
    pady=2 # distancia entre o botao e o numero que to escrevendo
)

# funcao para o clique do mouse
def botao_click(num):
    e.insert(END, num) # end pq insere o argumento no final e insere um numero

# funcao para somar
def botao_adiciona():
    global numero1
    global adicao
    adicao = TRUE # so se torna true quando clica no botao
    numero1 = e.get() # pegar oq inseriu
    e.delete(0, END) # delete pq depois q inseriu o primeiro numero q colocou, tem q limpar a entrada. 0 seria para o comeco e End para o fim. 

# funcao para subtrair
def botao_subrai():
    global numero1
    global subtracao
    subtracao = TRUE
    numero1 = e.get()
    e.delete(0, END)

# funcao para multiplicar
def botao_multiplica():
    global numero1
    global multiplicacao
    multiplicacao = TRUE
    numero1 = e.get()
    e.delete(0, END)

# funcao para dividir
def botao_divide():
    global numero1
    global divisao
    divisao = TRUE
    numero1 = e.get()
    e.delete(0, END)

# funcao para finalizar a operacao, responsavel por mostrar o resultado das entradas
def botao_igual():
    global subtracao
    global divisao
    global multiplicacao
    global adicao
    numero2 = e.get()
    e.delete(0, END)
    if adicao == TRUE:
        e.insert(0, int(numero1) + int(numero2))
        adicao = FALSE # aqui ele precisa ser falso pq se somar 5+5 e depois quiser ja fazer outra operacao, o adicao vai estar ativo e vai quebrar a logica
    if multiplicacao == TRUE:
        e.insert(0, int(numero1) * int(numero2))
        multiplicacao = FALSE
    if subtracao == TRUE:
        e.insert(0, int(numero1) - int(numero2))
        subtracao = FALSE
    if divisao == TRUE:
        e.insert(0, int(numero1) // int(numero2))
        divisao = FALSE

# funcao para limpar tudo
def botao_limpa():
    e.delete(0, END)


def botao_num(num, row, column):
    botao = Button(root,
                   text=num,
                   padx=40, # distancia na horizontal
                   pady=20, # distancia na vertical
                   command=lambda: botao_click(num),
                   fg='#FFFFFF',
                   activebackground='#240046',
                   activeforeground='#FFFFFF', #cor quando vc coloca o mouse em cima
                   bg='#282828',
                   relief=FLAT,
                   font=('futura', 12, 'bold'))
    botao.grid(row=row, column=column)


def botao_operador(op, command, row, column):
    operador = Button(root,
                      text=op,
                      padx=40,
                      pady=20,
                      command=command,
                      fg='#FFFFFF',
                      activebackground='#240046',
                      activeforeground='#FFFFFF',
                      bg='#320064',
                      relief=FLAT,
                      font=('futura', 12, 'bold'))
    operador.grid(row=row, column=column)


botao_operador('÷', botao_divide, 0, 4)
# primeira fileira
botao_num(1, 1, 1)
botao_num(2, 1, 2)
botao_num(3, 1, 3)
botao_operador('×', botao_multiplica, 1, 4)
# segunda fileira
botao_num(4, 2, 1)
botao_num(5, 2, 2)
botao_num(6, 2, 3)
botao_operador(' -', botao_subrai, 2, 4)
# terceira fileira
botao_num(7, 3, 1)
botao_num(8, 3, 2)
botao_num(9, 3, 3)
botao_operador('+', botao_adiciona, 3, 4)
# quarta fileira
zero = Button(root,
              text='0',
              padx=91,
              pady=20,
              command=lambda: botao_click(0),
              fg='#FFFFFF',
              activebackground='#240046',
              activeforeground='#FFFFFF',
              bg='#282828',
              relief=FLAT,
              font=('futura', 12, 'bold'))
zero.grid(row=4, column=1, columnspan=2)
botao_operador('C', botao_limpa, 4, 4)
botao_operador('=', botao_igual, 4, 3)

root.mainloop()
