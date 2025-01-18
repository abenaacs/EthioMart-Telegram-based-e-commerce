import json
import os
import logging


def convert_to_conll_format(input_file, output_file):
    """Convert labeled data to CoNLL format."""
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    conll_lines = []
    for line in lines:
        tokens = line.strip().split()
        for token in tokens:
            # Assign 'O' by default; you can add specific rules for labeling
            conll_lines.append(f"{token} O\n")
        conll_lines.append("\n")  # Add a blank line to separate sentences

    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(conll_lines)

    return output_file


def label_images(input_folder, output_file):
    """Generate default labels for images."""
    labels = {}
    for img_name in os.listdir(input_folder):
        labels[img_name] = {"label": "unlabeled", "bounding_box": []}

    with open(output_file, "w") as f:
        json.dump(labels, f, indent=4)

    logging.info(f"Image labels saved to {output_file}")
