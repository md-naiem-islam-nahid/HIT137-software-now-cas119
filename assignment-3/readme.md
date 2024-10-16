# **Translator Application Documentation**

## **Overview**

This Translator Application is a simple GUI-based translation tool built using Python's Tkinter for the GUI and Hugging Face's `MarianMTModel` for the translation functionality. It allows users to translate text between different languages by leveraging pre-trained machine translation models.

---

## **Table of Contents**
1. [Installation Requirements](#installation-requirements)
2. [How to Run the Application](#how-to-run-the-application)
3. [Features](#features)
4. [OOP Implementation](#oop-implementation)
5. [File Structure](#file-structure)

---

## **Installation Requirements**

To run the Translator Application, you need to have Python installed (preferably version 3.6+). Additionally, the following libraries need to be installed in your environment.

### **Packages to Install**

1. **Tkinter** (for the GUI)
   - On Linux: 
     ```bash
     sudo apt-get install python3-tk
     ```
   - On Windows/macOS, Tkinter usually comes pre-installed with Python.
   
2. **Transformers** (for Hugging Face translation models)
   ```bash
   pip install transformers
   ```

3. **PyTorch** (for loading the MarianMT translation model)
   - For most systems (CPU-based):
     ```bash
     pip install torch torchvision torchaudio
     ```
   - For specific setups (CUDA/GPU), visit [PyTorch installation](https://pytorch.org/get-started/locally/) for detailed instructions.

4. **SentencePiece** (required for tokenization)
   ```bash
   pip install sentencepiece
   ```

5. **Sacremoses** (optional for tokenization post-processing)
   ```bash
   pip install sacremoses
   ```

6. **Huggingface-hub** (for managing model files and configurations)
   ```bash
   pip install huggingface-hub
   ```

### **Complete Installation Command**

```bash
pip install transformers torch torchvision torchaudio sentencepiece sacremoses huggingface-hub
```

---

## **How to Run the Application**

Once all the required packages are installed, you can run the Translator Application by following these steps:

### **Step 1: Download/Clone the Repository**

- If you have the repository on your local machine, navigate to the folder where the `app.py` file is located.

### **Step 2: Run the Application**

- Open a terminal or command prompt in the project directory.
- Run the following command:

```bash
python app.py
```

This will launch the Translator Application's GUI.

### **Step 3: Using the Application**

1. Input the text you want to translate.
2. Click on the "Translate" button.
3. The translated text will be displayed in the designated area.

---

## **Features**

1. **Simple GUI**: The application uses a Tkinter GUI, allowing users to input text and receive translations.
2. **Multiple Language Translation**: The app uses Hugging Face’s `MarianMTModel` to translate between various languages.
3. **Error Handling & Logging**: The app includes decorators for logging translation activity and handling errors, ensuring a smooth user experience.

---

