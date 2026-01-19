=Document()
document.add_heading('My Heading') 
document.add_paragraph('This is a sample paragraph in the document.')
document.save('MyDocument.docx')

import pandas as pd
df=pd.read_csv('datasets/sample.csv')