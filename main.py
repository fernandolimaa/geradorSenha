import tkinter as tk
from tkinter import ttk

# Função para converter unidades
def converter():
    valor = entry_valor.get()
    try:
        valor = float(valor)  # Tenta converter o valor para float
        origem = unidade_origem.get()
        destino = unidade_destino.get()
        
        # Conversões de comprimento
        if origem == "Metros" and destino == "Quilômetros":
            resultado = valor / 1000

        elif origem == "Quilômetros" and destino == "Metros":
            resultado = valor * 1000

        elif origem == "Metros" and destino == "Centímetros":
            resultado = valor * 100

        elif origem == "Centímetros" and destino == "Metros":
            resultado = valor / 100

        elif origem == "Metros" and destino == "Milímetros":
            resultado = valor * 1000

        elif origem == "Milímetros" and destino == "Metros":
            resultado = valor / 1000

        elif origem == "Metros" and destino == "Decímetros":
            resultado = valor * 10
            
        elif origem == "Decímetros" and destino == "Metros":
            resultado = valor / 10

        # Conversões de volume
        elif origem == "Litros" and destino == "Mililitros":
            resultado = valor * 1000
        elif origem == "Mililitros" and destino == "Litros":
            resultado = valor / 1000

        # Conversões de temperatura
        elif origem == "Celsius" and destino == "Fahrenheit":
            resultado = (valor * 9/5) + 32
        elif origem == "Fahrenheit" and destino == "Celsius":
            resultado = (valor - 32) * 5/9

        else:
            label_resultado.config(text="Conversão não suportada.")
            return

        label_resultado.config(text=f"{valor} {origem} = {resultado:.2f} {destino}")
    except ValueError:
        label_resultado.config(text="Por favor, insira um valor numérico válido.")

# Criando a janela principal
janela = tk.Tk()
janela.title("Conversor de Unidades")



janela.mainloop()