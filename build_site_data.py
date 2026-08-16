import os
import json
import re
import markdown

BASE_DIR = r"S:\B.Tech Data Science Notes"
DATA_FILE = os.path.join(BASE_DIR, "notes_data.js")

MODULE_TITLES = {
    "DBMS": {
        "Module 1": "Architecture & ER Model",
        "Module 2": "Relational Algebra & Calculus",
        "Module 3": "SQL & Advanced Queries",
        "Module 4": "Relational Database Design",
        "Module 5": "Query Optimization & Concurrency",
        "Module 6": "Foundations of IBM Db2"
    },
    "Data Structure": {
        "Module 1": "ADT & Arrays",
        "Module 2": "Stacks & Queues",
        "Module 3": "Linked Lists",
        "Module 4": "Trees",
        "Module 5": "Graphs",
        "Module 6": "Sorting & Searching"
    },
    "MPCA": {
        "Module 1": "Architecture & Organization",
        "Module 2": "CPU & Pipelining",
        "Module 3": "8086 Microprocessor",
        "Module 4": "Memory & Peripherals Interfacing",
        "Module 5": "80386DX & Pentium Processor",
        "Module 6": "Pentium 4 & ARM Processor"
    }
}

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

    # DBMS Module 4
    "1_First_Normal_Form_1NF.md": "First Normal Form (1NF)",
    "2_Second_Normal_Form_2NF.md": "Second Normal Form (2NF)",
    "3_Third_Normal_Form_3NF.md": "Third Normal Form (3NF)",
    "4_Boyce_Codd_Normal_Form_BCNF.md": "Boyce-Codd Normal Form (BCNF)",
    "5_Algorithm_for_Decomposition_Using_Functional_Dependencies.md": "Algorithm for Decomposition Using Functional Dependencies",
    "6_Decomposition_Using_Multivalued_Attribute.md": "Decomposition Using Multivalued Attribute (4NF)",
    "7_Self_Learning_NoSQL_Data_Models.md": "NoSQL Data Models (Self-Learning)",

    # DBMS Module 5
    "1_Query_Optimization_Relational_Expressions.md": "Query Optimization & Relational Expressions",
    "2_Estimating_Statistics_and_Choice_of_Evaluation_Plan.md": "Estimating Statistics & Choice of Evaluation Plan",
    "3_Transaction_Concept_and_ACID_Properties.md": "Transaction Concept & ACID Properties",
    "4_Serializability_and_Concurrency_Control.md": "Serializability & Concurrency Control",
    "5_Lock_Based_Protocols_and_Multiple_Granularity.md": "Lock-Based Protocols & Multiple Granularity",
    "6_Insertion_Deletion_and_Predicate_Reads.md": "Insertion-Deletion & Predicate Reads (Phantoms)",
    "7_Timestamp_and_Validation_Based_Protocols.md": "Timestamp & Validation-Based Protocols",
    "8_Log_Based_Recovery.md": "Log-Based Recovery & Checkpointing",
    "9_Self_Learning_Distributed_Transactions_TCL_Performance_Tuning.md": "Distributed Transactions, TCL & Performance Tuning (Self-Learning)",

    # DBMS Module 6
    "1_IBM_Db2_Overview_Architecture_Use_Cases.md": "IBM Db2 Overview, Architecture & Use Cases",
    "2_Db2_System_Requirements_Installation_and_Interfaces.md": "Db2 System Requirements, Installation & Interfaces",
    "3_Basic_SQL_Operations_in_Db2.md": "Basic SQL Operations in IBM Db2",
    "4_Self_Learning_Db2_Cloud_Backup_Indexing_Warehouse.md": "Db2 on Cloud, Backup, Indexing & Warehouse (Self-Learning)",

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

    # Data Structures Module 4
    "1_Tree_Introduction_and_Terminologies.md": "Tree Introduction & Terminologies",
    "2_Binary_Tree_Representation_and_Types.md": "Binary Tree Representation & Types",
    "3_Binary_Tree_Traversals.md": "Binary Tree Traversals (Inorder, Preorder, Postorder)",
    "4_Binary_Search_Tree_and_Operations.md": "Binary Search Tree (BST) & Operations",
    "5_Applications_of_Binary_Tree_Expression_Tree_and_Huffman.md": "Applications of Binary Tree: Expression Tree & Huffman",
    "6_AVL_Tree_Rotations_and_Operations.md": "AVL Tree Rotations & Operations",
    "7_Introduction_to_B_Tree_and_B_Plus_Tree.md": "Introduction to B-Tree & B+ Tree",
    "8_Self_Learning_Red_Black_Trees.md": "Red-Black Trees (Self-Learning)",

    # Data Structures Module 5
    "1_Graph_Introduction_and_Terminologies.md": "Graph Introduction & Terminologies",
    "2_Graph_Representations.md": "Graph Representations (Adjacency Matrix & List)",
    "3_Graph_Traversals_BFS_and_DFS.md": "Graph Traversals: BFS & DFS",
    "4_Self_Learning_Graph_Application_Topological_Sorting.md": "Topological Sorting in Graphs (Self-Learning)",

    # Data Structures Module 6
    "1_Searching_Techniques_Linear_and_Binary_Search.md": "Searching Techniques: Linear & Binary Search",
    "2_Sorting_Techniques_Bubble_Insertion_Selection_Sort.md": "Sorting Techniques: Bubble, Insertion & Selection Sort",
    "3_Hashing_Concepts_and_Hash_Functions.md": "Hashing Concepts & Hash Functions",
    "4_Collision_Resolution_Techniques.md": "Collision Resolution Techniques (Open Addressing & Chaining)",
    "5_Self_Learning_Merge_Sort_and_Quick_Sort.md": "Merge Sort & Quick Sort (Self-Learning)",

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

    # MPCA Module 4
    "1_Memory_Interfacing_RAM_and_ROM_Decoding.md": "Memory Interfacing: RAM & ROM Decoding",
    "2_8255_Programmable_Peripheral_Interface_PPI.md": "8255 Programmable Peripheral Interface (PPI)",
    "3_8257_Direct_Memory_Access_Controller_DMAC.md": "8257 Direct Memory Access Controller (DMAC)",
    "4_8259_Programmable_Interrupt_Controller_PIC.md": "8259 Programmable Interrupt Controller (PIC)",
    "5_Self_Learning_Address_Decoding_Techniques_and_8259_Cascading.md": "Address Decoding Techniques & 8259 Cascading (Self-Learning)",

    # MPCA Module 5
    "1_80386DX_Architecture_and_Functional_Units.md": "80386DX Architecture & Functional Units",
    "2_80386_Register_Organization.md": "80386 Register Organization",
    "3_80386_Operating_Modes.md": "80386 Operating Modes (Real, Protected & Virtual 8086)",
    "4_Pentium_Processor_Architecture_and_Superscalar_Pipelining.md": "Pentium Processor Architecture & Superscalar Operation",
    "5_Self_Learning_80386_Memory_Management_Paging_and_MESI_Cache.md": "80386 Memory Management & MESI Cache Protocol (Self-Learning)",

    # MPCA Module 6
    "1_Evolutionary_Comparison_8086_to_Pentium.md": "Comparative Study: 8086 to Pentium 4",
    "2_Pentium_4_NetBurst_Microarchitecture.md": "Pentium 4 NetBurst Microarchitecture",
    "3_Pentium_4_ITLB_Branch_Prediction_and_Hyper_Threading.md": "Pentium 4 ITLB, Branch Prediction & Hyper-Threading",
    "4_Self_Learning_ARM_Processor_Architecture_and_Features.md": "ARM Processor Architecture & Features (Self-Learning)",
}

