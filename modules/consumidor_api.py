"""
Módulo responsável por consumir a API do Chuck Norris,
obtendo categorias e piadas aleatórias por categoria.
Inclui logs para rastrear chamadas e possíveis erros.
"""

import requests
import logging

URL_BASE = "https://api.chucknorris.io"

def obter_categorias():
    try:
        resposta = requests.get(f"{URL_BASE}/jokes/categories")
        resposta.raise_for_status()
        categorias = resposta.json()
        logging.info(f"Categorias obtidas com sucesso: {categorias}")
        return categorias
    except Exception as e:
        logging.exception("Erro ao obter categorias da API")
        raise

def obter_piada_por_categoria(categoria):
    try:

        logging.info(f"Buscando piada para categoria: '{categoria}'")

        resposta = requests.get(f"{URL_BASE}/jokes/random", params={"category": categoria})

        resposta.raise_for_status()
        dados = resposta.json()

        logging.info(f"Piada obtida (ID: {dados['id']}) para categoria '{categoria}'")

        return {
            "id": dados["id"],
            "url": dados["url"],
            "value": dados["value"],
            "category": categoria
        }
    except Exception as e:
        logging.exception(f"Erro ao obter piada da categoria '{categoria}'")
        raise
