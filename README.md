# Weather ETL Pipeline

ETL pipeline for extracting, transforming, and loading weather data from Open-Meteo API.

## 📋 About the Project

This project implements a complete ETL pipeline that:
- **Extracts** real-time weather data from Open-Meteo API
- **Transforms** raw data into structured format
- **Loads** processed data into CSV/JSON files

## 🚀 Technologies

- Python 3.8+
- Requests (HTTP requests)
- Pandas (data manipulation)
- PyYAML (configuration)

## 📦 Installation
```bash
# Clone the repository
git clone https://github.com/your-username/weather-etl-pipeline.git
cd weather-etl-pipeline

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## ⚙️ Configuration

Edit the `config/config.yaml` file with desired coordinates:
```yaml
api:
  base_url: "https://api.open-meteo.com/v1/forecast"
  latitude: -23.5505  # São Paulo
  longitude: -46.6333
```

## 🎯 Usage
```bash
python main.py
```

Processed data will be saved in `data/processed/`

## 📁 Project Structure
```
weather-etl-pipeline/
├── data/
│   ├── raw/              # Raw API data
│   └── processed/        # Processed data
├── src/
│   ├── extract.py        # Data extraction
│   ├── transform.py      # Transformation
│   └── load.py           # Loading
├── config/
│   └── config.yaml       # Configuration
├── logs/                 # Application logs
├── main.py              # Orchestrator
└── requirements.txt     # Dependencies
```

## 📊 Collected Data

- Current temperature (°C)
- Precipitation (mm)
- Weather code
- Collection timestamp
