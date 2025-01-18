## General README (For Repository)

# EthioMart: Telegram-Based E-Commerce Platform

EthioMart is an innovative e-commerce solution leveraging Telegram channels to extract, process, and analyze product data. This project provides an end-to-end pipeline for collecting product details, prices, and locations from Telegram messages and formatting the data for use in machine learning tasks such as Named Entity Recognition (NER).

### Features

- **Telegram Data Fetching**: Extracts messages from selected Telegram channels.
- **Data Preprocessing**: Cleans and structures raw data for analysis.
- **NER Pipeline**: Converts processed data into CoNLL format for NLP applications.
- **Modular Design**: Scripts and notebooks are organized for easy understanding and extensibility.

### Repository Structure

```
EthioMart-Telegram-based-e-commerce/
├── data/
│   ├── raw/               # Raw data files (Telegram messages, etc.)
│   └── processed/         # Processed data files (CoNLL format, etc.)
├── notebooks/          # Jupyter notebooks for analysis and visualization
├── scripts/            # Python scripts for pipeline execution
└── README.md          # General project overview
```

### Getting Started

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/abenaacs/EthioMart-Telegram-based-e-commerce.git
   cd EthioMart-Telegram-based-e-commerce
   ```

2. **Set Up Virtual Environment**:

   ```bash
   python -m venv env
   source env/bin/activate  # For Windows: .\env\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the Pipeline**:

   ```bash
   python scripts/pipeline_runner.py
   ```

4. **Explore the Outputs**:
   - Processed files: `data/processed/`
   - Logs and debug info: `logs/`
