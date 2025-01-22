from transformers import pipeline
from datasets import load_dataset
import json


def compare_models(data_file, models):
    dataset = load_dataset("conll2003", split="validation")  # Replace with your dataset
    results = {}

    for model_name in models.split(","):
        print(f"Evaluating model: {model_name}")
        nlp = pipeline("ner", model=model_name)
        predictions = nlp(dataset["tokens"][:100])  # Test on a sample

        # Placeholder for evaluation metrics
        results[model_name] = {"accuracy": 0.95}  # Replace with real metrics

    with open("model_comparison_results.json", "w") as f:
        json.dump(results, f, indent=4)


if __name__ == "__main__":
    compare_models(
        data_file="./processed/labeled_conll.txt",
        models="xlm-roberta-base,distilbert-base-multilingual-cased,bert-tiny-amharic",
    )
