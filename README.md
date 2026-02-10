# Weather ETL Pipeline

Pipeline ETL para extração, transformação e carregamento de dados climáticos da API Open-Meteo.

## 📋 Sobre o Projeto

Este projeto implementa um pipeline ETL completo que:
- **Extrai** dados climáticos em tempo real da API Open-Meteo
- **Transforma** os dados brutos em formato estruturado
- **Carrega** os dados processados em arquivos CSV/JSON

## 🚀 Tecnologias

- Python 3.8+
- Requests (requisições HTTP)
- Pandas (manipulação de dados)
- PyYAML (configuração)

## 📦 Instalação
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/weather-etl-pipeline.git
cd weather-etl-pipeline

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

## ⚙️ Configuração

Edite o arquivo `config/config.yaml` com as coordenadas desejadas:
```yaml
api:
  base_url: "https://api.open-meteo.com/v1/forecast"
  latitude: -23.5505  # São Paulo
  longitude: -46.6333
```

## 🎯 Uso
```bash
python main.py
```

Os dados processados serão salvos em `data/processed/`

## 📁 Estrutura do Projeto
```
weather-etl-pipeline/
├── data/
│   ├── raw/              # Dados brutos da API
│   └── processed/        # Dados processados
├── src/
│   ├── extract.py        # Extração de dados
│   ├── transform.py      # Transformação
│   └── load.py           # Carregamento
├── config/
│   └── config.yaml       # Configurações
├── logs/                 # Logs da aplicação
├── main.py              # Orquestrador
└── requirements.txt     # Dependências
```

## 📊 Dados Coletados

- Temperatura atual (°C)
- Precipitação (mm)
- Código do clima
- Timestamp da coleta
