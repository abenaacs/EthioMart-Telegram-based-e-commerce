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
