# EthioMart Scripts

This folder contains Python scripts that implement the data processing pipeline for the EthioMart project. Each script is modular and handles specific tasks.

### Scripts Overview

1. **`data_ingestion.py`**:

   - Fetches data from Telegram channels.
   - Saves the data to an Excel file for further processing.

2. **`data_preprocessing.py`**:

   - Cleans and preprocesses raw data.
   - Handles tokenization and removes unnecessary characters or noise.

3. **`labeling.py`**:

   - Converts structured data into CoNLL format for use in NLP tasks.

4. **`pipeline_runner.py`**:
   - Integrates the entire pipeline, running all scripts sequentially.

### Usage

1. **Run Individual Scripts**:

   - Example: Running data ingestion only:
     ```bash
     python scripts/data_ingestion.py
     ```

2. **Run the Full Pipeline**:
   ```bash
   python scripts/pipeline_runner.py
   ```

### Configuration

- **Input Files**: Place your raw files (e.g., `channels_to_crawl.csv`, `labeled_telegram_product_price_location.txt`) in the `data/raw/` folder.
- **Output Files**: Processed files will be saved in the `data/processed/` folder.
