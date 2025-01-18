## Notebook README

# EthioMart Jupyter Notebooks

This folder contains Jupyter notebooks that demonstrate the pipeline step-by-step. The notebooks are designed for experimentation, visualization, and debugging.

### Notebooks

1. **`pipeline_notebook.ipynb`**:
   - Implements the entire pipeline interactively.
   - Includes explanations, visualizations, and intermediate outputs.

### How to Use

1. **Set Up the Environment**:

   - Ensure the virtual environment is activated:
     ```bash
     source env/bin/activate  # For Windows: .\env\Scripts\activate
     ```
   - Install Jupyter:
     ```bash
     pip install jupyter
     ```

2. **Run the Notebook**:

   ```bash
   jupyter notebook notebooks/pipeline_notebook.ipynb
   ```

3. **Notebook Structure**:

   - **Data Ingestion**: Fetches Telegram data and displays samples.
   - **Preprocessing**: Cleans and tokenizes raw messages.
   - **Conversion**: Formats data into CoNLL format.

4. **Outputs**:
   - Visualize the structured and processed data.
   - Validate the outputs at each stage.

---
