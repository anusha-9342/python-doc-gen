from docx import Document

def replace_placeholders(doc, mappings):
    for paragraph in doc.paragraphs:
        for placeholder, value in mappings.items():
            if placeholder in paragraph.text:
                paragraph.text = paragraph.text.replace(placeholder, str(value))

  
    for paragraph in doc.paragraphs:
        # Step 3: store original paragraph text
        updated_text = paragraph.text

        # Step 4: apply all replacements on the temporary text
        for placeholder, value in mappings.items():
            updated_text = updated_text.replace(placeholder, str(value))

        # Step 5: clear existing runs and add one new run
        if updated_text != paragraph.text:
            paragraph.clear()
            paragraph.add_run(updated_text)

