# 📝 OCR - Optical Character Recognition

This repository contains a **Python-based OCR (Optical Character Recognition)** script using **EasyOCR** to extract structured data from images of forms and store it in a database. The extracted data is formatted as **JSON** for easy integration.

---

## 📌 Features

- ✅ **Extracts text** from images using **EasyOCR**.
- 📄 **Converts extracted text** into structured **JSON format**.
- 🗄️ **Stores extracted data** in a **database**.
- 🖼️ **Includes a sample image** for testing and demonstration.

---

## 🛠️ Setup Instructions

### ✅ Prerequisites

To run this project, make sure you have the following installed:

- 🐍 **Python** (>=3.8)
- 📚 **EasyOCR**
- 📦 Other required Python libraries (install via `requirements.txt`)

### 📥 Installation

Follow these steps to set up the project:

1. **Clone this repository**:
   ```bash
   git clone https://github.com/munishyadav08/OCR-.git
   cd OCR-

2. **Install dependencies**:
'''pip install -r requirements.txt

3.**Install Easy-OCR**:
pip install easyocr

### 🚀 Usage

To use this OCR script, follow these steps:

Run the OCR script on an image:

python ocr_script.py --image sample_form.jpg

-The script will process the image and output the extracted text in JSON format.

-Modify the script as needed to process different types of documents.

### 🗄️ Database Storage

This project supports storing extracted OCR data in a database. Follow these steps:

Configure the database connection:

-Open the config.py file.
-Update the database credentials (if req) .

Run the database storage script:

python store_data.py

-Verify the data in the database using any database management tool.
-Modify the database schema (if necessary) to match different data structures.





