# Automated Syllabus-to-Teaching-Website Platform Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a complete, automated academic teaching platform that converts every syllabus PDF into a dedicated, interactive, deployable teaching website with a centralized liquid glass faculty dashboard, starting with a fully verified pilot course (`PCCST303: Data Structures and Algorithms`).

**Architecture:** A modular, static-deployable multi-site architecture where each course has its own standalone learning website under `/courses/COURSE_CODE/`, unified by a shared design system, liquid glass theme engine, and accessible interaction components. The centralized faculty dashboard under `/faculty-dashboard/` manages all 158 verified courses, monitors content generation, provides live status, and automated companion PDFs with embedded clickable links to live course sites.

**Tech Stack:** HTML5, Modern Vanilla CSS (Glassmorphism, Dark/Light modes, CSS Custom Properties), Vanilla JavaScript (ES6+), Canvas / SVG / Three.js for 3D and algorithm visualizers, Web Speech API for voice narration, PyMuPDF / Python for PDF extraction, link injection, and automated testing.

**Spec:** Master Prompt — Automated Syllabus-to-Teaching-Website Platform — Jane Rose, Assistant Professor, CSE.

## Global Constraints
- Every readable PDF in the Syllabus folder must be processed with extracted metadata preserved for auditing.
- Use official course codes as unique identifiers (158 verified courses in KTU 2024 Scheme).
- Pilot course: `PCCST303: Data Structures and Algorithms` (Semester S3, 4 Credits, 4 Modules).
- Mandatory 46-hour teaching plan: syllabus requires 44 contact hours (4 x 11 hours); discrepancy explicitly documented with +2 hours revision/tutorials = 46 hours.
- Every course website must feature: official syllabus, 46-hr teaching plan, module notes, lecture slides, interactive demos, solved PYQs, 3D/Canvas algorithm animations, real-world industry projects, verified IEEE papers with DOIs, sourced salary data, quizzes/games, knowledge graph, and voice narration.
- Centralized Faculty Dashboard must support light/dark themes and 10 selectable glass styles (Frosted, Liquid, Aurora, Crystal, Holographic, Layered Translucent, Neumorphic, Dark Sci-Fi, Light Academic, High-Contrast).
- Companion PDF copies with clickable teaching links generated for each source syllabus PDF.
- Branding footer on every page: `Jane Rose | Asst. Professor | CSE`.

## Review Focus
1. **Syllabus fidelity**: Module names, topic lists, and credits must match official KTU 2024 text verbatim without fabrication.
2. **Teaching hour reconciliation**: The official 44 contact hours vs. 46 hours target must be explicitly reconciled and clearly visible in the UI.
3. **Interactive widgets reliability**: Algorithm visualizations, quizzes, knowledge graphs, and voice synthesis must run purely in standard browsers without external API keys or broken CDNs.
4. **PDF link accuracy**: Clickable links injected into companion PDFs must point to valid course URLs (`http://localhost:5173/courses/COURSE_CODE/` or production domain).
5. **Accessibility & Responsive design**: All UI elements must maintain WCAG AA contrast, reduced motion respect, and mobile responsiveness.

---

### Task 1: Discovered Syllabus Inventory & Master Course Registry Validation

**Files:**
- Create: `c:\Users\Asus\Downloads\SYLLABUS\tests\test_registry.py`
- Modify: `c:\Users\Asus\Downloads\SYLLABUS\registry\course_registry.json`
- Modify: `c:\Users\Asus\Downloads\SYLLABUS\registry\course_registry.csv`

**Interfaces:**
- Consumes: PyMuPDF raw text from 4 syllabus PDFs.
- Produces: Validated `course_registry.json` and `course_registry.csv` with 158 verified courses.

- [ ] **Step 1: Write test to verify course registry schema and course counts**
- [ ] **Step 2: Run test to verify passes against extracted registry**
- [ ] **Step 3: Ensure PCCST303 is registered with full metadata**
- [ ] **Step 4: Verify CSV and JSON synchronization**

---

### Task 2: Shared Design System & Liquid Glass Theme Engine