def get_clean_title(filename, content, is_qa_file, subject, module):
    fn = os.path.basename(filename)

    if is_qa_file:
        marks_match = re.search(r'(\d+)M', fn, re.I)
        marks = f"{marks_match.group(1)}-Mark" if marks_match else "Solved"
        mod_desc = MODULE_TITLES.get(subject, {}).get(module, "")
        if mod_desc:
            return f"{module}: {marks} Questions & Answers ({mod_desc})"
        return f"{module}: {marks} Questions & Answers"

    if fn in EXACT_TITLES:
        return EXACT_TITLES[fn]

    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    t = title_match.group(1).strip() if title_match else fn.replace('.md', '').replace('_', ' ')
    t = re.sub(r'^#+\s*', '', t).strip()
    t = re.sub(r'^Topic\s*[:\-]\s*', '', t, flags=re.IGNORECASE).strip()
    t = re.sub(r'^(?:[A-Za-z]\d{1,2}|\d{1,2})[\._\s\-]+\s*', '', t).strip()
    t = re.sub(r'\s*[\u2014\u2013\-]\s*(MPCA|DBMS|Data Structures?|Module\s*\d+).*$', '', t, flags=re.IGNORECASE).strip()
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
    is_qa_file = bool(re.search(r'\b(2M|3M|5M|10M)\.md$', filename, re.I)) or '_qa' in rel_path.lower()
    content_type = "qa" if is_qa_file else "notes"

    # Identify exact Module number
    module = "General"
    for part in parts:
        m_match = re.search(r'Module[_\s]*(\d+)', part, re.IGNORECASE)
        if m_match:
            module = f"Module {m_match.group(1)}"
            break

    # Extract marks category
    marks_match = re.search(r'(\d+)M', filename, re.I)
    marks_category = f"{marks_match.group(1)} Marks" if marks_match else "All"

    title = get_clean_title(filename, content, is_qa_file, subject, module)

    # Extract Definition block
    def_match = re.search(r'>\s*📌\s*\*\*Definition to Remember\*\*\s*\n>\s*(.+?)(?=\n\n|\n>|\n---|\Z)', content, re.DOTALL)
    if not def_match:
        def_match = re.search(r'>\s*\*\*Definition:\*\*\s*(.+?)(?=\n\n|\n>|\n---|\Z)', content, re.DOTALL)
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
    else:
        must_write_section = re.search(r'##\s*\d*\.?\s*Must-Write Points[^\n]*\n((?:[\*\-]\s*.*?\n)+)', content)
        if must_write_section:
            lines = must_write_section.group(1).split('\n')
            for line in lines:
                cleaned = re.sub(r'^[\*\-]\s*', '', line).strip()
                if cleaned:
                    must_write.append(cleaned)

    # Extract Quick Recall
    quick_match = re.search(r'>\s*⚡\s*\*\*Quick Recall\*\*\s*\n>\s*`?(.+?)`?\s*(?=\n|\Z)', content)
    if not quick_match:
        quick_match = re.search(r'##\s*\d*\.?\s*Quick Recall[^\n]*\n```[a-z]*\n(.+?)\n```', content, re.DOTALL)
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
        "contentType": content_type,
        "isQA": is_qa_file,
        "marksCategory": marks_category,
        "title": title,
        "content": content,
        "html": html,
        "definition": definition,
        "mustWrite": must_write,
        "quickRecall": quick_recall
    }

