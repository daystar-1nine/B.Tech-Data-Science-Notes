import os
import json
import re
import markdown

BASE_DIR = r"S:\B.Tech Data Science Notes"
DATA_FILE = os.path.join(BASE_DIR, "notes_data.js")

EXACT_TITLES = {
    # DBMS Module 1
    "1_DBMS_Architecture.md": "Database Management System (DBMS) Architecture",
    "2_Data_Abstraction.md": "Data Abstraction & 3-Level Schema Architecture",
    "3_Data_Independence.md": "Logical & Physical Data Independence",
    "4_ER_Model.md": "Entity Relationship (ER) Model",
    "5_Entity_Types_and_Sets.md": "Entity Types & Entity Sets",
    "6_Attributes_and_Keys.md": "Attributes & Key Constraints",
    "7_Relationship_Types_and_Sets.md": "Relationship Types & Relationship Sets",
    "8_Converting_ER_to_Tables.md": "Converting ER Model to Relational Tables",
    "9_Self_Learning_ORDBMS.md": "Object-Relational DBMS (ORDBMS) (Self-Learning)",
    
    # DBMS Module 2
    "1_Introduction_to_Relational_Algebra.md": "Introduction to Relational Algebra",
    "2_Selection_Operation.md": "Selection Operation (σ)",
    "3_Projection_Operation.md": "Projection Operation (π)",
    "4_Union_Operation.md": "Union Operation (∪)",
    "5_Intersection_Operation.md": "Intersection Operation (∩)",
    "6_Cartesian_Product_Operation.md": "Cartesian Product Operation (×)",
    "7_Join_Operation.md": "Join Operations (⋈)",
    "8_Self_Learning_Relational_Calculus.md": "Relational Calculus (Self-Learning)",

    # DBMS Module 3
    "1_SQL_Standards.md": "SQL Standards & Core Concepts",
    "2_DDL_Commands.md": "Data Definition Language (DDL) Commands",
    "3_Set_Operations.md": "Set Operations in SQL",
    "4_Aggregate_Functions.md": "Aggregate Functions in SQL",
    "5_NULL_Values.md": "NULL Values & 3-Valued Logic",
    "6_DML_Commands.md": "Data Manipulation Language (DML) Commands",
    "7_DCL_Commands.md": "Data Control Language (DCL) Commands",
    "8_Complex_Retrieval_Queries_using_GROUP_BY.md": "Complex Retrieval Queries using GROUP BY",
    "9_Recursive_Queries.md": "Recursive Queries & Common Table Expressions (CTE)",
    "10_Nested_Queries.md": "Nested Queries & Subqueries",
    "11_Self_Learning_Triggers.md": "Database Triggers (Self-Learning)",
    "12_Self_Learning_Procedures.md": "Stored Procedures (Self-Learning)",
    "13_Self_Learning_Functions.md": "Database Functions (Self-Learning)",
    "14_Self_Learning_Packages.md": "PL/SQL Packages (Self-Learning)",
    "15_Self_Learning_Embedded_SQL.md": "Embedded SQL (Self-Learning)",

    # Data Structures Module 1
    "1_Concept_of_ADT.md": "Concept of Abstract Data Types (ADT)",
    "2_Types_of_Data_Structures.md": "Types of Data Structures: Linear & Non-Linear",
    "3_Operations_on_Data_Structures.md": "Operations on Data Structures",
    "4_Arrays_Multi_Dimensional_Arrays.md": "Arrays, Multidimensional Arrays & Pointers",
    "5_String_Manipulation.md": "String Manipulation Operations",
    "6_Self_Learning_Structures_with_Pointers.md": "Self-Referential Structures with Pointers (Self-Learning)",

    # Data Structures Module 2
    "A1_Stack_ADT_Operations_Array_Implementation.md": "Stack ADT, Operations & Array Implementation",
    "A2_Stack_Applications_Parentheses.md": "Stack Applications: Well-Formedness of Parentheses",
    "A3_Stack_Infix_Postfix_Recursion.md": "Infix to Postfix Conversion & Recursion",
    "B1_Queue_ADT_Operations_Array_Implementation.md": "Queue ADT, Operations & Array Implementation",
    "B2_Queue_Types_Circular_Priority.md": "Queue Types: Circular & Priority Queues",
    "B3_Deque_Introduction.md": "Double-Ended Queue (Deque) Introduction",
    "B4_Queue_Applications.md": "Applications of Queues",
    "8_Self_Learning_Stack_Queue_Structure.md": "Stack & Queue Implementation using Structures (Self-Learning)",

    # Data Structures Module 3
    "1_Introduction_to_Linked_List.md": "Introduction to Linked Lists",
    "2_Linked_List_vs_Array.md": "Linked Lists vs. Arrays Comparison",
    "3_Types_of_Linked_List.md": "Types of Linked Lists",
    "4_Operations_on_Singly_Linked_List.md": "Operations on Singly Linked List",
    "5_Operations_on_Doubly_Linked_List.md": "Operations on Doubly Linked List",
    "6_Stack_using_Singly_Linked_List.md": "Stack Implementation using Singly Linked List",
    "7_Queue_using_Singly_Linked_List.md": "Queue Implementation using Singly Linked List",
    "8_Self_Learning_Polynomial_Representation_Addition.md": "Polynomial Representation & Addition (Self-Learning)",

    # MPCA Module 1
    "1_Intro_Comp_Org_Arch.md": "Computer Organization vs. Architecture",
    "2_Von_Neumann_Model.md": "Von Neumann Computer Model",
    "3_Performance_Measures.md": "CPU Performance Measures",
    "4_Architecture_8086_Family.md": "Architecture of 8086 Microprocessor Family",
    "5_8086_Instruction_Set.md": "8086 Instruction Set Architecture",
    "6_Addressing_Modes_8086.md": "Addressing Modes of 8086",
    "7_Self_Learning_Basic_Organization_of_Computer.md": "Basic Organization of Computer (Self-Learning)",
    "8_Self_Learning_Block_Level_Description.md": "Block-Level Description of Functional Units (Self-Learning)",
    "9_Self_Learning_Evolution_of_Computers.md": "Evolution of Computers (Self-Learning)",

    # MPCA Module 2
    "1_CPU_Architecture.md": "CPU Architecture & Register Organization",
    "2_Instruction_Formats.md": "Instruction Formats & Addressing",
    "3_Basic_Instruction_Cycle_Interrupt.md": "Basic Instruction Cycle & Interrupt Servicing",
    "4_Control_Unit.md": "Control Unit Architecture & Hardwired/Microprogrammed Control",
    "5_Microinstruction_Sequencing_Execution.md": "Microinstruction Sequencing & Execution",
    "6_Micro_Operations.md": "Register Transfer & Micro-Operations",
    "7_Parallel_Processing_Concepts.md": "Parallel Processing Concepts",
    "8_Flynn_Classification.md": "Flynn's Classification of Computers",
    "9_Instruction_Pipelining.md": "Instruction Pipelining Principles",
    "10_Pipeline_Hazards.md": "Pipeline Hazards & Resolution",
    "11_Self_Learning_Instruction_Interpretation_Sequencing.md": "Instruction Interpretation & Sequencing (Self-Learning)",
    "12_Self_Learning_Concepts_of_Nano_Programming.md": "Concepts of Nano-Programming (Self-Learning)",

    # MPCA Module 3
    "1_8086_CPU_Architecture.md": "8086 CPU Architecture & Internal Registers",
    "2_Programmers_Model_of_8086.md": "Programmer's Model of 8086",
    "3_Functional_Pin_Diagram_of_8086.md": "Functional Pin Diagram & Signals of 8086",
    "4_Memory_Segmentation_in_8086.md": "Memory Segmentation in 8086",
    "5_Memory_Banking_in_8086.md": "Memory Banking in 8086",
    "6_8086_in_Minimum_Mode.md": "8086 Microprocessor in Minimum Mode",
    "7_8086_in_Maximum_Mode.md": "8086 Microprocessor in Maximum Mode",
    "8_Minimum_Mode_Timing_Diagrams.md": "Minimum Mode Timing Diagrams",
    "9_Maximum_Mode_Timing_Diagrams.md": "Maximum Mode Timing Diagrams",
    "10_Self_Learning_De_multiplexing_of_Address_Data_Bus.md": "De-multiplexing of Address/Data Bus (Self-Learning)",
    "11_Self_Learning_Interrupt_Structure_and_its_Servicing.md": "Interrupt Structure & Servicing in 8086 (Self-Learning)",

    # Question Banks
    "2M.md": "2-Mark Questions & Answers",
    "3M.md": "3-Mark Questions & Answers",
    "5M.md": "5-Mark Questions & Answers",
    "10M.md": "10-Mark Questions & Answers"
}

