from docx import Document
document=Document()
document.add_heading('My Heading') 
document.add_paragraph('This is a sample paragraph in the document.')
document.save('MyDocument.docx')