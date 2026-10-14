import json
import os

plan_data = {
    "course_code": "PCCST303",
    "course_title": "DATA STRUCTURES AND ALGORITHMS",
    "semester": "S3",
    "regulation": "KTU B.Tech Curriculum 2024 Scheme",
    "credits": 4,
    "ltpr": "3:1:0:0",
    "official_contact_hours": 44,
    "target_hours": 46,
    "hours_discrepancy_reconciled": True,
    "discrepancy_explanation": "Official KTU syllabus prescribes 44 contact hours (11 hours per module across 4 modules). Reconciled to 46 hours by scheduling 44 in-depth lecture hours plus 2 dedicated tutorial/revision and KTU model exam analysis sessions.",
    "modules_breakdown": {
        "module_1": {"title": "Basic Concepts of Data Structures", "hours": 11},
        "module_2": {"title": "Linked List and Memory Management", "hours": 11},
        "module_3": {"title": "Trees and Graphs", "hours": 11},
        "module_4": {"title": "Sorting and Searching", "hours": 11},
        "revision_and_eval": {"title": "Consolidated Revision & Examination Workshop", "hours": 2}
    },
    "lectures": []
}

lecture_definitions = [
    # Module 1 (11 Hours)
    (1, 1, "Introduction to Data Structures & Data Abstraction",
     "Understand classification of data structures and ADT principles", "Basic C programming",
     "Chalk & Board + Slide presentation", "ADTs definition, mathematical specification of Stack ADT",
     "Array-based implementation of integer list", "Database records, browser tab history",
     "Identify ADT operations for a music playlist", "3-question MCQ on primitive vs non-primitive",
     "Horowitz Section 1.1-1.3", "Ability to define ADTs formally", "Write ADT specification for a shopping cart"),
    
    (2, 1, "Performance Analysis: Space & Time Complexity",
     "Formulate time and space complexity for imperative algorithms", "Algebraic summation & loops",
     "Mathematical derivation on board", "Step count method for matrix addition & multiplication",
     "Profiler in Python/C for loop execution time", "Cloud computing compute charges based on runtime",
     "Calculate exact step count of nested loop snippet", "Find Big-O for given recurrence code",
     "Cormen Chapter 3", "Derive step count and frequency counts", "Calculate time complexity of polynomial evaluation"),

    (3, 1, "Asymptotic Notations: Big-O, Big-Omega, Big-Theta",
     "Master formal definitions and proofs of asymptotic bounds", "Limits and inequalities",
     "Formal mathematical proof on board", "Prove 3n^2 + 5n = O(n^2) and find c, n0",
     "Interactive growth rate curve plotter (O(1) to O(2^n))", "Algorithm selection in high-frequency trading",
     "Plot f(n) vs c*g(n) for n=1 to 20", "Determine whether 2^(n+1) = O(2^n)",
     "Horowitz Section 1.4", "Formulate formal proofs for bounding constants", "Prove or disprove: f(n) = O(g(n)) implies g(n) = Omega(f(n))"),

    (4, 1, "Polynomial Representation using Arrays",
     "Design and implement 1D array representation for polynomials", "Array indexing and structs",
     "Board trace of polynomial array representation", "Degree & coefficient array vs structured term array",
     "C code demonstrating polynomial input and display", "Computer algebra systems (SymPy, Mathematica)",
     "Represent P(x) = 4x^5 + 3x^2 - 7 in memory", "MCQ on space wastage in sparse polynomials",
     "Horowitz Section 2.2", "Implement polynomial representation in C", "Write algorithm to add two 1D polynomials"),

    (5, 1, "Polynomial Addition using Arrays",
     "Implement polynomial addition algorithm and analyze complexity", "While loops and conditionals",
     "Step-by-step trace table on board", "Dry run with P1 = 3x^4 + 2x^2 + 1 and P2 = 5x^3 - 2x^2 + 4",
     "Live execution of polynomial add function in C", "Signal processing superposition of waves",
     "Code review and edge-case handling (zero coefficients)", "Quiz on time complexity of polynomial addition",
     "Horowitz Section 2.3", "Write robust polynomial arithmetic code", "Extend polynomial addition to polynomial multiplication"),

    (6, 1, "Sparse Matrix Representation: Tuple Form",
     "Understand memory inefficiency of dense matrices and 3-tuple format", "2D arrays and pointers",
     "Draw 2D grid vs 3-tuple table on board", "Convert 5x6 sparse matrix to 3-column tuple array",
     "Memory comparison script (bytes dense vs tuple)", "Google PageRank link graph matrix storage",
     "Convert a given 6x6 matrix with 4 non-zero elements into tuple format", "Check triplet array bounds question",
     "Horowitz Section 2.4", "Represent sparse matrices in 3-tuple form", "Calculate memory saved when sparsity is 90%"),

    (7, 1, "Sparse Matrix Operations: Fast Transpose",
     "Derive fast transpose algorithm with O(rows + non-zero) time", "Frequency counting and prefix sums",
     "Board derivation of row_terms and starting_pos arrays", "Trace fast transpose step-by-step with sample matrix",
     "Animated visualization of fast transpose index mapping", "3D graphics coordinate transforms and rendering",
     "Compute starting_pos array for a 4-row matrix", "Numerical on transpose time complexity comparison",
     "Horowitz Section 2.4.2", "Explain fast transpose and its linear-time advantage", "Trace transpose on a 5-element triplet array"),

    (8, 1, "Stack ADT: Operations, Array Implementation & Multi-Stacks",
     "Implement Stack ADT with push/pop and partition array for multi-stacks", "Pointers and array bounds",
     "Draw stack push/pop stack pointer state diagrams", "Derive boundary checks for 2 stacks in a single array",
     "C sandbox with push(), pop(), peek(), isEmpty()", "Function call stack in OS and undo history",
     "Simulate 2-stack array with 6 operations", "Predict top1 and top2 pointer values after ops",
     "Horowitz Section 3.1", "Implement multi-stacks in single array", "Write C function to test if stack has reached capacity"),

    (9, 1, "Queue ADT: Linear Queue & Circular Queue",
     "Diagnose false overflow in linear queues and implement circular queue", "Modulo arithmetic",
     "Clockwise circle pointer diagrams on board", "Calculate (rear + 1) % MAX and (front + 1) % MAX conditions",
     "Interactive circular queue visualizer with enqueue/dequeue", "CPU process scheduling queues, printer spoolers",
     "Trace circular queue of size 5 through 8 mixed operations", "Question on empty vs full queue condition",
     "Horowitz Section 3.2-3.3", "Implement circular queue with zero false overflows", "Implement Double-Ended Queue (Deque) operations"),

    (10, 1, "Infix to Postfix Conversion using Stacks",
     "Master operator precedence, associativity, and shunting-yard algorithm", "Operator precedence rules",
     "Full trace table with Symbol, Stack, Output columns", "Convert A + B * (C - D) / E ^ F to postfix on board",
     "Live parser running Infix to Postfix C code", "Compiler expression parsing and bytecode generation",
     "Convert (A + B) * C - D / E to Postfix in student notebook", "Solve KTU 2023 3-mark question on postfix conversion",
     "Lipschutz Chapter 6", "Convert arbitrary infix expressions without errors", "Convert infix expression with nested parentheses to postfix"),

    (11, 1, "Evaluation of Postfix Expressions using Stacks",
     "Execute postfix evaluation algorithm using operand stack", "Stack manipulation",
     "Step-by-step operand stack evaluation table", "Evaluate postfix string '5 3 + 8 2 - * 4 /' on board",
     "Interactive postfix calculator in JavaScript/C", "Reverse Polish Notation (RPN) in HP calculators and PostScript",
     "Evaluate '6 2 3 + - 3 8 2 / + * 2 ^ 3 +' in pairs", "KTU Model Question: trace stack states during evaluation",
     "Lipschutz Chapter 6", "Evaluate postfix expressions step-by-step", "Write complete C program for postfix evaluation"),

    # Module 2 (11 Hours)
    (12, 2, "Introduction to Linked Lists: Dynamic Memory vs Arrays",
     "Contrast contiguous vs non-contiguous allocation and node anatomy", "Pointers and dynamic memory (malloc/free)",
     "Memory layout diagrams on board with addresses", "Structure definition of `struct Node { int data; struct Node *next; }`",
     "Memory allocation visualizer showing heap blocks", "Music playlists, blockchain transaction ledgers",
     "Draw pointer links for inserting at head of list", "MCQ on overhead of pointer storage",
     "Horowitz Section 4.1", "Understand pointer chaining and dynamic node creation", "Write C code to dynamically create and link 3 nodes"),

    (13, 2, "Singly Linked List: Insertion Operations",
     "Implement insertion at beginning, end, and specific position", "Pointer assignments and traversal",
     "Step-by-step pointer manipulation diagrams", "Trace inserting node 25 between node 20 and node 30",
     "Live demo of insertAtBeginning(), insertAtEnd(), insertAtPos()", "Real-time task scheduling in embedded kernels",
     "Identify correct order of pointer updates without losing list head", "Find bug in faulty pointer assignment code",
     "Horowitz Section 4.2", "Safely manipulate pointers without memory leaks", "Write C function `insert_after_val(head, key, val)`"),

    (14, 2, "Singly Linked List: Deletion and Traversal",
     "Implement deletion of first, last, and keyed nodes with memory freeing", "Pointer manipulation and free()",
     "Board diagrams of reconnecting previous to next and free()", "Trace deletion of target key in a 5-node list",
     "Live debugging of segmentation faults during node deletion", "Cache eviction mechanisms (LRU cache node removal)",
     "Write edge-case checks (deleting from 1-node list or empty list)", "KTU PYQ: Write algorithm to delete node by value",
     "Horowitz Section 4.2", "Write bug-free deletion routines with proper free()", "Implement search and display operations on linked list"),

    (15, 2, "Stack and Queue Implementation using Linked List",
     "Construct dynamic stacks and queues with O(1) push/pop/enqueue/dequeue", "Head pointer and tail pointer updates",
     "Board diagrams comparing array bounds vs unbounded linked structures", "Trace linked stack push/pop and linked queue enqueue/dequeue",
     "Live C sandbox executing dynamic stack and queue", "Operating system interrupt handling queues",
     "Implement linked queue dequeue() checking for empty queue", "Analyze time and space complexity of linked stack vs array stack",
     "Horowitz Section 4.3", "Build dynamic stacks and queues without fixed capacities", "Write C program to reverse a linked list using stack"),

    (16, 2, "Polynomial Representation & Addition using Linked List",
     "Implement polynomial addition with linked lists of varying degrees", "Node structures with coef, expo, next",
     "Board trace of advancing pointers p1 and p2 based on exponents", "Trace adding (5x^4 + 3x^2) and (4x^4 + 2x^3 - x^2 + 7)",
     "Execution of polynomial addition C program with linked list", "Symbolic math engines and scientific computing",
     "Compare time/space complexity between array and linked list polynomial", "Write comparison logic for p1->expo == p2->expo",
     "Horowitz Section 4.4", "Implement linked polynomial addition algorithm", "Write algorithm to multiply two linked polynomials"),

    (17, 2, "Doubly Linked List (DLL): Anatomy & Insertion",
     "Master bidirectional traversal and 4-pointer update insertion", "Two pointers: prev and next",
     "Board diagrams showing prev and next pointer reassignment", "Derive 4 pointer updates for inserting node in DLL",
     "Interactive DLL visualizer showing forward and backward links", "Web browser back and forward button navigation",
     "Order the 4 pointer assignments to insert new node before key", "MCQ on pointer updates in DLL",
     "Horowitz Section 4.8", "Execute two-way pointer updates without orphan links", "Write C function for `insert_before_node_dll()`"),

    (18, 2, "Doubly Linked List: Deletion & Bidirectional Traversal",
     "Implement safe deletion in DLL handling head, middle, and tail nodes", "DLL node pointers and boundary cases",
     "Trace deleting middle node: `p->prev->next = p->next; p->next->prev = p->prev;`", "Trace deletion of tail node in 4-node DLL",
     "Interactive visualizer of DLL node removal and heap cleanup", "Photoshop undo/redo history states",
     "Simulate bidirectional traversal printing list in reverse", "KTU Model Question: Compare DLL vs Singly Linked List",
     "Horowitz Section 4.8", "Write robust DLL deletion with zero dangling pointers", "Implement function to check if DLL is palindrome"),

    (19, 2, "Circular Linked List (CLL): Singly & Doubly",
     "Understand wrap-around traversal and circular boundary invariants", "Tail pointing to head",
     "Circle pointer diagrams with `last` pointer advantage", "Trace insert at front vs insert at end using only `last` pointer",
     "Animation of circular round-robin traversal", "Round-Robin CPU scheduling, multiplayer game turns",
     "Determine termination condition for loop traversing a circular list", "Explain why keeping pointer to `last` is better than `head`",
     "Horowitz Section 4.5", "Implement circular linked list with `last` pointer", "Implement Josephus problem simulation using CLL"),

    (20, 2, "Memory Allocation Strategies: First-Fit, Best-Fit, Worst-Fit",
     "Analyze contiguous dynamic memory partitioning algorithms", "Free list linked structure",
     "Board simulation table with memory blocks and process requests", "Allocate processes P1(212K), P2(417K), P3(112K), P4(426K) in blocks",
     "Interactive memory allocator simulator comparing the 3 strategies", "Operating System virtual memory management (malloc heap)",
     "Calculate external fragmentation for each strategy on given workload", "KTU PYQ: Numerical on First-fit vs Best-fit allocation",
     "Silberschatz / Samanta Chapter 4", "Choose optimal memory allocation scheme for workloads", "Calculate total wasted space for worst-fit on 5 requests"),

    (21, 2, "Garbage Collection Techniques: Reference Counting & Mark-Sweep",
     "Understand automated memory reclamation and circular reference pitfalls", "Graph reachability from root set",
     "Draw object reference graph and trace reference count increments/decrements", "Trace Mark-Sweep two-phase traversal on heap graph",
     "Visual animation of mark phase and sweep compaction phase", "Java Virtual Machine (JVM) and Python garbage collectors",
     "Identify cycle in reference counting that causes memory leak", "Compare stop-the-world latency vs memory footprint",
     "Samanta Chapter 4", "Explain reference counting and mark-sweep algorithms", "Write brief comparative note on JVM GC algorithms"),

    (22, 2, "Memory Compaction & Module 2 Consolidation",
     "Analyze internal and external fragmentation and relocation compaction", "Base and limit registers",
     "Board diagrams showing sliding compaction and pointer adjustment", "Calculate memory addresses after moving allocated blocks to one end",
     "Live simulation of sliding compaction defragmenting memory", "Disk defragmentation, SSD wear leveling, heap compaction",
     "Group exercise: Solve 2024 KTU model question on memory compaction", "10-question MCQ quiz on Linked Lists & Memory",
     "Samanta Chapter 4", "Formulate compaction algorithms to eliminate fragmentation", "Revise all Module 2 derivations and algorithms"),

    # Module 3 (11 Hours)
    (23, 3, "Trees: Terminology, Representation & Properties",
     "Understand hierarchical tree structures, root, degree, depth, height", "Discrete structures and graphs",
     "Tree anatomy diagram on board with formal annotations", "Calculate height, depth, levels, and degree of given tree",
     "Canvas tree renderer displaying dynamic node hierarchy", "File system directory hierarchies, DOM tree in web browsers",
     "Identify parent, sibling, ancestor, and descendant sets for given node", "Formula quiz: Maximum nodes at level i = 2^i",
     "Horowitz Section 5.1", "Calculate tree metrics and formal properties", "Draw file system tree structure of `/usr/local/bin`"),

    (24, 3, "Binary Trees: Types (Strict, Complete, Perfect, Skewed)",
     "Distinguish binary tree varieties and their mathematical bounds", "Binary relations and powers of 2",
     "Comparative board diagrams of the 5 binary tree classes", "Prove minimum and maximum height for N nodes in binary tree",
     "Interactive binary tree generator showing complete vs full trees", "Decision trees in machine learning, heap data structures",
     "Check if given array represents complete binary tree", "KTU PYQ: Differentiate between complete and full binary tree",
     "Horowitz Section 5.2", "Prove structural theorems for binary trees", "Prove that in any non-empty binary tree, n0 = n2 + 1"),

    (25, 3, "Binary Tree Representation: Array vs Linked Representation",
     "Implement binary tree using 1D sequential array and linked struct", "Formulas: LeftChild=2i, RightChild=2i+1, Parent=i/2",
     "Sequential array index mapping vs pointer nodes diagram", "Map binary tree to array indices and compute empty slot wastage",
     "C code executing linked binary tree creation", "Compact array heaps vs flexible pointer trees",
     "Map a skewed binary tree of 5 nodes to array and calculate wasted cells", "Find parent of node at index 14 in complete binary tree",
     "Horowitz Section 5.2", "Select appropriate representation based on tree balance", "Write C struct definition for linked binary tree node"),

    (26, 3, "Binary Tree Traversals: Inorder, Preorder, Postorder",
     "Master depth-first recursive traversals (LDR, DLR, LRD)", "Recursion and call stack",
     "Board trace of recursive traversal paths with order numbers", "Compute Inorder, Preorder, and Postorder sequences for sample tree",
     "Step-by-step traversal visualizer highlighting visited nodes", "Syntax tree generation, expression evaluation, directory size",
     "Given a tree diagram, write the three traversal sequences", "Reconstruct binary tree from Inorder and Preorder sequences",
     "Horowitz Section 5.3", "Execute recursive tree traversals without hesitation", "Write recursive C functions for inorder, preorder, postorder"),

    (27, 3, "Expression Trees: Construction & Evaluation",
     "Construct binary expression trees from postfix expressions using stack", "Stacks and binary trees",
     "Step-by-step stack of tree nodes diagram on board", "Trace building expression tree for 'a b + c d e + * *'",
     "Live interactive expression tree builder and evaluator", "SQL query optimizer expression trees, spreadsheet formulas",
     "Derive prefix expression from expression tree preorder traversal", "KTU Model Question: Construct expression tree for given postfix",
     "Lipschutz Chapter 7", "Construct expression trees and evaluate them recursively", "Write algorithm to evaluate expression tree recursively"),

    (28, 3, "Binary Search Trees (BST): Definition & Search Operation",
     "Understand BST property (Left < Root < Right) and O(h) search", "Binary search logic",
     "Board diagrams illustrating search path comparisons", "Trace searching key 42 in BST with 10 nodes (best vs worst case)",
     "Interactive BST search simulator highlighting visited nodes", "Database B-tree root indexing, symbol tables in compilers",
     "Trace search path for missing key and identify termination condition", "Analyze best-case O(log n) vs worst-case O(n) skewed search",
     "Horowitz Section 5.5", "Implement recursive and iterative BST search", "Write C function `search_bst(root, key)`"),

    (29, 3, "Binary Search Tree: Insertion and Deletion",
     "Implement BST insertion and 3 deletion cases (0, 1, 2 children)", "Pointers and tree node replacement",
     "Board diagrams of replacing node with Inorder Successor/Predecessor", "Trace deleting root node with two children from BST",
     "Live sandbox running BST insert and delete operations", "Dynamic database index management",
     "Step-by-step deletion of node with 2 children in student workbook", "KTU PYQ: Delete node 50 from given BST and redraw tree",
     "Horowitz Section 5.5", "Execute BST deletion correctly under all 3 cases", "Write complete C program for BST insertion and deletion"),

    (30, 3, "Binary Heaps: Max Heap, Min Heap & Heapify",
     "Understand complete binary tree heap-order property and heapify", "Array representation of binary trees",
     "Board trace of bubbling up (insertion) and trickling down (deletion)", "Convert array [4, 10, 3, 5, 1] into Max-Heap using heapify",
     "Animated heap visualizer simultaneously showing array and tree", "Operating system priority scheduling, streaming top-K items",
     "Draw Max-Heap after inserting element 15", "KTU PYQ: Construct Max-Heap from given sequence of numbers",
     "Cormen Chapter 6", "Perform heapify and maintain heap invariants", "Write C functions for `insert_heap()` and `heapify()`"),

    (31, 3, "Priority Queues using Heaps",
     "Implement Priority Queue ADT with O(log n) enqueue and dequeue", "Binary Heaps",
     "Comparison table: Unordered array vs Ordered array vs Heap", "Trace extractMax() and restore heap property on board",
     "Priority queue simulation with emergency room triage data", "Network packet prioritization, hospital patient scheduling",
     "Compute runtime comparison table for PQ implementations", "Solve priority queue extraction problem",
     "Horowitz Section 5.6", "Implement high-performance Priority Queue with heaps", "Write priority queue application for process scheduling"),

    (32, 3, "Graphs: Definitions, Adjacency Matrix & Adjacency List",
     "Master graph terminology (directed, undirected, weighted, cyclic)", "2D arrays and linked lists",
     "Board diagrams comparing matrix memory (V^2) vs list memory (V+E)", "Draw adjacency matrix and adjacency list for 5-vertex graph",
     "Interactive graph visualizer displaying matrix and list views", "Social networks (Facebook friendship graph, Twitter followers)",
     "Convert given directed graph into adjacency list", "Calculate memory difference for graph with V=1000, E=2000",
     "Horowitz Section 6.1", "Select optimal graph representation based on density", "Write C representation for adjacency list graph"),

    (33, 3, "Graph Traversals (BFS & DFS) and Shortest Path Application",
     "Implement Breadth First Search (Queue) and Depth First Search (Stack)", "Queues, Stacks, Graphs",
     "Trace queue states for BFS and recursion stack for DFS on board", "Trace single-source shortest path on unweighted graph using BFS",
     "Interactive animated BFS and DFS traversal on 8-node graph", "GPS navigation route finding, web crawlers, maze solving",
     "Write BFS and DFS traversal order starting from vertex A", "KTU PYQ: Single source shortest path using BFS trace",
     "Horowitz Section 6.2-6.3", "Implement BFS and DFS algorithms in C", "Write complete BFS program to find shortest path in unweighted graph"),

    # Module 4 (11 Hours)
    (34, 4, "Introduction to Sorting: Selection Sort and Insertion Sort",
     "Analyze comparison sorts, in-place behavior, and stability", "Nested loops and swapping",
     "Trace pass-by-pass array states on board", "Dry run Selection Sort and Insertion Sort on [29, 10, 14, 37, 13]",
     "Animated sorting visualizer comparing swap counts in real-time", "Sorting student rosters by roll number, poker hand card sorting",
     "Count comparisons in Insertion Sort on sorted vs reverse-sorted array", "MCQ on stability: why Selection Sort is unstable",
     "Horowitz Section 7.1-7.2", "Implement Selection and Insertion sort with complexity analysis", "Write C program for Insertion Sort and count shifts"),

    (35, 4, "Divide and Conquer Sorting: Quick Sort Algorithm",
     "Master partitioning strategy, pivot selection, and recursive division", "Divide and conquer, recursion",
     "Step-by-step Lomuto/Hoare partition diagram on board", "Trace Quick Sort on [35, 33, 42, 10, 14, 19, 27, 44] with pivot=35",
     "Interactive Quick Sort step debugger showing sub-array boundaries", "V8 JavaScript engine `Array.prototype.sort()` internal sort",
     "Simulate partition function on 6-element array", "Calculate worst-case recursion depth when array is already sorted",
     "Cormen Chapter 7", "Implement Quick Sort and explain worst-case O(n^2) mitigation", "Write Quick Sort with randomized pivot selection in C"),

    (36, 4, "Quick Sort Complexity & Best/Worst Case Analysis",
     "Derive recurrence relations T(n) = 2T(n/2) + O(n) and T(n) = T(n-1) + O(n)", "Recurrence relations and Master theorem",
     "Recursion tree diagrams on board for balanced vs skewed partitions", "Derive O(n log n) average case and O(n^2) worst case mathematically",
     "Benchmark comparison: Quick Sort on random vs sorted input", "Database query optimization and distributed sorting",
     "Identify worst-case input configurations for first-element pivot", "KTU PYQ: Derive average-case time complexity of Quick Sort",
     "Cormen Chapter 7", "Mathematically defend Quick Sort performance characteristics", "Explain 3 strategies to avoid worst-case in Quick Sort"),

    (37, 4, "Merge Sort: Divide, Conquer, and Merge Algorithm",
     "Implement 2-way Merge Sort with guaranteed O(n log n) runtime", "Recursion and auxiliary arrays",
     "Tree of array subdivisions and 2-pointer merge on board", "Trace merging two sorted arrays [2, 5, 8] and [3, 6, 9]",
     "Interactive visualizer of Merge Sort subdivision and merge passes", "External sorting of massive multi-gigabyte server log files",
     "Trace auxiliary array copies during Merge Sort on 8 numbers", "Prove Merge Sort stability and O(n) auxiliary space overhead",
     "Cormen Chapter 2", "Implement robust Merge Sort with external space awareness", "Write C program for `merge(arr, l, m, r)` function"),

    (38, 4, "Heap Sort: In-Place O(n log n) Sorting",
     "Construct in-place sorting algorithm using Max-Heap structure", "Binary Heaps and array indexing",
     "Board diagrams of buildMaxHeap followed by repeated root-to-end swaps", "Trace Heap Sort on array [12, 11, 13, 5, 6, 7]",
     "Interactive Heap Sort visualizer showing heap shrink and sorted tail grow", "Embedded automotive control systems needing O(1) space guarantee",
     "Draw intermediate heap state after 2 largest items are extracted", "Compare Heap Sort vs Quick Sort vs Merge Sort trade-off table",
     "Cormen Chapter 6", "Implement Heap Sort with in-place O(1) auxiliary space", "Write complete C program for Heap Sort"),

    (39, 4, "Radix Sort: Non-Comparative Distribution Sort",
     "Understand digit-by-digit distribution sort and LSD/MSD techniques", "Counting sort and buckets",
     "Board table showing 10 bucket passes for units, tens, hundreds digits", "Trace Radix Sort on [170, 45, 75, 90, 802, 24, 2, 66]",
     "Animated bucket sorting visualizer sorting 3-digit integers", "Card sorting machines, post office ZIP code routing",
     "Determine number of passes needed for given maximum key length d", "Analyze O(d * (n + b)) complexity and compare with comparison sorts",
     "Horowitz Section 7.7", "Implement Radix Sort for integer collections", "Write algorithm for Radix Sort on 4-digit numbers"),

    (40, 4, "Searching Techniques: Linear Search & Binary Search",
     "Analyze sequential search vs logarithmic binary search on sorted data", "Search intervals and mid calculations",
     "Decision tree for binary search on board with mid-point pointer moves", "Derive T(n) = T(n/2) + 1 recurrence showing O(log n) time",
     "Interactive search race visualizer comparing comparisons between Linear vs Binary", "Dictionary lookups, database index lookups",
     "Trace binary search for key 23 in 15-element sorted array", "KTU Model Question: Compare Linear Search and Binary Search",
     "Horowitz Section 7.1", "Implement recursive and iterative Binary Search safely", "Explain bug in `mid = (low + high) / 2` (integer overflow)"),

    (41, 4, "Hashing Fundamentals: Hash Functions & Properties",
     "Understand direct address tables, hash collisions, and hash functions", "Modular arithmetic and bit manipulation",
     "Draw key-to-index mapping diagrams with collision demonstrations", "Calculate hash indices for keys using Division, Mid-square, and Folding",
     "Interactive hash function sandbox showing distribution across buckets", "Compiler symbol tables, cryptographic digital signatures, cache keys",
     "Compute hash addresses for keys [1234, 5678, 9101] using Folding method", "Analyze uniform hashing criteria and avalanche effect",
     "Horowitz Section 7.8", "Design collision-resistant hash functions", "Calculate hash values using Mid-square method for 4 keys"),

    (42, 4, "Collision Resolution: Open Addressing (Linear & Quadratic Probing)",
     "Implement open addressing and analyze primary and secondary clustering", "Linear probing formulas: `h(k, i) = (h'(k) + i) % m`",
     "Step-by-step hash table cell allocation diagrams on board", "Insert keys [25, 35, 45, 15] into table of size 10 using linear probing",
     "Interactive collision visualizer illustrating probe sequences", "In-memory database caching (Redis dictionary internals)",
     "Calculate probe count for successful and unsuccessful search", "Trace quadratic probing `h(k, i) = (h'(k) + c1*i + c2*i^2) % m`",
     "Horowitz Section 7.8.2", "Implement Linear and Quadratic probing collision handlers", "Solve numerical problem on 7-slot hash table with linear probing"),

    (43, 4, "Collision Resolution: Double Hashing & Open Hashing (Chaining)",
     "Master secondary hash function probing and separate chaining linked lists", "Linked lists and secondary hash functions",
     "Board diagrams comparing open addressing vs separate chaining", "Trace inserting 8 keys into chained hash table with table size 5",
     "Interactive chained hash table visualizer with expandable linked chains", "Git commit hash database, Java `HashMap` internal architecture",
     "Calculate load factor alpha = n/m and expected search time", "KTU PYQ: Numerical on separate chaining vs double hashing",
     "Cormen Chapter 11", "Implement separate chaining using linked list buckets", "Write C program for hash table with separate chaining"),

    (44, 4, "Comprehensive Comparison of Sorting & Searching Algorithms",
     "Synthesize time, space, stability, and adaptability of all techniques", "All algorithm complexity bounds",
     "Master summary comparison matrix on board covering 7 sorting algorithms", "Solve algorithmic selection case studies based on constraints",
     "Live benchmark dashboard sorting 10,000 integers with all algorithms", "Software engineering system design interview trade-offs",
     "Match real-world scenario to optimal sorting/searching algorithm", "Comprehensive 10-question MCQ test on Module 4",
     "Horowitz Chapter 7", "Select the optimal algorithm for arbitrary constraints", "Complete algorithmic decision tree cheat-sheet"),

    # Revision & Assessment Sessions (2 Hours)
    (45, 4, "Revision Workshop: Derivations, Proofs & Numerical Problems",
     "Consolidate core derivations and numerical problem-solving skills", "Modules 1 through 4",
     "Interactive problem solving on board across all 4 modules", "Solve 4 complex numericals (Tree traversals, Fast Transpose, Hashing, Sorting)",
     "Live KTU previous-year exam question walkthrough", "Academic excellence and semester exam preparation",
     "Students solve selected Part B numerical in exam conditions", "Rapid-fire 5-question oral quiz on edge-case behaviors",
     "KTU S3 Syllabus & QP Archive", "Master all high-yield numerical topics for the semester exam", "Complete KTU Model Exam Part A revision sheet"),

    (46, 4, "Model Examination & KTU Examination Strategy Session",
     "Evaluate student exam readiness and analyze sample answer papers", "Complete syllabus",
     "Deconstruct 60-mark KTU exam structure and mark distribution strategy", "Review high-scoring model answers and common student errors",
     "Online mock exam simulation with instant score reporting", "Preparation for University Examination and placement technical tests",
     "Mock exam writing and peer review of answer presentation", "Full 60-mark Model Examination assessment",
     "KTU S3 Official Exam Papers", "Confidence to achieve top grade in University examination", "Final review of personal study revision notes")
]

for item in lecture_definitions:
    lec = {
        "lecture_no": item[0],
        "module_no": item[1],
        "topic": item[2],
        "learning_objective": item[3],
        "prerequisite_knowledge": item[4],
        "teaching_method": item[5],
        "board_work_or_numerical": item[6],
        "practical_demonstration": item[7],
        "real_life_application": item[8],
        "student_activity": item[9],
        "quiz_or_assessment": item[10],
        "learning_resource": item[11],
        "expected_outcome": item[12],
        "homework_or_assignment": item[13]
    }
    plan_data["lectures"].append(lec)

out_dir = r"c:\Users\Asus\Downloads\SYLLABUS\courses\PCCST303\teaching-plan"
os.makedirs(out_dir, exist_ok=True)
out_file = os.path.join(out_dir, "teaching_plan_46h.json")
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(plan_data, f, indent=2)

print(f"Successfully generated 46-hour teaching plan for PCCST303 ({len(plan_data['lectures'])} lectures).")