def get_clean_title(filename, content):
    fn = os.path.basename(filename)
    if fn in EXACT_TITLES:
        return EXACT_TITLES[fn]

    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    t = title_match.group(1).strip() if title_match else fn.replace('.md', '').replace('_', ' ')
    t = re.sub(r'^#+\s*', '', t).strip()
    t = re.sub(r'^Topic\s*[:\-]\s*', '', t, flags=re.IGNORECASE).strip()
    t = re.sub(r'^(?:[A-Za-z]\d{1,2}|\d{1,2})[\._\s\-]+\s*', '', t).strip()
    return t

def parse_markdown_file(filepath):
    rel_path = os.path.relpath(filepath, BASE_DIR).replace('\\', '/')
    pdf_rel_path = f"PDF_Notes/{rel_path[:-3]}.pdf"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(filepath)

    parts = rel_path.split('/')
    semester = parts[0] if len(parts) > 0 and 'Semester' in parts[0] else "General"
    subject = parts[1] if len(parts) > 1 else "General"
    
    # Check if this is a Question & Answer Bank file
    is_qa_file = (
        filename.lower().endswith('m.md') or 
        'module_' in rel_path.lower() and '_qa' in rel_path.lower() or
        'questions' in content.lower() and 'answers' in content.lower() and '2-mark' in content.lower()
    )

    if is_qa_file:
        module = "Question & Answers Bank"
    else:
        module = "General"
        for part in parts:
            if re.match(r'^Module\s*\d+$', part, re.IGNORECASE):
                module = part.title()
                break

    title = get_clean_title(filename, content)

    # Extract Definition block
    def_match = re.search(r'>\s*📌\s*\*\*Definition to Remember\*\*\s*\n>\s*(.+?)(?=\n\n|\n>|\n---|\Z)', content, re.DOTALL)
    definition = def_match.group(1).replace('\n>', ' ').strip() if def_match else ""

    # Extract Must Write Points
    must_write_match = re.search(r'>\s*⭐\s*\*\*Must-Write Points[^\n]*\*\*\s*\n((?:>\s*.*?\n)+)', content)
    must_write = []
    if must_write_match:
        lines = must_write_match.group(1).split('\n')
        for line in lines:
            cleaned = re.sub(r'^>\s*\d+\.\s*', '', line).strip()
            if cleaned and not cleaned.startswith('>'):
                must_write.append(cleaned)

    # Extract Quick Recall
    quick_match = re.search(r'>\s*⚡\s*\*\*Quick Recall\*\*\s*\n>\s*`?(.+?)`?\s*(?=\n|\Z)', content)
    quick_recall = quick_match.group(1).strip() if quick_match else ""

    html = markdown.markdown(content, extensions=['tables', 'fenced_code', 'nl2br', 'sane_lists'])

    return {
        "id": rel_path.replace('/', '-').replace('.md', ''),
        "relPath": rel_path,
        "pdfPath": check_pdf_exists(pdf_rel_path, rel_path),
        "filename": filename,
        "semester": semester,
        "subject": subject,
        "module": module,
        "title": title,
        "content": content,
        "html": html,
        "definition": definition,
        "mustWrite": must_write,
        "quickRecall": quick_recall
    }

