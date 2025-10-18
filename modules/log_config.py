"""
Módulo responsável por configurar o sistema de logs do projeto.
Garante criação da pasta de logs e registra eventos com codificação UTF-8.
"""


import logging
import os

PASTA_LOGS = "logs"
ARQUIVO_LOG = os.path.join(PASTA_LOGS, "execucao.log")

def configurar_logs():
    if not os.path.exists(PASTA_LOGS):
        os.makedirs(PASTA_LOGS)

    logging.basicConfig(
        filename=ARQUIVO_LOG,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode="a",
        encoding="utf-8"
    )

    logging.info("Sistema de logs configurado.")
