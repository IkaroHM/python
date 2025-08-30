import tkinter as tk
cores = ['yellow', 'blue', 'green', 'purple']
c = 0
def clique():
    global c
    c += 1
    botao.config(text=f'Cliques: {c}')
    janela.config(bg=cores[c % 4])
janela = tk.Tk()
janela.geometry("300x200")
janela.config(bg=cores[0])
botao = tk.Button(janela,text='Cliques: 0', font=('arial',20),command=clique)
botao.pack(expand=True)
janela.mainloop()
