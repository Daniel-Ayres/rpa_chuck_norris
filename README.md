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

```bash
rpa_chuck_norris/
│
├── main.py                      # Script principal da automação
├── requirements.txt             # Dependências do projeto
├── .gitignore                   # Ignora arquivos temporários e diretórios não versionados
│
├── modules/                     # Módulos organizados por responsabilidade
│   ├── __init__.py
│   ├── consumidor_api.py        # Consome a API do Chuck Norris
│   ├── escritor_excel.py        # Salva as piadas no Excel
│   ├── leitor_excel.py          # Lê e exibe as piadas da planilha
│   └── log_config.py            # Configuração do sistema de logs
│
├── data/                        # Planilhas geradas (não versionadas)
└── logs/                        # Arquivos de log da execução (não versionados)
```

## 🚀 Como Executar

### **1️⃣ Clone o repositório**

```bash
git clone https://github.com/Daniel-Ayres/rpa_chuck_norris.git
cd rpa_chuck_norris
```

### 2️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```
### 3️⃣ Execute o script principal

```bash
python main.py
```
### 4️⃣ Após a execução

### 📁 A planilha será gerada em:

```bash
data/chuck_norris_jokes.xlsx
```

### 🪵 O log estará disponível em:
```bash
logs/execucao.log
```


## 📦 Bibliotecas Utilizadas

| Biblioteca | Descrição |
|-------------|------------|
| **requests** | Responsável por realizar as requisições HTTP para consumir a API pública do Chuck Norris. |
| **pandas** | Utilizada para manipulação e estruturação dos dados, além de facilitar a exportação para o formato Excel. |
| **openpyxl** | Engine utilizada pelo `pandas` para salvar os dados em arquivos `.xlsx`. |
| **logging** | Gerencia o registro de logs, permitindo rastrear cada etapa da execução da automação. |
| **os** | Manipula diretórios e caminhos de arquivos, criando automaticamente as pastas `data/` e `logs/`. |


## ❓ Por que essas bibliotecas?

- **🛰️ requests** — Simples e robusta para consumir **APIs RESTful**, amplamente utilizada pela comunidade Python.
  
- **📊 pandas** — Facilita a **manipulação e estruturação de dados** em formato tabular, permitindo salvar facilmente em planilhas Excel.
   
- **📘 openpyxl** — É a **engine recomendada pelo pandas** para leitura e escrita de arquivos `.xlsx` (Excel).
  
- **🧾 logging** — Permite **rastrear toda a execução da automação**, registrando informações e erros com diferentes níveis de log (`INFO`, `ERROR`, etc.).
   
- **📁 os** — Possibilita a **criação automática de diretórios**, como `data/` e `logs/`, tornando a automação independente do ambiente.  


## 🧪 Exemplo de Saída no Terminal

```bash
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
```


## 🧑‍💻 Autor

Projeto desenvolvido por [Daniel Ayres] para fins de estudo e prática de automação RPA com Python e consumo de APIs REST.
