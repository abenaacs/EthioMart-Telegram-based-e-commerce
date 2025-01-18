# preprocessing.py
import pandas as pd
import re
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def preprocess_amharic_text(text):
    """Normalize and clean Amharic text."""
    text = re.sub(r"[^\w\s፣።]", "", text)  # Remove special characters
    text = re.sub(r"\s+", " ", text)  # Remove extra spaces
    text = text.strip()
    return text


def preprocess_data(input_file, output_file):
    """Preprocess and save cleaned data."""
    try:
        logging.info(f"Reading data from {input_file}")

        if input_file.endswith(".xlsx") or input_file.endswith(".xls"):
            df = pd.read_excel(input_file, engine="openpyxl")
        elif input_file.endswith(".csv"):
            df = pd.read_csv(input_file)
        elif input_file.endswith(".txt"):
            with open(input_file, "r", encoding="utf-8") as f:
                lines = f.readlines()

            tokens = []
            labels = []

            for line in lines:
                line = line.strip()
                if line:
                    try:
                        token, label = line.split(" ", 1)
                        tokens.append(token)
                        labels.append(label)
                    except ValueError:
                        continue

            # Create a DataFrame to store the tokens and their labels
            df = pd.DataFrame({"token": tokens, "label": labels})
            # Save to CSV
            output_file = output_file.replace(".xlsx", ".csv")
            df.to_csv(output_file, index=False)
        else:
            raise ValueError(f"Unsupported file format: {input_file}")

        df["cleaned_message"] = df["token"].apply(preprocess_amharic_text)

        # Save cleaned data to Excel
        if input_file.endswith(".xlsx") or input_file.endswith(".xls"):
            df.to_excel(output_file, index=False, engine="openpyxl")
        else:
            df.to_csv(output_file, index=False)

        logging.info(f"Cleaned data saved to {output_file}")
    except Exception as e:
        logging.error(f"Error during preprocessing: {e}")
