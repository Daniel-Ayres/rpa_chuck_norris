# 🤖 RPA Chuck Norris Jokes

Este projeto é uma automação RPA desenvolvida em Python, que consome a API pública do [Chuck Norris Jokes](https://api.chucknorris.io/). Ele realiza a coleta automática de uma piada para cada categoria disponível, salva os dados em uma planilha Excel e exibe as piadas no terminal. Todo o processo é registrado por logs, garantindo rastreabilidade da execução.

---

## 📌 Funcionalidades

- Consumo de API com requisições HTTP
- Coleta de piadas por categoria
- Escrita dos dados em planilha `.xlsx`
- Leitura da planilha e exibição organizada no console
- Geração de log detalhado em arquivo `.log`

---

## 🧱 Estrutura do Projeto


rpa_chuck_norris/
│
├── main.py                      # Script principal da automação
├── requirements.txt             # Dependências do projeto
├── .gitignore                   # Ignora arquivos temporários e diretórios não versionados
│
├── modules/                     # Módulos organizados por responsabilidade
│   ├── __init__.py
│   ├── consumidor_api.py        # Consome a API do Chuck Norris
│   ├── escritor_excel.py        # Salva piadas no Excel
│   ├── leitor_excel.py          # Lê e exibe piadas da planilha
│   └── log_config.py            # Configuração do sistema de logs
│
├── data/                        # Planilhas geradas (não versionadas)
└── logs/                        # Arquivos de log da execução (não versionados)

## 🚀 Como Executar

1.Clone o repositório:

git clone https://github.com/seu-usuario/rpa_chuck_norris.git
cd rpa_chuck_norris

2.Instale as dependências:

pip install -r requirements.txt


3.Execute o script:

python main.py


4.Após a execução:

A planilha será gerada em: data/chuck_norris_jokes.xlsx

O log estará disponível em: logs/execucao.log

As piadas serão exibidas formatadas no terminal


## 📦 Bibliotecas Utilizadas

Biblioteca |	Função
___________________________________________________________
requests	 |   Realiza requisições HTTP para consumir a API
___________________________________________________________
pandas	   |  Manipulação de dados e escrita no Excel
___________________________________________________________
openpyxl	 | Utilizada pelo pandas para salvar arquivos .xlsx
___________________________________________________________
logging	   |  Registro de logs de eventos e erros
___________________________________________________________
os	       | Criação de diretórios e manipulação de caminhos de arquivos
_____________________________________________________________

## ❓ Por que essas bibliotecas?
--requests é simples e robusta para consumir APIs RESTful, muito usada pela comunidade.

--pandas facilita a manipulação e estruturação dos dados, especialmente em formato tabular.

--openpyxl é a engine recomendada pelo pandas para escrever arquivos .xlsx (Excel).

--logging permite rastrear toda a execução da automação com controle de nível (INFO, ERROR etc).

--os possibilita a criação automática de pastas como data/ e logs/, tornando a automação independente do ambiente.

## 🧪 Exemplo de Saída no Terminal
Buscando categorias disponíveis...
Coletando uma piada por categoria...
Salvando piadas no Excel...

Piadas por categoria:
--------------------------------------------------------------------------------
Categoria: dev
ID       : a1whrz_crhgykfuah1mrmw
URL      : https://api.chucknorris.io/jokes/a1whrz_crhgykfuah1mrmw
Piada    : Chuck Norris's programs can pass the Turing Test by staring at the interrogator.
--------------------------------------------------------------------------------
Categoria: food
ID       : 4uqhu_nmtncleixytkl0pq
URL      : https://api.chucknorris.io/jokes/4uqhu_nmtncleixytkl0pq
Piada    : Chuck Norris proceeded to eat the chips, the bag, and the man in one deft move.
--------------------------------------------------------------------------------
...

## 🧑‍💻 Autor

Projeto desenvolvido por [Daniel Ayres] para fins de estudo e prática de automação RPA com Python e consumo de APIs REST.
