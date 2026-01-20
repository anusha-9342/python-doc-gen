# Phase 2: Phase 2: Template Analysis and Data Mapping Strategy

⏱️ **Estimated Duration:** 4 days

---

## 🎯 Milestone 1: Template Placeholder Identification

### Task 1: Create a Sample Word Template with Placeholders

- [ ] **Status:** Not Started

**Description:**
Design a basic Word document template that includes a static header and specific text placeholders (e.g., `{{customer_name}}`, `{{product_id}}`, `{{date}}`) where dynamic content will be inserted.

**✅ Definition of Done:**
> A Microsoft Word document template is saved as a .docx file containing a static header and the exact text placeholders '{{customer_name}}', '{{product_id}}', and '{{date}}'.

**Concepts:** `Word template design` `placeholder conventions`

**📚 Resources:**
- 📖 [Dynamics and Smart Templates Best Practices for Word – Templafy ...](https://support.templafy.com/hc/en-us/articles/13782453408797-Dynamics-and-Smart-Templates-Best-Practices-for-Word)
- 🔗 [Power Automate Word Templates in SharePoint](https://www.iwmentor.com/pages/blog/power-automate-word-templates-in-sharepoint)
- 🔗 [Custom placeholders/tags for dynamic content in a Word template ...](https://stackoverflow.com/questions/6471409/custom-placeholders-tags-for-dynamic-content-in-a-word-template)
- 🎥 [Populate a Word Template with Power Automate | How to Tutorial ...](https://www.youtube.com/watch?v=vpo_U5Qf1ak)
- 🎥 [Automate Dynamic Document Creation with Power Automate and ...](https://www.youtube.com/watch?v=8PUFodSc5BY)
- 🔗 [Populating a Word Template for an Easy Win - Lindsay T Shelton](https://www.lindsaytshelton.com/blog/20250112populating_a_word_template_for_an_easy_win/)
- 💻 [DocxTemplater: C# library for generating DOCX documents with ...](https://github.com/Amberg/DocxTemplater)

---

### Task 2: Identify and Extract Placeholders from Template

- [ ] **Status:** Not Started

**Description:**
Write a Python script that opens the `template.docx` file, iterates through its paragraphs, and identifies all defined placeholders. Store these placeholders in a list.

**✅ Definition of Done:**
> The Python script successfully opens "template.docx", extracts all placeholders formatted as `{{placeholder_name}}` from its paragraphs, and stores these unique placeholders in a Python list named `placeholders_list`.

**Concepts:** `document parsing` `text search` `regular expressions (optional)`

**📚 Resources:**
- 💻 [ShayHill/docx2python: Extract docx headers, footers ... - GitHub](https://github.com/ShayHill/docx2python)
- 🎥 [Easily Create & Fill Word Templates in Python - YouTube](https://www.youtube.com/watch?v=u04Cq0aed_4)
- 🎥 [Automatically Fill Word Files with Python - YouTube](https://www.youtube.com/watch?v=3qjEPRmge8I)
- 💻 [Single figure not displayed after rendering although all others are ...](https://github.com/elapouya/python-docx-template/issues/368)
- 📖 [Instruction to export GPT-Generated text into Structured DOCX - GPT ...](https://community.openai.com/t/instruction-to-export-gpt-generated-text-into-structured-docx/655675)
- 📖 [DOCX - Apache POI - Ignition - Inductive Automation Forum](https://forum.inductiveautomation.com/t/docx-apache-poi/71426)

---

## 🎯 Milestone 2: Data-to-Template Mapping

### Task 1: Decide on Data Mapping Strategy

- [ ] **Status:** Not Started

**Description:**
Determine how the column headers from the spreadsheet will be mapped to the placeholders identified in the Word template. Implement the chosen strategy.

**✅ Definition of Done:**
> A Python dictionary or a loaded configuration file accurately defines the mapping from Word template placeholder keys to spreadsheet column headers, and this mapping is successfully loaded and accessible for use in the document generation logic.

**🤔 Decision Point:**
> How will you map the spreadsheet column headers to the placeholders in your Word template?

Options:
- **Direct Code Mapping**: Implement a Python dictionary directly in your script to map spreadsheet column names to template placeholder names (e.g., `{'Client Name': '{{customer_name}}'}`).
- **Configuration File (JSON/YAML)**: Create a separate configuration file (e.g., `mapping.json` or `mapping.yaml`) that defines the relationship between spreadsheet columns and template placeholders. Your script will read this file.
- **Convention-Based Mapping**: Assume that spreadsheet column headers directly correspond to placeholder names (e.g., a column 'Customer Name' maps to `{{Customer Name}}`). This requires careful naming in both the spreadsheet and template.

**Concepts:** `data mapping` `configuration management` `dynamic content linking`

**📚 Resources:**
- 🎥 [How to Automatically Create Word and PDF Documents from Excel ...](https://www.youtube.com/watch?v=V4_OZbpB-0o)
- 🎥 [Use Excel data to populate a template in Word - YouTube](https://www.youtube.com/watch?v=6zEUJfZcA9c)
- 🔗 [How to Generate Word Documents From Excel Data? | Learn Now!](https://perfectdoc.studio/inspiration/generate-word-documents-from-excel-data/)
- 🔗 [How to Populate Word Documents Using Power Automate?](https://perfectdoc.studio/inspiration/how-to-populate-word-document-template-using-power-automate/)
- 🎥 [Power Automate: How to populate a Word Template - YouTube](https://www.youtube.com/watch?v=1HyacOSm-6k)
- 🎥 [How to do Mail Merge in Power Automate (Full Tutorial) - YouTube](https://www.youtube.com/watch?v=lj9BA1fbBGI)
- 🔗 [python - Prompting script to replace placeholders in template file ...](https://stackoverflow.com/questions/9274202/prompting-script-to-replace-placeholders-in-template-file)
- 🎥 [Automate Dynamic Document Creation with Power Automate and ...](https://www.youtube.com/watch?v=8PUFodSc5BY)

---

## 📊 Progress

Track your progress by checking off tasks as you complete them!

When done with this phase, merge to `main` and move to `phase-3`.

---
*Generated by [RoadmapFlow](https://roadmapflow.com) 🚀*