def check_pdf_exists(pdf_rel_path, rel_path):
    full_pdf = os.path.join(BASE_DIR, pdf_rel_path.replace('/', '\\'))
    if os.path.exists(full_pdf):
        return pdf_rel_path

    # Secondary check inside PDF_Notes folder without Semester X prefix
    alt_pdf = os.path.join(BASE_DIR, "PDF_Notes", rel_path.replace('/', '\\')[:-3] + ".pdf")
    if os.path.exists(alt_pdf):
        return "PDF_Notes/" + rel_path[:-3] + ".pdf"

    return ""

def get_file_sort_key(item):
    filename = item['filename']
    
    # 1. Module 1, Module 2, Module 3 come first
    if item['module'].startswith('Module'):
        mod_num = int(re.search(r'\d+', item['module']).group()) if re.search(r'\d+', item['module']) else 1
        mod_order = mod_num
    else:
        # Question & Answers Bank placed at end of subject
        mod_order = 99

    # Question Bank mark sorting (2M < 3M < 5M < 10M)
    q_match = re.search(r'(\d+)M\.md', filename, re.IGNORECASE) or re.search(r'(\d+)\s*Mark', filename, re.IGNORECASE)
    mark_num = int(q_match.group(1)) if q_match else 0

    # Letter-number prefixes (A1_, A2_, B1_, B2_)
    alpha_num_match = re.match(r'^([A-Z])(\d+)_', filename, re.IGNORECASE)
    if alpha_num_match:
        section_idx = ord(alpha_num_match.group(1).upper()) - ord('A')
        topic_num = int(alpha_num_match.group(2))
        return (item['semester'], item['subject'], mod_order, 0, section_idx, topic_num, mark_num, filename)

    # Standard numeric prefixes (1_, 2_, 3_, 8_)
    num_match = re.match(r'^(\d+)_', filename)
    if num_match:
        num = int(num_match.group(1))
        section_idx = 2 if num == 8 and 'Self_Learning_Stack_Queue' in filename else 0
        return (item['semester'], item['subject'], mod_order, 0, section_idx, num, mark_num, filename)

    return (item['semester'], item['subject'], mod_order, 1, 0, 0, mark_num, filename)

def main():
    items = []
    for root, dirs, files in os.walk(BASE_DIR):
        if '.git' in dirs: dirs.remove('.git')
        if 'PDF_Notes' in dirs: dirs.remove('PDF_Notes')
        if '.github' in dirs: dirs.remove('.github')

        for file in files:
            if file.endswith('.md') and not file.lower().startswith('readme'):
                full_path = os.path.join(root, file)
                items.append(parse_markdown_file(full_path))

    items.sort(key=get_file_sort_key)

    js_code = "window.NOTES_DATA = " + json.dumps(items, indent=2, ensure_ascii=False) + ";"
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        f.write(js_code)

    print(f"Successfully generated notes_data.js with Question & Answers Bank separation for {len(items)} files!")

if __name__ == "__main__":
    main()
