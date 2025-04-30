import tkinter as tk
 
def clicar(botao):
    atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, atual + botao)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, resultado)
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

def limpar():
    entrada.delete(0, tk.END)

def tecla_pressionada(event):
    tecla = event.char
    if tecla in '0123456789.+-*/':
        clicar(tecla)
    elif tecla == '\r':  # Enter
        calcular()
    elif tecla == '\x08':  # Backspace
        limpar()

janela = tk.Tk()
janela.title("Calculadora")

entrada = tk.Entry(janela, width=20, font=("Arial", 24), borderwidth=5, relief="ridge", justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

botoes = {
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
}

for (texto, linha, coluna) in botoes:
    if texto == '=':
        tk.Button(janela, text=texto, width=5, height=2, font=("Arial", 18),
                  command=calcular).grid(row=linha, column=coluna)
    elif texto == 'C':
        tk.Button(janela, text=texto, width=23, height=2, font=("Arial", 18),
                  command=limpar).grid(row=linha, column=coluna, columnspan=4)
    else:
        tk.Button(janela, text=texto, width=5, height=2, font=("Arial", 18),
                  command=lambda t=texto: clicar(t)).grid(row=linha, column=coluna)
        
janela.bind('<Key>', tecla_pressionada)
janela.mainloop()
