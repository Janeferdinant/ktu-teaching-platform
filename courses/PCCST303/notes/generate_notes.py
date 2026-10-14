import json
import os

notes_data = {
    "course_code": "PCCST303",
    "course_title": "DATA STRUCTURES AND ALGORITHMS",
    "faculty": "Jane Rose | Asst. Professor | CSE",
    "modules": [
        {
            "module_no": 1,
            "title": "Basic Concepts of Data Structures",
            "contact_hours": 11,
            "official_syllabus": "Definitions; Data Abstraction; Performance Analysis - Time & Space Complexity, Asymptotic Notations; Polynomial representation using Arrays, Sparse matrix (Tuple representation); Stacks and Queues - Stacks, Multi-Stacks, Queues, Circular Queues, Double Ended Queues; Evaluation of Expressions- Infix to Postfix, Evaluating Postfix Expressions.",
            "sections": [
                {
                    "title": "1.1 Data Abstraction & Abstract Data Types (ADT)",
                    "content": "A Data Structure is a systematic way of organizing, managing, and storing data in computer memory so that operations can be performed efficiently. An Abstract Data Type (ADT) is a mathematical specification of a set of data objects and the operations that can be performed on them, completely independent of any programming language implementation.\n\nKey Principles of Data Abstraction:\n1. Encapsulation: The user only interacts with the interface (public methods), while the internal memory representation (arrays, pointers) is hidden.\n2. Axiomatic Specification: Operations are defined in terms of preconditions and postconditions.",
                    "worked_examples": "Mathematical specification of Stack ADT:\nOperations: create(), push(item), pop(), top(), isEmpty(), isFull().\nAxiom: pop(push(S, x)) = x; top(push(S, x)) = x."
                },
                {
                    "title": "1.2 Performance Analysis & Asymptotic Notations",
                    "content": "Algorithm efficiency is evaluated through Time Complexity (the number of computational steps as a function of input size n) and Space Complexity (memory required beyond the input size).\n\nAsymptotic Bounds:\n1. Big-O Notation (O): Upper bound. f(n) = O(g(n)) if there exist positive constants c and n0 such that 0 <= f(n) <= c*g(n) for all n >= n0.\n2. Big-Omega Notation (Ω): Lower bound. f(n) = Ω(g(n)) if there exist positive constants c and n0 such that 0 <= c*g(n) <= f(n) for all n >= n0.\n3. Big-Theta Notation (Θ): Tight bound. f(n) = Θ(g(n)) if and only if f(n) = O(g(n)) and f(n) = Ω(g(n)).",
                    "worked_examples": "Prove 4n^2 + 7n + 12 = O(n^2):\nFor n >= 1: 7n <= 7n^2 and 12 <= 12n^2.\nTherefore, 4n^2 + 7n + 12 <= 4n^2 + 7n^2 + 12n^2 = 23n^2.\nChoose c = 23, n0 = 1. The definition holds, so 4n^2 + 7n + 12 = O(n^2)."
                },
                {
                    "title": "1.3 Polynomial Representation & Sparse Matrices (Tuple Format)",
                    "content": "Polynomials can be represented in 1D arrays using arrays of structs where each element holds `coeff` and `expo`. When polynomials are sparse (most coefficients are zero), this structure avoids allocating memory for zero terms.\n\nSparse Matrix (Tuple Representation):\nA matrix where the vast majority of elements are zero is called a sparse matrix. Representing it as a dense 2D array wastes substantial memory. In 3-tuple form, we store only non-zero elements in an array of triplets: (Row, Column, Value).\nRow 0 holds metadata: (Total_Rows, Total_Cols, NonZero_Count).\n\nFast Transpose Algorithm:\nTransposes a sparse matrix in O(cols + non_zero) time rather than O(cols * non_zero). It computes `row_terms` (frequency of elements in each column of the original matrix) and `starting_pos` (prefix sums indicating where each column will start in the transposed matrix).",
                    "worked_examples": "Given a 4x4 matrix with 3 non-zero elements at (0,1,5), (1,3,9), (3,0,2):\nTriplet Array: [ [4,4,3], [0,1,5], [1,3,9], [3,0,2] ].\nFast Transpose row_terms for cols 0..3: [1, 1, 0, 1].\nstarting_pos: [1, 2, 3, 3].\nDirect placement into transposed triplet array in O(n) passes."
                },
                {
                    "title": "1.4 Stacks, Multi-Stacks, Queues, and Deques",
                    "content": "A Stack is a Last-In-First-Out (LIFO) linear data structure. Insertion and deletion occur at a single end called `top`.\nMulti-Stacks: Dividing a single array of size N to accommodate two stacks:\n- Stack 1 grows from left to right starting at index -1.\n- Stack 2 grows from right to left starting at index N.\n- Overflow occurs only when top1 + 1 == top2, achieving 100% space utilization.\n\nA Queue is a First-In-First-Out (FIFO) linear data structure. Elements are inserted at `rear` and removed from `front`.\nCircular Queue: Solves the false overflow problem of linear queues by wrapping indices around using modulo arithmetic: `rear = (rear + 1) % MAX` and `front = (front + 1) % MAX`.\nCondition for Full: `(rear + 1) % MAX == front`.\nCondition for Empty: `front == -1`.\n\nDouble-Ended Queue (Deque): Allows insertion and deletion at both ends (Input-restricted and Output-restricted variations).",
                    "worked_examples": "Trace Circular Queue of size 4:\n1. enqueue(10) -> front=0, rear=0, arr=[10, _, _, _]\n2. enqueue(20) -> front=0, rear=1, arr=[10, 20, _, _]\n3. dequeue() -> returns 10, front=1, rear=1, arr=[_, 20, _, _]\n4. enqueue(30), enqueue(40), enqueue(50) -> rear wraps to index 0, full condition triggered."
                },
                {
                    "title": "1.5 Infix to Postfix Conversion & Postfix Expression Evaluation",
                    "content": "Arithmetic expressions are written in Infix notation (A + B). Compilers convert infix expressions to Postfix (Reverse Polish Notation, AB+) because postfix eliminates the need for parentheses and operator precedence rules during execution.\n\nInfix to Postfix Algorithm (Shunting-Yard):\n1. Scan infix token by token from left to right.\n2. If operand, append to output.\n3. If '(', push onto stack.\n4. If ')', pop and append from stack until '(' is encountered; discard '('.\n5. If operator op: while stack top has higher or equal precedence (taking associativity into account), pop to output. Push op.\n6. At end of expression, pop all remaining operators to output.\n\nPostfix Evaluation:\nUse an operand stack. When an operand is encountered, push it. When an operator is encountered, pop two operands (op2, then op1), compute `op1 operator op2`, and push the result back onto the stack.",
                    "worked_examples": "Convert: A + B * (C - D) / E\nStack trace shows '+' pushed, '*' pushed, '(' pushed, '-' pushed, ')' causes '-' to pop, '/' has equal precedence to '*' so '*' pops and '/' is pushed.\nOutput Postfix: A B C D - * E / +\n\nEvaluate Postfix: '6 2 3 + - 4 *'\nPush 6, 2, 3 -> Stack: [6, 2, 3]\nOp '+': pop 3, 2 -> 2+3=5. Push 5. Stack: [6, 5]\nOp '-': pop 5, 6 -> 6-5=1. Push 1. Stack: [1]\nPush 4. Stack: [1, 4]\nOp '*': pop 4, 1 -> 1*4=4. Push 4. Result = 4."
                }
            ],
            "exam_tips": "1. Always clearly show the operator stack and output columns step-by-step when converting expressions in the exam.\n2. In Circular Queue questions, state both empty condition (front == -1) and full condition ((rear + 1) % MAX == front).\n3. When asked for Fast Transpose, derive row_terms and starting_pos explicitly—this carries 4 out of 9 marks.",
            "summary": "Module 1 builds the theoretical and practical foundations of linear data structures, abstract data types, asymptotic analysis, polynomial representations, sparse matrices, stacks, queues, and compiler expression evaluation."
        },
        {
            "module_no": 2,
            "title": "Linked List and Memory Management",
            "contact_hours": 11,
            "official_syllabus": "Singly Linked List - Operations on Linked List, Stacks and Queues using Linked List, Polynomial representation using Linked List; Doubly Linked List; Circular Linked List; Memory allocation - First-fit, Best-fit, and Worst-fit allocation schemes; Garbage collection and compaction.",
            "sections": [
                {
                    "title": "2.1 Singly Linked List: Anatomy & Core Operations",
                    "content": "A Singly Linked List (SLL) is a sequence of dynamically allocated nodes. Each node contains a data field and a pointer (`next`) to the subsequent node. The list terminates with a `NULL` pointer.\n\nAdvantages over Arrays:\n1. Dynamic size: Grows and shrinks at runtime without pre-allocating contiguous memory blocks.\n2. Efficient insertion/deletion: Does not require shifting subsequent elements (O(1) insertion at head).\n\nCore Operations:\n- Insertion at beginning: `newNode->next = head; head = newNode;`\n- Insertion at end: Traverse to node where `curr->next == NULL`, set `curr->next = newNode`.\n- Deletion of node by value: Keep track of `prev` and `curr`. When `curr->data == key`, set `prev->next = curr->next; free(curr);`.",
                    "worked_examples": "C Node Definition:\nstruct Node {\n  int data;\n  struct Node *next;\n};\nDeletion of middle node:\nstruct Node *temp = prev->next;\nprev->next = temp->next;\nfree(temp);"
                },
                {
                    "title": "2.2 Doubly Linked List (DLL) & Circular Linked List (CLL)",
                    "content": "Doubly Linked List (DLL):\nEach node contains two pointers: `prev` (pointing to the preceding node) and `next` (pointing to the succeeding node). Allows bidirectional traversal.\nInsertion before a given node in DLL requires updating 4 pointers:\n1. `newNode->next = curr;`\n2. `newNode->prev = curr->prev;`\n3. `curr->prev->next = newNode;`\n4. `curr->prev = newNode;`\n\nCircular Linked List (CLL):\nThe last node's `next` pointer points back to the first node instead of `NULL`. Maintaining a pointer to the `last` node allows O(1) access to both the beginning (`last->next`) and the end (`last`).",
                    "worked_examples": "Circular Linked List insertion at end with `last` pointer:\nnewNode->next = last->next;\nlast->next = newNode;\nlast = newNode;\nTakes O(1) time without any loop traversal."
                },
                {
                    "title": "2.3 Dynamic Memory Allocation Strategies: First-Fit, Best-Fit, Worst-Fit",
                    "content": "Operating systems and memory managers maintain a free list of available memory blocks to satisfy dynamic allocation requests.\n\nAllocation Strategies:\n1. First-Fit: Scans the free list from the beginning and allocates the first block that is large enough. Fast (O(n)), but leaves small unused fragments at the front of memory.\n2. Best-Fit: Searches the entire free list to find the block whose size is closest to the requested size. Minimizes wasted space per allocation, but creates very tiny unusable fragments ('external fragmentation').\n3. Worst-Fit: Allocates the largest available block. Leaves large remaining fragments that can satisfy future requests, but exhausts large blocks rapidly.",
                    "worked_examples": "Memory Blocks: [100K, 500K, 200K, 300K, 600K]. Process Request: 212K.\n- First-Fit: Chooses 500K (wastes 288K)\n- Best-Fit: Chooses 300K (wastes 88K)\n- Worst-Fit: Chooses 600K (wastes 388K)"
                },
                {
                    "title": "2.4 Garbage Collection & Memory Compaction",
                    "content": "Garbage Collection is the automatic reclamation of dynamically allocated memory that is no longer reachable by the program.\n\nTechniques:\n1. Reference Counting: Every object maintains a counter of active references. When the count drops to 0, memory is immediately reclaimed. Drawback: Fails to detect circular references (A points to B and B points to A).\n2. Mark-Sweep Algorithm: Two phases:\n   - Mark Phase: Traverses all objects reachable from root pointers (globals, stack frames) and marks them as active.\n   - Sweep Phase: Scans the entire heap; any unmarked block is returned to the free list.\n\nMemory Compaction:\nConsolidates all free memory fragments into one contiguous block by shifting active allocated blocks to one end of memory and updating all internal memory pointers. Eliminates external fragmentation.",
                    "worked_examples": "Mark-Sweep trace:\nHeap has nodes {A, B, C, D, E}. Root points to A. A points to B and C. D points to E and E points to D.\nMark phase visits: A, B, C.\nSweep phase identifies D and E as unvisited and reclaims them to free list, successfully resolving the circular reference."
                }
            ],
            "exam_tips": "1. When writing linked list insertion/deletion code, remember to check for empty list (head == NULL) and 1-element list edge cases.\n2. In memory management numericals, draw the memory block layout diagram with address boundaries and process allocations.\n3. State the difference between internal and external fragmentation clearly.",
            "summary": "Module 2 covers dynamic linear data structures (singly, doubly, circular linked lists), dynamic stacks and queues, polynomial manipulation, and system memory management (allocation heuristics, garbage collection, and compaction)."
        },
        {
            "module_no": 3,
            "title": "Trees and Graphs",
            "contact_hours": 11,
            "official_syllabus": "Trees :- Representation Of Trees; Binary Trees - Types and Properties, Binary Tree Representation, Tree Operations, Tree Traversals; Expression Trees; Binary Search Trees - Binary Search Tree Operations; Binary Heaps - Binary Heap Operations, Priority Queue. Graphs :- Definitions; Representation of Graphs; Depth First Search and Breadth First Search; Applications of Graphs - Single Source All Destination.",
            "sections": [
                {
                    "title": "3.1 Tree Terminology & Binary Tree Properties",
                    "content": "A Tree is a non-linear hierarchical data structure consisting of nodes connected by directed edges. A tree contains one `root` node with degree 0 in-degree, and every other node has exactly one parent.\n\nBinary Tree Types:\n1. Full (Strict) Binary Tree: Every node has either 0 or 2 children.\n2. Complete Binary Tree: All levels are completely filled except possibly the last level, where nodes are as far left as possible.\n3. Perfect Binary Tree: All internal nodes have 2 children and all leaf nodes are at the same depth.\n4. Skewed Binary Tree: Every node has only a left child (left-skewed) or only a right child (right-skewed).\n\nMathematical Theorems:\n- In any binary tree, the maximum number of nodes at level i is 2^i.\n- In a non-empty binary tree with n nodes and e edges: e = n - 1.\n- Theorem: In any binary tree, the number of leaf nodes n0 is related to the number of nodes of degree 2 (n2) by: n0 = n2 + 1.",
                    "worked_examples": "Proof of n0 = n2 + 1:\nLet total nodes = n = n0 + n1 + n2.\nTotal edges = e = n - 1 = n0 + n1 + n2 - 1.\nAlso, counting edges from children: e = 0*n0 + 1*n1 + 2*n2 = n1 + 2*n2.\nEquating: n0 + n1 + n2 - 1 = n1 + 2*n2 => n0 = n2 + 1. (Proved)"
                },
                {
                    "title": "3.2 Binary Tree Traversals & Expression Trees",
                    "content": "Traversals systematically visit every node in a binary tree exactly once.\n\nDepth-First Recursive Traversals:\n1. Inorder (LDR): Traverse Left subtree, visit Data (root), traverse Right subtree. (Yields sorted order in a BST).\n2. Preorder (DLR): Visit Data (root), traverse Left subtree, traverse Right subtree.\n3. Postorder (LRD): Traverse Left subtree, traverse Right subtree, visit Data (root).\n\nExpression Trees:\nA binary tree where internal nodes are operators and leaf nodes are operands.\n- Inorder traversal yields Infix expression.\n- Preorder traversal yields Prefix expression.\n- Postorder traversal yields Postfix expression.",
                    "worked_examples": "Given tree with root '+' having left child 'A' and right subtree '*' with children 'B' and 'C':\n- Inorder: A + B * C\n- Preorder: + A * B C\n- Postorder: A B C * +"
                },
                {
                    "title": "3.3 Binary Search Trees (BST) & Heaps",
                    "content": "A Binary Search Tree (BST) is a binary tree where for every node X:\n- All keys in the left subtree of X are strictly less than key(X).\n- All keys in the right subtree of X are strictly greater than key(X).\n\nBST Deletion (3 Cases):\n- Case 1: Node is a leaf. Simply delete it and set parent's pointer to NULL.\n- Case 2: Node has one child. Bypass the node by linking parent directly to the child.\n- Case 3: Node has two children. Replace node's key with its Inorder Successor (smallest node in right subtree) or Inorder Predecessor, then recursively delete that successor/predecessor node.\n\nBinary Heap:\nA complete binary tree satisfying the heap-order property:\n- Max-Heap: Every parent node is greater than or equal to its children (`A[parent(i)] >= A[i]`).\n- Min-Heap: Every parent node is less than or equal to its children (`A[parent(i)] <= A[i]`).\nRepresented compactly in 1D array: Parent = floor(i/2), Left = 2i, Right = 2i + 1.\nHeapify takes O(log n) time. Building a heap takes O(n) time.",
                    "worked_examples": "BST Deletion Case 3:\nDelete node 50 from BST where 50 has left child 30 and right child 70 (with left child 60).\nInorder successor of 50 is 60. Copy 60 into root, then delete 60 from right subtree."
                },
                {
                    "title": "3.4 Graphs: Representations, BFS, DFS & Applications",
                    "content": "A Graph G = (V, E) consists of a set of vertices V and edges E.\n\nRepresentations:\n1. Adjacency Matrix: 2D array A[V][V]. Fast edge lookup O(1), but takes O(V^2) space—wasteful for sparse graphs.\n2. Adjacency List: Array of linked lists where list[i] contains all neighbors of vertex i. Takes O(V + E) space.\n\nGraph Traversals:\n- Breadth-First Search (BFS): Uses a Queue. Explores neighbors level by level. Computes shortest path in unweighted graphs.\n- Depth-First Search (DFS): Uses a Stack (or recursion). Explores as deep as possible along each branch before backtracking.\n\nApplication:\nSingle-Source All-Destination shortest paths in unweighted graphs can be computed in O(V + E) time using BFS.",
                    "worked_examples": "BFS on graph with vertices {A, B, C, D, E} starting at A:\n1. Queue = [A], Visited = {A}\n2. Pop A, visit neighbors B, C. Queue = [B, C], Visited = {A, B, C}\n3. Pop B, visit neighbor D. Queue = [C, D], Visited = {A, B, C, D}\n4. Pop C, visit neighbor E. Queue = [D, E], Visited = {A, B, C, D, E}\nResulting BFS Traversal: A, B, C, D, E."
                }
            ],
            "exam_tips": "1. In tree questions, always reconstruct the tree from traversals by identifying the root from Preorder, then partitioning Inorder into left and right subtrees.\n2. In BST deletion of a two-child node, always specify whether you used Inorder Successor or Predecessor.\n3. In Heap questions, show intermediate trees for both bubbling up and trickling down.",
            "summary": "Module 3 explores non-linear hierarchical trees, binary search trees, binary heaps, priority queues, and graph representations with BFS, DFS, and shortest path algorithms."
        },
        {
            "module_no": 4,
            "title": "Sorting and Searching",
            "contact_hours": 11,
            "official_syllabus": "Sorting Techniques :- Selection Sort, Insertion Sort, Quick Sort, Merge Sort, Heap Sort, Radix Sort. Searching Techniques :- Linear Search, Binary Search, Hashing - Hashing functions : Mid square, Division, Folding, Digit Analysis; Collision Resolution : Linear probing, Quadratic Probing, Double hashing, Open hashing.",
            "sections": [
                {
                    "title": "4.1 Comparison-Based Sorting Algorithms",
                    "content": "Sorting arranges elements in ascending or descending order. Comparison-based sorting has a theoretical lower bound of Ω(n log n).\n\nAlgorithms:\n1. Selection Sort: Finds minimum element in unsorted portion and swaps with first unsorted element. O(n^2) all cases. Unstable.\n2. Insertion Sort: Inserts each element into its sorted position among predecessor elements. O(n) best case (already sorted), O(n^2) worst case. Stable and adaptive.\n3. Quick Sort: Selects a pivot, partitions array such that elements < pivot are on left and elements > pivot are on right, and recursively sorts sub-arrays. Average O(n log n), worst-case O(n^2) when pivot is minimum/maximum. In-place.\n4. Merge Sort: Divide and conquer. Divides array into halves, recursively sorts them, and merges sorted halves. Guaranteed O(n log n) all cases. Stable, but requires O(n) auxiliary memory.\n5. Heap Sort: Builds Max-Heap in O(n) time, then repeatedly swaps root with last element and heapifies down. Guaranteed O(n log n) time and in-place O(1) space. Unstable.",
                    "worked_examples": "Quick Sort Lomuto Partition Trace on [38, 27, 43, 3, 9, 82, 10]:\nPivot = 10.\nScan compares elements with pivot 10.\nSwaps 38 with 3, 27 with 9.\nPlace pivot: [3, 9, 10, 38, 27, 82, 43]. Left sub-array [3, 9], right sub-array [38, 27, 82, 43]."
                },
                {
                    "title": "4.2 Non-Comparison Sorting: Radix Sort",
                    "content": "Radix Sort sorts elements digit by digit, from least significant digit (LSD) to most significant digit (MSD), using a stable sub-routine (like Counting Sort) for each digit position.\n\nComplexity:\nTime Complexity: O(d * (n + b)), where d is number of digits, n is number of elements, and b is the base (e.g. 10 for decimal numbers).\nOutperforms comparison sorts when keys are integers of bounded length.",
                    "worked_examples": "Trace on [170, 045, 075, 090, 802, 024, 002, 066]:\n- Pass 1 (Units digit): [170, 090, 802, 002, 024, 045, 075, 066]\n- Pass 2 (Tens digit): [802, 002, 024, 045, 066, 170, 075, 090]\n- Pass 3 (Hundreds digit): [002, 024, 045, 066, 075, 090, 170, 802] -> Sorted!"
                },
                {
                    "title": "4.3 Searching Techniques: Linear vs Binary Search",
                    "content": "1. Linear Search: Sequentially inspects each element from index 0 to n-1. Works on unsorted data. Time: O(n).\n2. Binary Search: Operates on sorted arrays. Compares target with middle element `mid = low + (high - low)/2` and halves the search space in each iteration.\nRecurrence: T(n) = T(n/2) + O(1) => Time: O(log n).",
                    "worked_examples": "Binary Search on [2, 5, 8, 12, 16, 23, 38, 56, 72, 91] for target 23:\n- Iter 1: low=0, high=9, mid=4 (val=16). 23 > 16 => low = 5.\n- Iter 2: low=5, high=9, mid=7 (val=56). 23 < 56 => high = 6.\n- Iter 3: low=5, high=6, mid=5 (val=23). 23 == 23 => Key found at index 5 in 3 comparisons!"
                },
                {
                    "title": "4.4 Hashing: Hash Functions & Collision Resolution",
                    "content": "Hashing maps arbitrary keys to fixed table indices using a hash function `h(k)`, achieving average O(1) search and insertion.\n\nHash Functions:\n1. Division Method: `h(k) = k mod m` (choose m to be a prime number not close to a power of 2).\n2. Mid-Square Method: Square the key `k^2` and extract the middle r digits.\n3. Folding Method: Partition key into parts of table-size length and sum them.\n4. Digit Analysis: Extract digits having the most uniform distribution.\n\nCollision Resolution Strategies:\n1. Open Addressing (Closed Hashing):\n   - Linear Probing: `h(k, i) = (h'(k) + i) mod m`. Causes Primary Clustering (long continuous runs of occupied slots).\n   - Quadratic Probing: `h(k, i) = (h'(k) + c1*i + c2*i^2) mod m`. Eliminates primary clustering but can suffer secondary clustering.\n   - Double Hashing: `h(k, i) = (h1(k) + i * h2(k)) mod m`. Optimal open addressing.\n2. Separate Chaining (Open Hashing):\n   Each table slot is a linked list of records that hash to the same index. Handles high load factors gracefully.",
                    "worked_examples": "Insert keys [12, 22, 32, 42] into table size m=10 using Division method and Linear Probing:\n- h(12) = 2 -> slot 2\n- h(22) = 2 (collision) -> (2+1)%10 = 3 -> slot 3\n- h(32) = 2 (collision) -> (2+2)%10 = 4 -> slot 4\n- h(42) = 2 (collision) -> (2+3)%10 = 5 -> slot 5"
                }
            ],
            "exam_tips": "1. In Hashing numericals, show the probe sequence clearly for each key when collisions occur.\n2. In Quick Sort, explicitly write the recurrence relations for best case, average case, and worst case.\n3. In stability comparisons, use duplicate values (e.g. 5a, 5b) to demonstrate whether relative order is preserved.",
            "summary": "Module 4 provides a deep comparative analysis of sorting algorithms (Selection, Insertion, Quick, Merge, Heap, Radix), logarithmic binary searching, and hash tables with collision handling mechanisms."
        }
    ]
}

out_dir = r"c:\Users\Asus\Downloads\SYLLABUS\courses\PCCST303\notes"
os.makedirs(out_dir, exist_ok=True)
out_file = os.path.join(out_dir, "module_notes.json")
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(notes_data, f, indent=2)

print(f"Successfully generated comprehensive module notes for PCCST303 ({len(notes_data['modules'])} modules).")
