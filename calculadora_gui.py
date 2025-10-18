import tkinter as tk

def clicar(botao):
    atual = entrada.get()
    if botao == "=":
        try:
            resultado = eval(atual)
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, str(resultado))
        except:
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, "Erro")
    elif botao == "C":
        entrada.delete(0, tk.END)
    else:
        entrada.insert(tk.END, botao)

# Janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")
janela.resizable(False, False)

# Campo de entrada
entrada = tk.Entry(janela, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entrada.pack(fill=tk.BOTH, padx=10, pady=10)

# Botões
botoes = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

for linha in botoes:
    frame = tk.Frame(janela)
    frame.pack(expand=True, fill="both")
    for botao in linha:
        btn = tk.Button(frame, text=botao, font=("Arial", 18), bd=5, relief=tk.RAISED,
                        command=lambda b=botao: clicar(b))
        btn.pack(side="left", expand=True, fill="both")

janela.mainloop()
