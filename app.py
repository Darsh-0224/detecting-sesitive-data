import re
import cv2
import pytesseract

# Set Tesseract OCR path (Windows users only)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Medical Sensitive Data Patterns
MEDICAL_PATTERNS = {
    "Medical Record Number": r"\bMRN\d{6,10}\b",  # Example format: MRN123456
    "Disease": r"\b(HIV|Cancer|Diabetes|Alzheimer's|Tuberculosis|Schizophrenia|Hypertension|COVID-19|Asthma|Parkinson's|Stroke|Epilepsy)\b",
    "Medication": r"\b(Prozac|Morphine|Oxycodone|Cisplatin|Amoxicillin|Insulin|Ibuprofen|Paracetamol|Warfarin|Aspirin|Metformin|Atorvastatin)\b",
    "Medical Procedure": r"\b(CT Scan|MRI|Dialysis|Chemotherapy|Biopsy|Transplant|Angioplasty|Endoscopy|Ultrasound|X-Ray|Radiation Therapy|Surgery)\b"
}

# Function to extract text from an image using OCR
def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    text = pytesseract.image_to_string(gray)  # Perform OCR
    return text.strip()

# Function to detect sensitive medical data
def detect_sensitive_medical_data(text):
    detected = []
    for label, pattern in MEDICAL_PATTERNS.items():
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            detected.append((label, matches))
    return detected

# Test with an image
image_path = r"D:\Web Dev\123456\nlp\dataimage2.png"  # Update with your image path
extracted_text = extract_text_from_image(image_path)

if extracted_text:
    print(f"Extracted Text:\n{extracted_text}\n")
    detected_entities = detect_sensitive_medical_data(extracted_text)

    if detected_entities:
        print("Sensitive Medical Data Found:")
        for label, matches in detected_entities:
            print(f"  - {label}: {matches}")
    else:
        print("No sensitive medical data detected.")
else:
    print("No text extracted from the image.")