**Files:**
- Create: `c:\Users\Asus\Downloads\SYLLABUS\shared-components\themes\liquid-glass.css`
- Create: `c:\Users\Asus\Downloads\SYLLABUS\shared-components\themes\theme-switcher.js`
- Create: `c:\Users\Asus\Downloads\SYLLABUS\tests\test_theme_engine.py`

**Interfaces:**
- Consumes: CSS custom properties (`--glass-bg`, `--glass-border`, `--glass-blur`, `--accent-glow`).
- Produces: 10 selectable glass styles with real-time UI switching, dark/light modes, and WCAG AA contrast.

- [ ] **Step 1: Write automated test for CSS tokens and theme variables**
- [ ] **Step 2: Implement `liquid-glass.css` with 10 glass themes**
- [ ] **Step 3: Implement `theme-switcher.js` with persistence in `localStorage`**
- [ ] **Step 4: Verify theme switching and reduced motion support**

---

### Task 3: Pilot Course Website Architecture (`/courses/PCCST303/`)

**Files:**
- Create: `c:\Users\Asus\Downloads\SYLLABUS\courses\PCCST303\website\index.html`
- Create: `c:\Users\Asus\Downloads\SYLLABUS\courses\PCCST303\website\course.css`
- Create: `c:\Users\Asus\Downloads\SYLLABUS\courses\PCCST303\website\course.js`

**Interfaces:**
- Consumes: `pccst303_data.json` and shared liquid glass styles.
- Produces: Standalone, responsive course homepage with tabs/sections for all 14 teaching components.

- [ ] **Step 1: Scaffold course website layout with semantic HTML5 and branding footer**
- [ ] **Step 2: Add official course metadata banner, syllabus tabs, and progress counters**
- [ ] **Step 3: Connect navigation and theme switcher**
- [ ] **Step 4: Test in browser via automated test**

---

### Task 4: 46-Hour Comprehensive Teaching Plan for PCCST303

**Files:**
- Create: `c:\Users\Asus\Downloads\SYLLABUS\courses\PCCST303\teaching-plan\teaching_plan_46h.json`
- Modify: `c:\Users\Asus\Downloads\SYLLABUS\courses\PCCST303\website\index.html`

**Interfaces:**
- Consumes: Module 1 (11h), Module 2 (11h), Module 3 (11h), Module 4 (11h) + 2h Revision/Assessment = 46h.
- Produces: Full 46-hour interactive teaching schedule table with filtering by module, lecture hour, teaching method, and board work numericals.

- [ ] **Step 1: Generate granular 46-lecture dataset (Lecture, Module, Topic, LO, Method, Board Work, Practical Demo, Student Activity, Quiz, Homework)**
- [ ] **Step 2: Render interactive teaching plan table in the website with search/filter**
- [ ] **Step 3: Add faculty progress tracking toggles (Planned vs Completed)**
- [ ] **Step 4: Verify total hours count equals 46 with discrepancy badge**

---

### Task 5: Module-Wise Deep Notes and Downloadable Slides

**Files:**
- Create: `c:\Users\Asus\Downloads\SYLLABUS\courses\PCCST303\notes\module_notes.json`
- Create: `c:\Users\Asus\Downloads\SYLLABUS\courses\PCCST303\slides\lecture_slides.html`
- Modify: `c:\Users\Asus\Downloads\SYLLABUS\courses\PCCST303\website\index.html`

**Interfaces:**
- Consumes: Official module syllabus descriptions and textbook references.
- Produces: Complete educational notes for Modules 1 to 4 with derivations, comparison tables, code, exam tips, and printable slide deck.

- [ ] **Step 1: Write comprehensive notes for Modules 1, 2, 3, 4**
- [ ] **Step 2: Build interactive slide presenter with fullscreen mode and print-to-PDF support**
- [ ] **Step 3: Embed notes viewer with collapsible subtopics and search**
- [ ] **Step 4: Verify text clarity and mathematical notation**

---

### Task 6: Interactive Algorithm Demonstrations, Sandbox & 3D Visualizer

**Files:**
- Create: `c:\Users\Asus\Downloads\SYLLABUS\courses\PCCST303\algorithms\algorithm_visualizer.js`
- Create: `c:\Users\Asus\Downloads\SYLLABUS\courses\PCCST303\algorithms\tree_3d_canvas.js`
- Modify: `c:\Users\Asus\Downloads\SYLLABUS\courses\PCCST303\website\index.html`

