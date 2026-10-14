# Automated Syllabus-to-Teaching-Website Platform
## Project Status & Execution Tracking
**Faculty:** Jane Rose | Asst. Professor | CSE  
**University & Regulation:** APJ Abdul Kalam Technological University (KTU) — B.Tech Curriculum 2024 Scheme  
**Repository Root:** `c:\Users\Asus\Downloads\SYLLABUS`  
**Last Updated:** 2026-10-14  

---

## 1. Discovered Syllabus Inventory (1,206 Pages Processed)

| Source PDF File | Size | Total Pages | Programme / Scope | Courses Extracted |
|:---|:---:|:---:|:---|:---:|
| `B. Tech Curriculum-2024 Semester I to VIII.pdf` | 1.17 MB | 12 | B.Tech Curriculum Scheme (Semesters 1 to 8) | Common scheme roadmap |
| `Computer Science and Engineering.pdf` | 7.16 MB | 444 | B.Tech Computer Science & Engineering (Core & Electives) | 100 courses |
| `Computer Science and Engineering (Artificial Intelligence).pdf` | 6.98 MB | 399 | B.Tech CSE (Artificial Intelligence) | 92 courses |
| `Computer Science and Engineering (Cyber Security) .pdf` | 8.09 MB | 351 | B.Tech CSE (Cyber Security) | 76 courses |
| **Total Unique Courses Identified** | | **1,206 pages** | **3 Degree Programmes** | **158 Unique Courses** |

---

## 2. Master Registries Created & Synchronized
- `registry/course_registry.csv` (158 courses with Codes, Titles, Semesters, Credits, LTPR, Marks, Source PDF, Page numbers)
- `registry/course_registry.json` (Structured JSON catalog for dashboard and web routing)
- `registry/deployment_manifest.json` (Per-course deployment mapping, URL paths, build status, and linked PDF audit for all 158 courses)

---

## 3. Companion PDFs with Clickable Teaching Links Generated
All 3 original PDFs preserved intact; companion linked PDFs generated in `syllabus/processed-pdfs/`:
1. `syllabus/processed-pdfs/Computer Science and Engineering_with_course_links.pdf` (97 clickable course links embedded)
2. `syllabus/processed-pdfs/Computer Science and Engineering (Artificial Intelligence)_with_course_links.pdf` (25 clickable course links embedded)
3. `syllabus/processed-pdfs/Computer Science and Engineering (Cyber Security)_with_course_links.pdf` (36 clickable course links embedded)

---

## 4. Platform Phase Execution Summary

| Phase | Description | Status | Deliverables / Artifacts |
|:---|:---|:---:|:---|
| **Phase 1: Discovery** | Inspect syllabus directory, extract text, discover PDFs | **COMPLETED** | 4 PDFs inventoried (1,206 pages) |
| **Phase 2: Master Registry** | Build `course_registry.csv` and `course_registry.json` | **COMPLETED** | 158 verified unique courses cataloged |
| **Phase 3: Platform Architecture** | Design system, liquid glass theme engine, shared components | **COMPLETED** | `shared-components/themes/liquid-glass.css` (10 glass styles) |
| **Phase 4: Pilot Website Scaffold** | Dedicated course website for `PCCST303` | **COMPLETED** | `/courses/PCCST303/` standalone SPA/HTML5 |
| **Phase 5: 46-Hour Teaching Plan** | Lecture-by-lecture schedule with learning objectives | **COMPLETED** | 46 hours mapped across 4 modules with board work |
| **Phase 6: Module Notes & Slides** | Deep-dive notes and lecture slides for all 4 modules | **COMPLETED** | Printable slide deck + comprehensive notes |
| **Phase 7: Demos & Code Sandbox** | Executable interactive algorithms (Stacks, Trees, Sorting) | **COMPLETED** | Step-by-step visualizations & code execution |
| **Phase 8: Question Papers & Solutions** | KTU model & previous exams with step-by-step answers | **COMPLETED** | Filterable interactive QP solver |
| **Phase 9: 3D Visualizations & Canvas** | 3D tree/graph traversal, animated sorting algorithms | **COMPLETED** | Canvas interactive simulations |
| **Phase 10: Industry Projects & Applications** | Real-world industry case studies and student portfolios | **COMPLETED** | 4 complete industry projects with architectures |
| **Phase 11: IEEE Papers & Research** | Sourced IEEE papers, DOIs, research gaps & projects | **COMPLETED** | Literature survey & student research roadmap |
| **Phase 12: Careers & Sourced Salaries** | Roles, required skills, India/Canada/UAE salary ranges | **COMPLETED** | Data-backed compensation & interview guide |
| **Phase 13: Quizzes & Gamification** | Interactive MCQs, drag-and-drop, flashcards, scoring | **COMPLETED** | Real-time score tracking & knowledge tests |
| **Phase 14: Interactive Knowledge Graph** | Connected nodes of modules, algorithms, applications | **COMPLETED** | Interactive SVG graph with node interaction |
| **Phase 15: Voice Narration & A11y** | Web Speech API narration, speed controls, captions | **COMPLETED** | Accessible narration with keyboard controls |
| **Phase 16: Liquid Glass Faculty Dashboard** | Central dashboard with 10 glass themes, course switcher | **COMPLETED** | `/faculty-dashboard/` with real metrics & search |
| **Phase 17: Linked PDF Generator** | Generate companion PDF with clickable course links | **COMPLETED** | PyMuPDF PDF link injector (all 3 PDFs) |
| **Phase 18: Quality & Acceptance** | Automated test suite & preview server | **COMPLETED** | 19 unit tests passing (100% OK), Dev server live |

---

## 5. Live URLs
- **Faculty Dashboard:** `http://localhost:5173/faculty-dashboard/`
- **Pilot Course Website (PCCST303):** `http://localhost:5173/courses/PCCST303/`
- **Lecture Slide Presenter:** `http://localhost:5173/courses/PCCST303/slides/`
- **Any Course Website:** `http://localhost:5173/courses/:COURSE_CODE/`

---
*Branding: Jane Rose \| Asst. Professor \| CSE*
