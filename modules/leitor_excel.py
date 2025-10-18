"""
Módulo responsável por ler a planilha Excel gerada
e exibir as piadas formatadas no terminal, por categoria.
"""


import pandas as pd
import os

def ler_e_exibir_piadas(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        print("Arquivo não encontrado.")
        return

    df = pd.read_excel(caminho_arquivo)

    print("\n Piadas por categoria:\n" + "-" * 80)
    for i, row in df.iterrows():
        print(f"Categoria: {row['category']}")
        print(f"ID       : {row['id']}")
        print(f"URL      : {row['url']}")
        print(f"Piada    : {row['value']}\n")
        print("-" * 80)