**Interfaces:**
- Consumes: Canvas/WebGL 2D & 3D rendering context.
- Produces: Interactive visualizers for Stacks/Queues, Binary Search Trees, Sorting algorithms, and Graph traversals with Play/Pause/Step/Speed controls.

- [ ] **Step 1: Implement Sorting Visualizer (Quick Sort, Merge Sort, Heap Sort) with step-by-step playback**
- [ ] **Step 2: Implement 3D/Interactive Binary Search Tree & Expression Tree Canvas**
- [ ] **Step 3: Implement Infix to Postfix expression evaluator with stack visualization**
- [ ] **Step 4: Test responsiveness and framerate**

---

### Task 7: Solved Previous-Year Questions & Model Examination Papers

**Files:**
- Create: `c:\Users\Asus\Downloads\SYLLABUS\courses\PCCST303\solved-question-papers\pyq_solutions.json`
- Modify: `c:\Users\Asus\Downloads\SYLLABUS\courses\PCCST303\website\index.html`

**Interfaces:**
- Consumes: KTU S3 exam pattern (Part A: 8 questions x 3 marks = 24; Part B: 4 modules x 9 marks = 36; Total 60 marks).
- Produces: Step-by-step worked solutions, numerical calculations, mark allocations, and concise revision summaries.

- [ ] **Step 1: Assemble authentic question bank mapped to Modules 1-4**
- [ ] **Step 2: Add step-by-step solutions with diagrams, code, and mark distribution**
- [ ] **Step 3: Add filterable question paper viewer (by Module, Marks, Difficulty)**
- [ ] **Step 4: Verify clear labeling of official vs model questions**

---

### Task 8: Real-Life Industry Applications, Projects & Portfolio Guide

**Files:**
- Create: `c:\Users\Asus\Downloads\SYLLABUS\courses\PCCST303\applications\industry_projects.json`
- Modify: `c:\Users\Asus\Downloads\SYLLABUS\courses\PCCST303\website\index.html`

**Interfaces:**
- Consumes: Data structure applications in industry (OS memory allocators, database indexing B-trees, network routing graphs, autocomplete tries).
- Produces: 4 complete student portfolio project guides with architecture diagrams, datasets, and code.

- [ ] **Step 1: Draft 4 industry projects with architecture, algorithms, and evaluation metrics**
- [ ] **Step 2: Build project gallery UI in the course website**
- [ ] **Step 3: Verify code snippets and portfolio guidelines**

---

### Task 9: IEEE Research Literature, Career Paths & Sourced Salary Research

**Files:**
- Create: `c:\Users\Asus\Downloads\SYLLABUS\courses\PCCST303\research\ieee_papers.json`
- Create: `c:\Users\Asus\Downloads\SYLLABUS\courses\PCCST303\careers\career_salary_data.json`
- Modify: `c:\Users\Asus\Downloads\SYLLABUS\courses\PCCST303\website\index.html`

**Interfaces:**
- Consumes: Verified IEEE papers, DOIs, industry compensation data (India, Canada, UAE).
- Produces: Research literature survey table, research gap roadmap, career ladder, and transparently sourced salary benchmarks.

- [ ] **Step 1: Curate verified IEEE papers with real DOIs and syllabus mapping**
- [ ] **Step 2: Compile salary benchmarks (INR, CAD, AED) with sources and dates**
- [ ] **Step 3: Render research and career sections on the course website**
- [ ] **Step 4: Verify links and disclaimer labels**

---

### Task 10: Gamified Quizzes, Puzzles & Interactive Knowledge Graph

**Files:**
- Create: `c:\Users\Asus\Downloads\SYLLABUS\courses\PCCST303\quizzes\quiz_engine.js`
- Create: `c:\Users\Asus\Downloads\SYLLABUS\courses\PCCST303\knowledge-graph\knowledge_graph.js`
- Modify: `c:\Users\Asus\Downloads\SYLLABUS\courses\PCCST303\website\index.html`

