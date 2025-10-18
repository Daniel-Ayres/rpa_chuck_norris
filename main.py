"""
RPA em Python para coletar piadas do Chuck Norris via API,
salvar em planilha Excel e exibir os resultados no terminal.
Inclui logs para rastrear todas as etapas da execução.
"""


from modules.consumidor_api import obter_categorias, obter_piada_por_categoria
from modules.escritor_excel import salvar_piadas_em_excel
from modules.leitor_excel import ler_e_exibir_piadas
from modules.log_config import configurar_logs
import os
import logging

CAMINHO_ARQUIVO = os.path.join("data", "chuck_norris_jokes.xlsx")

def main():
    configurar_logs()
    logging.info("Iniciando execução do RPA Chuck Norris")

    try:
        print("Buscando categorias disponíveis...")
        categorias = obter_categorias()
        logging.info(f"Categorias obtidas: {categorias}")

        print("Coletando uma piada por categoria...")
        piadas = [obter_piada_por_categoria(categoria) for categoria in categorias]
        logging.info(f"Total de piadas coletadas: {len(piadas)}")

        print("Salvando piadas no Excel...")
        salvar_piadas_em_excel(piadas)

        print("\nLendo e exibindo piadas da planilha:")
        ler_e_exibir_piadas(CAMINHO_ARQUIVO)

        logging.info("Execução finalizada com sucesso.")

    except Exception as e:
        logging.exception("Erro durante execução:")
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
