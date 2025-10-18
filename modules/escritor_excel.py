"""
Módulo responsável por salvar as piadas em uma planilha Excel.
Cria a pasta de saída se necessário e registra logs de sucesso ou falha.
"""

import pandas as pd
import os
import logging

PASTA_DADOS = "data"
ARQUIVO_SAIDA = "chuck_norris_jokes.xlsx" 

def salvar_piadas_em_excel(piadas):
    try:
        if not os.path.exists(PASTA_DADOS):
            os.makedirs(PASTA_DADOS)
            logging.info(f"Pasta '{PASTA_DADOS}' criada.")

        df = pd.DataFrame(piadas)
        caminho = os.path.join(PASTA_DADOS, ARQUIVO_SAIDA)
        df.to_excel(caminho, index=False)
        logging.info(f" Planilha salva com sucesso em: {caminho}")
        print(f"Arquivo salvo em: {caminho}")
    except Exception as e:
        logging.exception("Erro ao salvar piadas no Excel")
        raise
