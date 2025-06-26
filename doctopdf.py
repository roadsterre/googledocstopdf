import os
import re
import requests
from pdfwriter import text_to_pdf  # Make sure this module exists and works

def id_extraction(url):
    match = re.search(r"/d/([a-zA-Z0-9-_]+)", url)
    if match:
        return match.group(1)
    else:
        raise ValueError("❌ Invalid Google Docs URL.")

# Step 1: Get Google Docs ID
user_link = input("Paste your Google Docs link: ").strip()
doc_id = id_extraction(user_link)
print(f"✅ Extracted Doc ID: {doc_id}")

# Step 2: Export as text
doc_url = f"https://docs.google.com/document/d/{doc_id}/export?format=txt"
response = requests.get(doc_url)

if response.status_code != 200:
    print(f"❌ Failed to access document. Status code: {response.status_code}")
    exit()

text = response.text
text = text.lstrip('\ufeff')  # Remove BOM if present

print("✅ Document downloaded successfully.")

# Step 3: Split into chapters using regex (e.g., "1. Chapter Title")
# Matches start of lines like "1. Something", "2. Another", etc.
raw_chapters = re.split(r"(?=^\d+\.\s)", text, flags=re.MULTILINE)
chapters = [ch.strip() for ch in raw_chapters if ch.strip()]

# Step 4: Clean and organize chapters
chapter_data = []
for ch in chapters:
    lines = ch.splitlines()
    if not lines:
        continue

    title_line = lines[0].strip()
    content = "\n".join(lines[1:]).strip()

    # Fallback to index if chapter number not detected
    number_match = re.match(r"(\d+)", title_line)
    ch_num = int(number_match.group(1)) if number_match else len(chapter_data) + 1

    chapter_data.append((ch_num, title_line, content))

# Debug (optional)
# print("DEBUG: Chapter Data")
# for ch_num, title, body in chapter_data:
#     print(f"\n[CHAPTER {ch_num}] {title}\n---\n{body[:100]}...\n")

# Step 5: Ask where to save PDFs
output_dir = input("Enter directory to save PDFs (leave blank for current folder): ").strip()
if output_dir:
    os.makedirs(output_dir, exist_ok=True)
else:
    output_dir = "."

# Step 6: Save each chapter as a PDF
for ch_num, title, body in sorted(chapter_data):
    if not title.strip():
        print(f"⚠️ Skipping chapter {ch_num} due to missing title.")
        continue

    # Sanitize title for filename
    # Sanitize title for safe filenames
                          # Optional: limit length
    
    safe_title = re.sub(r'[\\/*?:"<>|\n\r]', "", title)  # Remove invalid characters
    safe_title = re.sub(r'^\d+(\.\d+)*\.?\s*', '', safe_title).strip()  # Remove chapter number and dot
    safe_title = safe_title[:80]  # Limit length if needed



    pdf_filename = f"{safe_title}.pdf"
    pdf_path = os.path.join(output_dir, pdf_filename)

    # Write to temporary text file
    with open("temp_chapter.txt", "w", encoding="utf-8") as f:
        f.write(f"{title}\n\n{body}")

    # Convert text to PDF
    text_to_pdf("temp_chapter.txt", pdf_path)
    print(f"✅ Saved: {pdf_filename}")

# Step 7: Cleanup
os.remove("temp_chapter.txt")
print(f"\n✅ All chapters exported as PDFs to: {os.path.abspath(output_dir)}")
