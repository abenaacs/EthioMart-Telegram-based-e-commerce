import shap
from transformers import AutoModelForTokenClassification, AutoTokenizer
import datasets


def interpret_model(model_dir, data_file):
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModelForTokenClassification.from_pretrained(model_dir)

    # Load a small dataset
    dataset = datasets.load_dataset("conll2003", split="validation[:10]")

    # Tokenize a sample
    inputs = tokenizer(
        dataset["tokens"], return_tensors="pt", padding=True, truncation=True
    )
    outputs = model(**inputs)

    # SHAP interpretation
    explainer = shap.Explainer(model)
    shap_values = explainer.shap_values(inputs["input_ids"])

    shap.summary_plot(
        shap_values, inputs["input_ids"], feature_names=tokenizer.get_vocab()
    )


if __name__ == "__main__":
    interpret_model(
        model_dir="./fine_tuned_model/",
        data_file="./processed/labeled_conll.txt",
    )
