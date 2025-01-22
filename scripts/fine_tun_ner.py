from transformers import (
    AutoModelForTokenClassification,
    AutoTokenizer,
    Trainer,
    TrainingArguments,
)
from datasets import load_dataset, load_metric
import os


def fine_tune_ner(
    data_file,
    output_dir,
    model_name_or_path,
    num_train_epochs,
    learning_rate,
    batch_size,
):
    # Load dataset
    dataset = load_dataset("conll2003", split="train")  # Replace with your dataset

    # Load model and tokenizer
    model = AutoModelForTokenClassification.from_pretrained(
        model_name_or_path, num_labels=len(dataset.features["ner_tags"].feature.names)
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)

    # Tokenize data
    def tokenize_and_align_labels(examples):
        tokenized_inputs = tokenizer(
            examples["tokens"], truncation=True, is_split_into_words=True
        )
        labels = []
        for i, label in enumerate(examples["ner_tags"]):
            word_ids = tokenized_inputs.word_ids(batch_index=i)
            label_ids = [
                -100 if word_id is None else label[word_id] for word_id in word_ids
            ]
            labels.append(label_ids)
        tokenized_inputs["labels"] = labels
        return tokenized_inputs

    tokenized_dataset = dataset.map(tokenize_and_align_labels, batched=True)

    # Training arguments
    args = TrainingArguments(
        output_dir=output_dir,
        evaluation_strategy="epoch",
        learning_rate=learning_rate,
        per_device_train_batch_size=batch_size,
        num_train_epochs=num_train_epochs,
        save_strategy="epoch",
        logging_dir=f"{output_dir}/logs",
    )

    trainer = Trainer(
        model=model,
        args=args,
        train_dataset=tokenized_dataset,
    )

    trainer.train()


if __name__ == "__main__":
    fine_tune_ner(
        data_file="./processed/labeled_conll.txt",
        output_dir="./fine_tuned_model/",
        model_name_or_path="xlm-roberta-base",
        num_train_epochs=3,
        learning_rate=5e-5,
        batch_size=16,
    )