**Interfaces:**
- Consumes: Syllabus topic relationships and quiz question banks.
- Produces: Interactive MCQ engine with instant feedback/scoring, and interactive SVG/Canvas knowledge graph with zoom, pan, and node exploration.

- [ ] **Step 1: Implement quiz engine with module-wise MCQs, instant explanations, and score card**
- [ ] **Step 2: Implement interactive Knowledge Graph connecting concepts, algorithms, and career skills**
- [ ] **Step 3: Connect graph node clicks to section scrolls/popups**
- [ ] **Step 4: Test quiz state and graph responsiveness**

---

### Task 11: Web Speech Narration & Accessibility (WCAG AA)

**Files:**
- Create: `c:\Users\Asus\Downloads\SYLLABUS\shared-components\voice\narration_engine.js`
- Modify: `c:\Users\Asus\Downloads\SYLLABUS\courses\PCCST303\website\index.html`

**Interfaces:**
- Consumes: Browser SpeechSynthesis API with graceful offline fallback.
- Produces: Narration bar with Play/Pause, speed adjustment (0.75x to 2x), synchronized highlighting, and captions.

- [ ] **Step 1: Implement Web Speech narration controller**
- [ ] **Step 2: Add keyboard shortcuts (Space to toggle, Esc to stop) and captions box**
- [ ] **Step 3: Verify fallback when speech synthesis is unavailable**

---

### Task 12: Centralized Liquid Glass Faculty Dashboard

**Files:**
- Create: `c:\Users\Asus\Downloads\SYLLABUS\faculty-dashboard\index.html`
- Create: `c:\Users\Asus\Downloads\SYLLABUS\faculty-dashboard\dashboard.css`
- Create: `c:\Users\Asus\Downloads\SYLLABUS\faculty-dashboard\dashboard.js`

**Interfaces:**
- Consumes: `course_registry.json` (158 courses) and `deployment_manifest.json`.
- Produces: Faculty control center with 10 glass themes, real-time KPI metrics, course search/filter, pilot launcher, batch generation triggers, and deployment audit.

- [ ] **Step 1: Scaffold faculty dashboard with 10 selectable glass styles and dark/light modes**
- [ ] **Step 2: Render KPI stats (1,206 pages scanned, 158 courses, modules, hours, deployment links)**
- [ ] **Step 3: Build searchable course datatable with links to individual course websites**
- [ ] **Step 4: Add pilot course direct launch card and status indicators**

---

### Task 13: Companion PDF Generator with Clickable Course Links

**Files:**
- Create: `c:\Users\Asus\Downloads\SYLLABUS\scripts\generate_linked_pdfs.py`
- Modify: `c:\Users\Asus\Downloads\SYLLABUS\registry\deployment_manifest.json`

**Interfaces:**
- Consumes: Original 4 syllabus PDFs and course registry URLs.
- Produces: Companion PDFs (e.g. `Computer Science and Engineering_with_course_links.pdf`) with clickable teaching material links inserted into course headers.

- [ ] **Step 1: Write PyMuPDF script to locate course headers in PDFs and inject clickable annotations/links**
- [ ] **Step 2: Run script to generate linked PDFs for all 3 syllabus documents**
- [ ] **Step 3: Verify clickable links in generated PDF using PDF reader/PyMuPDF link extractor**
- [ ] **Step 4: Update deployment manifest with linked PDF paths**

---

### Task 14: Automated Testing, Deployment & Verification

**Files:**
- Create: `c:\Users\Asus\Downloads\SYLLABUS\tests\test_full_platform.py`
- Create: `c:\Users\Asus\Downloads\SYLLABUS\server.js` (or static dev server)
- Modify: `c:\Users\Asus\Downloads\SYLLABUS\PROJECT_STATUS.md`
- Create: `c:\Users\Asus\Downloads\SYLLABUS\README.md`

**Interfaces:**
- Consumes: All generated course assets, dashboard, and registry files.
- Produces: Live preview server, passing test suite, and final verification report.

- [ ] **Step 1: Write integration test suite checking all endpoints, assets, and branding**
- [ ] **Step 2: Start local server and test with browser agent**
- [ ] **Step 3: Update `PROJECT_STATUS.md` and `README.md`**
- [ ] **Step 4: Final verification and handoff**
