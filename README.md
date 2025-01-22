# EthioMart: Telegram-Based E-Commerce Platform

EthioMart is an innovative e-commerce solution leveraging Telegram channels to extract, process, and analyze product data. This project provides an end-to-end pipeline for collecting product details, prices, and locations from Telegram messages and formatting the data for use in machine learning tasks such as Named Entity Recognition (NER).

---

## Features

1. **Telegram Data Fetching**: Extracts messages from selected Telegram channels, enabling real-time data collection.
2. **Data Preprocessing**: Cleans and structures raw data by handling tokenization, removing noise, and preparing it for downstream analysis.
3. **NER Pipeline**: Converts processed data into CoNLL format, suitable for NLP tasks like Named Entity Recognition.
4. **Quantitative Analysis and Visualization**:
   - Advanced analysis using TA-Lib and PyNance for financial data insights.
   - Comprehensive exploratory data analysis (EDA) via Jupyter notebooks.
5. **End-to-End Modular Pipeline**: Streamlined and automated workflow, integrating all steps from data ingestion to evaluation.

---

## Repository Structure

```plaintext
EthioMart-Telegram-based-e-commerce/
├── data/
│   ├── raw/               # Raw data files (e.g., Telegram messages)
│   └── processed/         # Processed data files (e.g., CoNLL format)
├── notebooks/             # Jupyter notebooks for analysis and visualization
├── scripts/               # Python scripts for pipeline execution
├── results/               # Results from analysis and model evaluation
└── README.md              # General project overview
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/abenaacs/EthioMart-Telegram-based-e-commerce.git
cd EthioMart-Telegram-based-e-commerce
```

### 2. Set Up Virtual Environment

```bash
python -m venv env
source env/bin/activate  # For Windows: .\env\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the Pipeline

Execute the full pipeline or individual scripts:

#### Full Pipeline Execution

```bash
python scripts/pipeline_runner.py
```

#### Individual Scripts

Run specific scripts as needed:

- **Data Ingestion**:
  ```bash
  python scripts/data_ingestion.py
  ```
- **Data Preprocessing**:
  ```bash
  python scripts/data_preprocessing.py
  ```
- **Data Labeling**:
  ```bash
  python scripts/labeling.py
  ```

---

## Configuration

1. **Input Files**:

   - Place your raw files (e.g., `channels_to_crawl.csv`, `labeled_telegram_product_price_location.txt`) in the `data/raw/` folder.

2. **Output Files**:

   - Processed files will be saved in the `data/processed/` folder.

3. **Results**:
   - Analysis results and visualizations are stored in the `results/` directory.

---

## Key Enhancements

1. **Integration with Financial Analysis Tools**:

   - Implemented advanced quantitative analysis using **TA-Lib** and **PyNance** for trend detection and investment insights.

2. **Exploratory Data Analysis (EDA)**:

   - Comprehensive exploration of collected data, leveraging visualizations and statistical summaries to derive actionable insights.

3. **Streamlined Evaluation**:
   - Automated evaluation of the NER pipeline with classification metrics, including precision, recall, and F1 scores.

---

## Explore the Outputs

- **Processed Files**: Located in `data/processed/`
- **Logs and Debug Info**: Accessible in `logs/`
- **Results**: Available in `results/` for financial insights and EDA outputs.

---

## Future Scope

- **Real-Time Integration**: Expand Telegram data fetching to include real-time updates.
- **Multi-language Support**: Extend NER pipeline for multi-language datasets.
- **Enhanced Visualization**: Incorporate dashboards for dynamic visual analytics.

---

EthioMart continues to evolve, aiming to deliver robust e-commerce capabilities powered by advanced data analytics and machine learning. Your contributions are welcome!
