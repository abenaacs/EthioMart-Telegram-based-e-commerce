from data_ingestion import fetch_telegram_data
from preprocessing import preprocess_data
from labeling import convert_to_conll_format
from dotenv import load_dotenv
import os


def run_pipeline():
    # Paths
    raw_folder = "./data/raw/"
    processed_folder = "./data/processed/"
    os.makedirs(processed_folder, exist_ok=True)

    load_dotenv()

    # Step 1: Fetch Telegram Data
    api_id = os.getenv("TG_API_ID")
    api_hash = os.getenv("TG_API_HASH")
    channels_file = os.path.join(raw_folder, "channels_to_crawl.csv")
    output_excel = os.path.join(processed_folder, "telegram_data.xlsx")

    with open(channels_file, "r") as f:
        channels = [line.strip() for line in f.readlines()]

    print("Fetching Telegram data...")
    fetch_telegram_data(api_id, api_hash, channels, output_excel)

    # Step 2: Preprocess Data
    raw_text_file = os.path.join(
        raw_folder, "labeled_telegram_product_price_location.txt"
    )
    preprocessed_text_file = os.path.join(processed_folder, "preprocessed_text.txt")

    print("Preprocessing data...")
    preprocess_data(raw_text_file, preprocessed_text_file)

    # Step 3: Convert to CoNLL Format
    conll_file = os.path.join(processed_folder, "labeled_conll.txt")

    print("Converting to CoNLL format...")
    convert_to_conll_format(preprocessed_text_file, conll_file)

    print(f"Pipeline completed. Output files saved in {processed_folder}")


if __name__ == "__main__":
    run_pipeline()
