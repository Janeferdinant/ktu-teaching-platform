# Module Components & Presentation Enrichment Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Cross-check and enrich each module across the academic platform with corresponding 3D interactive demos, worked numerical solutions, industry applications, module-filtered knowledge graphs, comprehensive module quizzes, and solved previous-year examination papers with embedded technical SVG figures, followed by automated production deployment to Vercel using Windows Credential Manager.

**Architecture:** 
1. Build a multi-module interactive showcase system in `shared-components/course/` supporting 3D canvas renderers (Stack/Matrix 3D, Memory Allocation Blocks 3D, BST/Graph 3D, Hashing/Bucket 3D).
2. Create rich module-by-module sections for Numerical Solutions (with LaTeX-style formulations and step-by-step mathematical derivations), Applications, Knowledge Graphs, and Quizzes.
3. Implement solved KTU University Question Papers with embedded vector SVG diagrams for all 4 modules.
4. Upgrade `courses/PCCST303/` (pilot) and `scripts/build_all_courses.py` (all 158 courses) to render these enriched components.
5. Run test suite verification (`tests/test_full_platform.py` and `tests/test_module_features.py`).
6. Deploy directly to Vercel Production via Windows Credential Manager credentials and verify live.

**Tech Stack:** HTML5, Canvas 3D isometric projection, Vanilla CSS (Liquid Glass), JavaScript, SVG vector diagrams, Vercel CLI, Windows Credential Manager.

---

## Global Constraints
- Branding footer strictly: `Jane Rose | Asst. Professor | CSE`
- Regulation: `KTU B.Tech 2024 Scheme`
- Hours Model: `46 Hours (44 Contact + 2 Revision)`
- Every course must have 4 modules with distinct technical data.
- Previous year papers MUST contain embedded SVG figures/diagrams.

---

## Tasks

### Task 1: Module-Specific 3D Interactive Canvas Visualizer
- [x] Implement 4 distinct 3D visualizers in `shared-components/course/course.js`:
  - Module 1: 3D Stack / Queue isometric block memory visualizer with push/pop animations.
  - Module 2: 3D Dynamic Memory Allocation Heap blocks visualizer (First-Fit, Best-Fit with fragmentation depth).
  - Module 3: 3D Rotating Binary Search Tree / Graph mesh with node depth, lighting, and traversal highlight.
  - Module 4: 3D Hash Table Bucket Matrix with collision probing visualization.
- [x] Add module switcher selector buttons to the Interactive Demos tab so students can switch between Module 1, 2, 3, and 4 simulations.

### Task 2: Worked Numerical Solutions for Modules 1 to 4
- [x] Add structured numerical derivations for each module:
  - Module 1: Recurrence relation derivation via substitution & Master Theorem.
  - Module 2: Memory allocation fragmentation & doubly linked list memory footprint equations.
  - Module 3: Binary heap build-heap O(n) summation proof and BST height calculations.
  - Module 4: Hash collision probing sequence calculations (Linear, Quadratic, Double Hashing).
- [x] Display with clear step-by-step mathematical work, variable definitions, and KTU marks breakdown.

### Task 3: Real-Life Systems Applications by Module
- [x] Detail production engineering architectures for each module:
  - Module 1: Web browser navigation history stack and OS print spoolers.
  - Module 2: Linux kernel `kmalloc` slab allocators and media circular buffers.
  - Module 3: Network routing tables (OSPF Dijkstra graphs) and database B-Tree index structures.
  - Module 4: Distributed cache architectures (Redis consistent hashing) and low-latency symbol lookup.

### Task 4: Interactive Knowledge Graph with Module Filter
- [x] Enhance SVG knowledge graph in `shared-components/course/course.js`:
  - Add module filter pills (All, Mod 1, Mod 2, Mod 3, Mod 4).
  - Add interactive node inspection panel showing concept descriptions, prerequisites, and learning outcomes when clicking any graph node.

### Task 5: Module-by-Module Gamified Quizzes
- [x] Upgrade Quiz Engine in `shared-components/course/course.js`:
  - Categorize questions by Module (Module 1, 2, 3, 4).
  - Add module tabs so students can practice module-specific quizzes.
  - Include instant feedback, correct/incorrect highlights, and KTU syllabus explanations.

### Task 6: Solved KTU University Exam Papers WITH TECHNICAL SVG FIGURES
- [x] Create comprehensive solved University questions for Modules 1 to 4:
  - Module 1: Infix to Postfix expression conversion with Stack Trace Figure (SVG) & Sparse Matrix 3-Tuple Figure (SVG).
  - Module 2: Doubly Linked List node insertion & deletion with pointer re-wiring Figure (SVG).
  - Module 3: BST node deletion (3 cases) with tree diagram Figure (SVG) & Max-Heap array mapping Figure (SVG).
  - Module 4: Hash Table linear probing with collision resolution table Figure (SVG) & Separate Chaining bucket Figure (SVG).

### Task 7: Update Pilot Course PCCST303 & Batch Course Generator
- [x] Update `courses/PCCST303/website/index.html` with enriched module tabs, SVG figures, and numerical cards.
- [x] Update `scripts/build_all_courses.py` to generate enriched module cards, SVG diagrams, and numerical solutions across all 158 course websites.
- [x] Run `py scripts/build_all_courses.py` to regenerate all course sites.

### Task 8: Verification & Automated Tests
- [x] Create `tests/test_module_features.py` to verify:
  - Presence of 3D canvas demo and module switcher.
  - Presence of numerical solutions across modules.
  - Presence of SVG figures in solved question papers.
  - Presence of module-filtered quizzes and knowledge graphs.
- [x] Run `py tests/test_module_features.py` and `py tests/test_full_platform.py`.

### Task 9: Production Deployment to Vercel via Windows Credential Manager
- [x] Read Vercel token from Windows Credential Manager (`LegacyGeneric:target=Vercel`).
- [x] Execute `npx vercel deploy --prod --yes --token <TOKEN>`.
- [x] Verify live endpoints on `https://ktu-teaching-platform.vercel.app`.
- [x] Push clean sync commit to GitHub repository `https://github.com/Janeferdinant/ktu-teaching-platform`.
