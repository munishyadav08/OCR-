import easyocr
import json
import os
import cv2

# Ensure output directory exists
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

def extract_text(image_path):
    """Extracts text from an image using EasyOCR"""
    if not os.path.exists(image_path):
        print(f"❌ Error: Image file '{image_path}' not found!")
        return ""

    # Load and preprocess image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Extract text using EasyOCR
    text_results = reader.readtext(gray, detail=0)

    # Join text results into a single string
    extracted_text = " ".join(text_results)

    print("\n🔍 Extracted Text:\n", extracted_text)  # Debugging output

    return extracted_text

def parse_text(extracted_text):
    """Parses extracted text into structured JSON format"""
    if not extracted_text:
        return {}

    # Example parsing logic (Modify based on your actual text structure)
    structured_data = {
        "raw_text": extracted_text,  # Store raw text
        "keywords": extracted_text.split()[:5]  # Extract first 5 words as sample data
    }

    print("\n📌 Parsed Data Structure:\n", structured_data)  # Debugging output

    return structured_data

def save_to_json(data, output_file="output/extracted_data.json"):
    """Saves extracted data into a JSON file"""
    if not data or all(value is None for value in data.values()):
        print("⚠️ No valid data extracted! JSON file will not be saved.")
        return

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"✅ JSON saved at {output_file}")
    except Exception as e:
        print(f"❌ Error saving JSON: {e}")

def main():
    image_path = "images/Sample_form.jpg"  # Update with actual image path
    extracted_text = extract_text(image_path)

    if not extracted_text.strip():
        print("⚠️ No text detected! JSON file will not be saved.")
        return

    structured_data = parse_text(extracted_text)

    save_to_json(structured_data)

if __name__ == "__main__":
    main()
