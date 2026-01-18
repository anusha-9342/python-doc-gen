# Phase 3: Phase 3: Dynamic Content Insertion & Document Generation

⏱️ **Estimated Duration:** 5 days

---

## 🎯 Milestone 1: Dynamic Content Insertion Logic

### Task 1: Implement Placeholder Replacement Function

- [ ] **Status:** Not Started

**Description:**
Write a Python function that takes a `python-docx` document object and a dictionary of placeholder-to-value mappings. This function should iterate through all paragraphs and replace placeholders with their corresponding values.

**✅ Definition of Done:**
> The Python function `replace_placeholders` successfully replaces all occurrences of placeholder strings found in a `python-docx` Document object's paragraphs with their corresponding values provided in a mapping dictionary when executed.

**Concepts:** `document modification` `text replacement` `iterating document elements`

**📚 Resources:**
- 💻 [python-docx-replace-text-and-retain-style.py · GitHub](https://gist.github.com/adejones/a6d42984f66ea9990d78974531863bee)
- 💻 [feature: replace scalar placeholders in template · Issue #99 · python ...](https://github.com/python-openxml/python-docx/issues/99)
- 🔗 [Populating MS Word Templates with Python - Practical Business ...](https://pbpython.com/python-word-template.html)
- 🎥 [Automatically Fill Word Files with Python - YouTube](https://www.youtube.com/watch?v=3qjEPRmge8I)
- 🎥 [Easily Create & Fill Word Templates in Python - YouTube](https://www.youtube.com/watch?v=u04Cq0aed_4)
- 🔗 [Python-Docx replacing texts with tables - Stack Overflow](https://stackoverflow.com/questions/78851220/python-docx-replacing-texts-with-tables)
- 🎥 [How to Automate Word Documents Using Python - YouTube](https://www.youtube.com/watch?v=H8Ars15wGRM)
- 🔗 [Instruction to export GPT-Generated text into Structured DOCX - GPT ...](https://community.openai.com/t/instruction-to-export-gpt-generated-text-into-structured-docx/655675)

---

### Task 2: Handle Header Content Preservation

- [ ] **Status:** Not Started

**Description:**
Modify the placeholder replacement function to ensure that the static header of the document template remains untouched, or is dynamically updated only if placeholders exist within it and are explicitly part of the mapping.

**✅ Definition of Done:**
> When the placeholder replacement function is executed, any static content in the document header remains unchanged, and placeholders within the header are only replaced if they are present in the provided data mapping, otherwise they remain untouched.

**Concepts:** `document sections` `header/footer handling` `conditional replacement`

**📚 Resources:**
- 💻 [open-xml-templating/docxtemplater: Generate docx, pptx ... - GitHub](https://github.com/open-xml-templating/docxtemplater)
- 🔗 [c# - Replacing Content Controls in OpenXML - Stack Overflow](https://stackoverflow.com/questions/3448297/replacing-content-controls-in-openxml)
- 🎥 [Populate a Word Template table Dynamically with Power Automate ... - YouTube](https://www.youtube.com/watch?v=ke6cUWzhqXo)
- 🎥 [Automate Dynamic Document Creation with Power Automate and ... - YouTube](https://www.youtube.com/watch?v=8PUFodSc5BY)
- 🎥 [Power Automate: How to populate a Word Template - YouTube](https://www.youtube.com/watch?v=1HyacOSm-6k)
- 🎥 [How to Automate Word Documents Using Python - YouTube](https://www.youtube.com/watch?v=H8Ars15wGRM)
- 🔗 [python - Replace image in Word docx format - Stack Overflow](https://stackoverflow.com/questions/71562597/replace-image-in-word-docx-format)

---

## 🎯 Milestone 2: Batch Document Generation

### Task 1: Develop a Document Generation Loop

- [ ] **Status:** Not Started

**Description:**
Integrate the data reading, placeholder identification, mapping, and replacement logic into a main script. The script should iterate through each row of your spreadsheet, generate a new Word document from the template, populate it with data from the current row, and save it with a unique name.

**✅ Definition of Done:**
> The main script successfully generates and saves N uniquely named Word documents, where N is the number of data rows in the input spreadsheet, and each generated document uses data from its corresponding spreadsheet row to fill all placeholders from the template.

**Concepts:** `iteration` `file I/O` `automation scripts`

**📚 Resources:**
- 🎥 [How to Automate Word Documents Using Python - YouTube](https://www.youtube.com/watch?v=H8Ars15wGRM)
- 🎥 [Generate MS Word documents in bulk based on an Excel list using ...](https://www.youtube.com/watch?v=Zy9sx4GvjUY)
- 🔗 [excel - Using docxtpl library in Python, how to generate complex ...](https://stackoverflow.com/questions/74878870/using-docxtpl-library-in-python-how-to-generate-complex-word-documents-from-mul)
- 🎥 [Use Excel data to populate a template in Word - YouTube](https://www.youtube.com/watch?v=6zEUJfZcA9c)
- 🎥 [How to Automatically Create Word and PDF Documents from Excel ...](https://www.youtube.com/watch?v=V4_OZbpB-0o)
- 🔗 [Video Automations from Templates, Mail Merge Style - Brainstorm ...](https://discuss.kde.org/t/video-automations-from-templates-mail-merge-style/1721)
- 📖 [Data Mapping Tools: MapForce | Altova](https://www.altova.com/mapforce)

---

## 📊 Progress

Track your progress by checking off tasks as you complete them!

When done with this phase, merge to `main` and move to `phase-4`.

---
*Generated by [RoadmapFlow](https://roadmapflow.com) 🚀*