def check_pdf_exists(pdf_rel_path, rel_path):
    full_pdf_path = os.path.join(BASE_DIR, pdf_rel_path)
    if os.path.exists(full_pdf_path):
        return pdf_rel_path
    flat_pdf_path = f"PDF_Notes/{os.path.basename(rel_path)[:-3]}.pdf"
    if os.path.exists(os.path.join(BASE_DIR, flat_pdf_path)):
        return flat_pdf_path
    return None

def main():
    notes_list = []
    
    for root, dirs, files in os.walk(os.path.join(BASE_DIR, "Semester 3")):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                try:
                    note_obj = parse_markdown_file(filepath)
                    notes_list.append(note_obj)
                except Exception as e:
                    print(f"Error parsing {filepath}: {e}")

    # Sort notes logically: Semester -> Subject -> Module -> ContentType -> Filename
    # Custom sort for marks: 2M -> 3M -> 5M -> 10M
    def sort_key(x):
        fn = x['filename']
        mark_order = 0
        if fn.startswith('2M'): mark_order = 1
        elif fn.startswith('3M'): mark_order = 2
        elif fn.startswith('5M'): mark_order = 3
        elif fn.startswith('10M'): mark_order = 4
        return (x['semester'], x['subject'], x['module'], x['contentType'], mark_order, x['filename'])

    notes_list.sort(key=sort_key)

    js_content = f"window.NOTES_DATA = {json.dumps(notes_list, indent=2, ensure_ascii=False)};\n"
    
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"Successfully generated notes_data.js for {len(notes_list)} files with clean Q&A bank integration!")

if __name__ == '__main__':
    main()
