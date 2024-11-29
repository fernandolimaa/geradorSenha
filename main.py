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


# Campo de entrada do valor
label_valor = tk.Label(janela, text="Digite o valor:")
label_valor.pack()

entry_valor = tk.Entry(janela, width=20)
entry_valor.pack()

# Combobox para unidades de origem
label_origem = tk.Label(janela, text="Unidade de origem:")
label_origem.pack()

unidade_origem = ttk.Combobox(
    janela, 
    values=[
        "Metros", "Quilômetros", "Centímetros", "Milímetros", "Decímetros",
        "Litros", "Mililitros",
        "Celsius", "Fahrenheit"
    ]
)
unidade_origem.set("Metros")  # Definindo um valor padrão
unidade_origem.pack()

# Combobox para unidades de destino
label_destino = tk.Label(janela, text="Unidade de destino:")
label_destino.pack()

unidade_destino = ttk.Combobox(
    janela, 
    values=[
        "Metros", "Quilômetros", "Centímetros", "Milímetros", "Decímetros",
        "Litros", "Mililitros",
        "Celsius", "Fahrenheit"
    ]
)
unidade_destino.set("Quilômetros")  # Definindo um valor padrão
unidade_destino.pack()

# Botão para realizar a conversão
botao_converter = tk.Button(janela, text="Converter", command=converter)
botao_converter.pack()

# Rótulo para mostrar o resultado
label_resultado = tk.Label(janela, text="Resultado: ")
label_resultado.pack()

janela.mainloop()