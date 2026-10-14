# Automated Syllabus-to-Teaching-Website Platform
### Faculty: Jane Rose | Asst. Professor | CSE
**Institution:** APJ Abdul Kalam Technological University (KTU)  
**Curriculum Regulation:** B.Tech Curriculum 2024 Scheme  

---

## Overview

The **Automated Syllabus-to-Teaching-Website Platform** converts official syllabus PDFs across Computer Science & Engineering, Artificial Intelligence, and Cyber Security into interactive, responsive, student-ready teaching websites with a centralized faculty control dashboard.

Every course code is provided with:
1. **Dedicated Course Website:** Standalone SPA at `/courses/COURSE_CODE/`.
2. **Official Syllabus & Outcomes:** Direct extraction of contact hours, credits, and Course Outcomes (CO1..CO4) mapped to Bloom's taxonomy.
3. **46-Hour Reconciled Teaching Plan:** Complete 46-lecture syllabus schedule with lecture-by-lecture learning objectives, board work numericals, practical demonstrations, real-life applications, and assessment criteria.
4. **Module Notes:** Deep-dive educational notes for all 4 official modules with mathematical derivations, worked examples, and KTU examination tips.
5. **Presentation Slides:** Fullscreen interactive slide deck exportable to PDF for offline printing.
6. **Interactive Demonstrations & Sandboxes:** Real-time algorithm visualizers (Sorting, Stacks, Binary Search Trees).
7. **Solved Question Papers:** KTU Part A (3-mark) and Part B (9-mark) questions with step-by-step worked solutions.
8. **Real-Life Industry Projects:** Production system architectures, datasets, and capstone portfolio projects.
9. **IEEE Research Literature:** Verified publications with DOIs connecting syllabus modules to active research topics.
10. **Career Opportunities & Sourced Salaries:** Transparent compensation ranges in India, Canada, and the UAE with cited sources.
11. **Gamified Quizzes & Knowledge Graph:** Interactive MCQs with instant feedback, scoring, and SVG knowledge graph.
12. **Web Speech Narration:** Built-in speech synthesis with speed control, keyboard shortcuts, and captions.
13. **Centralized Faculty Dashboard:** Multi-style Liquid Glass UI with 10 selectable styles and searchable catalog of all 158 courses.
14. **Companion PDFs with Clickable Links:** Original PDFs preserved; companion PDFs created with clickable teaching links embedded on each course header.

---

## Directory Structure

```text
academic-teaching-platform/
├── README.md
├── PROJECT_STATUS.md
├── server.js                        # Node.js dev & preview server
├── syllabus/
│   ├── originals/                   # 4 Source KTU 2024 PDFs (1,206 pages)
│   └── processed-pdfs/              # Companion PDFs with embedded clickable links
├── registry/
│   ├── course_registry.csv          # Master CSV of 158 verified courses
│   ├── course_registry.json         # Master JSON course registry
│   └── deployment_manifest.json     # Per-course deployment mapping
├── faculty-dashboard/
│   ├── index.html                   # Centralized Liquid Glass faculty dashboard
│   ├── dashboard.css                # Glassmorphism & layout styles
│   └── dashboard.js                 # Search, filter & launch controller
├── shared-components/
│   └── themes/
│       ├── liquid-glass.css         # 10 Selectable glass styles + dark/light mode
│       └── theme-switcher.js        # Theme engine with localStorage persistence
├── courses/
│   ├── PCCST303/                    # Pilot Course: Data Structures & Algorithms
│   │   ├── syllabus/
│   │   ├── teaching-plan/
│   │   ├── notes/
│   │   ├── slides/
│   │   └── website/
│   └── [157 OTHER COURSES]/         # Dedicated directory per unique course code
├── scripts/
│   ├── build_all_courses.py         # Automated batch course generator
│   └── generate_linked_pdfs.py      # PyMuPDF PDF link injector
└── tests/
    ├── test_registry.py
    ├── test_theme_engine.py
    ├── test_pilot_course.py
    ├── test_dashboard.py
    ├── test_pdf_links.py
    └── test_full_platform.py        # Integration test runner
```

---

## Quick Start & Verification

### 1. Run Automated Test Suite
```bash
py tests/test_full_platform.py
```
*Runs all 19 unit & integration tests covering schema, glass themes, pilot course components, dashboard KPIs, and PDF link integrity.*

### 2. Launch Local Dev Server
```bash
node server.js
```
*Starts server at `http://localhost:5173`.*

### 3. Key Navigation URLs
- **Faculty Dashboard:** [http://localhost:5173/faculty-dashboard/](http://localhost:5173/faculty-dashboard/)
- **Pilot Course Website (PCCST303):** [http://localhost:5173/courses/PCCST303/](http://localhost:5173/courses/PCCST303/)
- **PCCST303 Slide Presenter:** [http://localhost:5173/courses/PCCST303/slides/](http://localhost:5173/courses/PCCST303/slides/)
- **Dynamic Course Portal:** `http://localhost:5173/courses/:COURSE_CODE/` (e.g., `/courses/PCCST302/`, `/courses/GAEST305/`, `/courses/GAMAT301/`)

---
**Branding Footer:** Jane Rose | Asst. Professor | CSE  
APJ Abdul Kalam Technological University
