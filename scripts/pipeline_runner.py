from data_ingestion import fetch_telegram_data
from preprocessing import preprocess_data, preprocess_images
from labeling import convert_to_conll_format, label_images
from dotenv import load_dotenv
import os


def run_pipeline():
    # Paths
    raw_folder = "./data/raw/"
    processed_folder = "./data/processed/"
    os.makedirs(processed_folder, exist_ok=True)

    load_dotenv()

    # Step 1: Fetch Telegram Data (Text + Images)
    api_id = os.getenv("TG_API_ID")
    api_hash = os.getenv("TG_API_HASH")
    channels_file = os.path.join(raw_folder, "channels_to_crawl.csv")
    output_excel = os.path.join(processed_folder, "telegram_data.xlsx")
    output_image_folder = os.path.join(processed_folder, "images/")
    os.makedirs(output_image_folder, exist_ok=True)

    with open(channels_file, "r") as f:
        channels = [line.strip() for line in f.readlines()]

    print("Fetching Telegram data...")
    fetch_telegram_data(api_id, api_hash, channels, output_excel, output_image_folder)

    # Step 2: Preprocess Data (Text)
    raw_text_file = os.path.join(
        raw_folder, "labeled_telegram_product_price_location.txt"
    )
    preprocessed_text_file = os.path.join(processed_folder, "preprocessed_text.txt")

    print("Preprocessing text data...")
    preprocess_data(raw_text_file, preprocessed_text_file)

    # Step 3: Preprocess Images
    print("Preprocessing images...")
    preprocessed_image_folder = os.path.join(processed_folder, "preprocessed_images/")
    os.makedirs(preprocessed_image_folder, exist_ok=True)
    preprocess_images(output_image_folder, preprocessed_image_folder)

    # Step 4: Convert Text to CoNLL Format
    conll_file = os.path.join(processed_folder, "labeled_conll.txt")

    print("Converting text data to CoNLL format...")
    convert_to_conll_format(preprocessed_text_file, conll_file)

    # Step 5: Label Images
    print("Labeling images...")
    labels_file = os.path.join(processed_folder, "image_labels.json")
    label_images(preprocessed_image_folder, labels_file)

    print(f"Pipeline completed. Output files saved in {processed_folder}")


if __name__ == "__main__":
    run_pipeline()
