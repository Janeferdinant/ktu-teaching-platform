/**
 * Academic Teaching Platform - Advanced Multi-Module Interactive Engine
 * Jane Rose | Asst. Professor | CSE
 */

let currentTab = 'overview';
let teachingPlanData = null;
let currentSlideIdx = 0;
let courseSlidesData = [];
let active3DModule = 1;
let animFrameId = null;
let rotAngle = 0;

document.addEventListener('DOMContentLoaded', async () => {
  setupTabs();
  initEmbeddedSlides();
  await loadTeachingPlan();
  setup3DDemo(1);
  setupQuizEngine('all');
  setupKnowledgeGraph('all');
});

// Tab Navigation
function setupTabs() {
  const tabBtns = document.querySelectorAll('.nav-tab-btn');
  tabBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const target = btn.dataset.tab;
      switchTab(target);
    });
  });
}

function switchTab(tabId) {
  currentTab = tabId;
  document.querySelectorAll('.nav-tab-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.tab === tabId);
  });
  document.querySelectorAll('.tab-section').forEach(sec => {
    sec.classList.toggle('active', sec.id === `sec-${tabId}`);
  });

  if (tabId === 'demos') {
    setup3DDemo(active3DModule);
  }
}

// ==========================================
// 1. MULTI-MODULE 3D INTERACTIVE VISUALIZER
// ==========================================

function switch3DModule(modNo) {
  active3DModule = modNo;
  document.querySelectorAll('#demo-module-pills .module-pill').forEach(p => {
    p.classList.toggle('active', parseInt(p.dataset.mod) === modNo);
  });
  setup3DDemo(modNo);
}

function setup3DDemo(modNo) {
  const canvas = document.getElementById('demo-3d-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  if (animFrameId) cancelAnimationFrame(animFrameId);

  // Resize canvas to match container
  const rect = canvas.parentElement.getBoundingClientRect();
  canvas.width = rect.width || 800;
  canvas.height = 360;

  if (modNo === 1) render3DStackDemo(ctx, canvas);
  else if (modNo === 2) render3DMemoryHeapDemo(ctx, canvas);
  else if (modNo === 3) render3DRotatingTreeDemo(ctx, canvas);
  else if (modNo === 4) render3DHashMatrixDemo(ctx, canvas);
}

// Module 1: 3D Stack / Queue Isometric Blocks
let stackItems = [14, 28, 42, 65, 89];
function render3DStackDemo(ctx, canvas) {
  const hud = document.getElementById('demo-hud');
  if (hud) hud.innerText = `Module 1: 3D Isometric Stack (Size: ${stackItems.length} / 7) • Top: ${stackItems[stackItems.length - 1] || 'Empty'}`;

  ctx.clearRect(0, 0, canvas.width, canvas.height);
  const cx = canvas.width / 2;
  const baseY = canvas.height - 50;

  // Draw 3D Base Pedestal
  drawIsoBlock(ctx, cx, baseY, 140, 70, 16, '#1e293b', '#0f172a', '#334155');

  // Draw Stack Elements with 3D Depth
  stackItems.forEach((val, idx) => {
    const y = baseY - 20 - idx * 36;
    const colorTop = '#38bdf8';
    const colorLeft = '#0284c7';
    const colorRight = '#0369a1';
    drawIsoBlock(ctx, cx, y, 100, 50, 24, colorTop, colorLeft, colorRight, `[${idx}] ${val}`);
  });
}

function push3DStack() {
  if (active3DModule !== 1) switch3DModule(1);
  if (stackItems.length >= 7) {
    alert('Stack Overflow! Maximum 7 blocks reached.');
    return;
  }
  stackItems.push(Math.floor(Math.random() * 89) + 10);
  setup3DDemo(1);
}

function pop3DStack() {
  if (active3DModule !== 1) switch3DModule(1);
  if (stackItems.length === 0) {
    alert('Stack Underflow! No blocks to pop.');
    return;
  }
  stackItems.pop();
  setup3DDemo(1);
}

// Module 2: 3D Dynamic Memory Allocation Heap
let heapBlocks = [
  { size: 120, allocated: true, id: "Proc_A", color: "#34d399" },
  { size: 80, allocated: false, id: "FREE HOLE", color: "#64748b" },
  { size: 160, allocated: true, id: "Proc_B", color: "#818cf8" },
  { size: 100, allocated: false, id: "FREE HOLE", color: "#64748b" },
  { size: 140, allocated: true, id: "Proc_C", color: "#f43f5e" }
];

function render3DMemoryHeapDemo(ctx, canvas) {
  const hud = document.getElementById('demo-hud');
  if (hud) hud.innerText = `Module 2: 3D Memory Heap Allocation • 5 Segments • First-Fit & Best-Fit Simulation`;

  ctx.clearRect(0, 0, canvas.width, canvas.height);
  let startX = 60;
  const startY = canvas.height / 2;

  heapBlocks.forEach(b => {
    const w = (b.size / 600) * (canvas.width - 140);
    draw3DMemorySegment(ctx, startX, startY, w, 55, 30, b);
    startX += w + 12;
  });
}

function allocateMemoryBlock() {
  if (active3DModule !== 2) switch3DModule(2);
  const freeIdx = heapBlocks.findIndex(b => !b.allocated);
  if (freeIdx !== -1) {
    heapBlocks[freeIdx].allocated = true;
    heapBlocks[freeIdx].id = `Proc_${String.fromCharCode(68 + Math.floor(Math.random() * 5))}`;
    heapBlocks[freeIdx].color = '#fbbf24';
  } else {
    // Reset
    heapBlocks.forEach((b, i) => { if (i % 2 === 1) b.allocated = false; });
  }
  setup3DDemo(2);
}

// Module 3: 3D Rotating Binary Search Tree / Graph
const tree3DNodes = [
  { val: 50, x: 0, y: -90, z: 0 },
  { val: 30, x: -90, y: -20, z: -40 },
  { val: 70, x: 90, y: -20, z: 40 },
  { val: 20, x: -140, y: 60, z: -20 },
  { val: 40, x: -40, y: 60, z: -60 },
  { val: 60, x: 40, y: 60, z: 60 },
  { val: 85, x: 140, y: 60, z: 20 }
];

const tree3DEdges = [
  [0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]
];

function render3DRotatingTreeDemo(ctx, canvas) {
  const hud = document.getElementById('demo-hud');
  if (hud) hud.innerText = `Module 3: 3D Rotating Binary Search Tree Mesh • Real-Time Depth Projection & Inorder (20-30-40-50-60-70-85)`;

  function loop() {
    rotAngle += 0.015;
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const cx = canvas.width / 2;
    const cy = canvas.height / 2 + 10;
    const cosA = Math.cos(rotAngle);
    const sinA = Math.sin(rotAngle);

    // Project nodes
    const projected = tree3DNodes.map(n => {
      const rx = n.x * cosA - n.z * sinA;
      const rz = n.x * sinA + n.z * cosA;
      const scale = 250 / (250 + rz);
      return {
        val: n.val,
        px: cx + rx * scale,
        py: cy + n.y * scale,
        scale: scale,
        depth: rz
      };
    });

    // Draw edges
    ctx.lineWidth = 2;
    tree3DEdges.forEach(([u, v]) => {
      const p1 = projected[u];
      const p2 = projected[v];
      ctx.strokeStyle = 'rgba(56, 189, 248, 0.45)';
      ctx.beginPath();
      ctx.moveTo(p1.px, p1.py);
      ctx.lineTo(p2.px, p2.py);
      ctx.stroke();
    });

    // Sort by depth
    projected.sort((a, b) => b.depth - a.depth);

    // Draw nodes
    projected.forEach(p => {
      const r = Math.max(12, 20 * p.scale);
      const grad = ctx.createRadialGradient(p.px - r*0.3, p.py - r*0.3, r*0.1, p.px, p.py, r);
      grad.addColorStop(0, '#a5f3fc');
      grad.addColorStop(0.7, '#0284c7');
      grad.addColorStop(1, '#082f49');

      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.arc(p.px, p.py, r, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = '#38bdf8';
      ctx.stroke();

      ctx.fillStyle = '#ffffff';
      ctx.font = `bold ${Math.floor(11 * p.scale)}px sans-serif`;
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText(p.val, p.px, p.py);
    });

    if (active3DModule === 3) {
      animFrameId = requestAnimationFrame(loop);
    }
  }
  loop();
}

// Module 4: 3D Hash Table Bucket Matrix
let hashBuckets = [
  { bucket: 0, keys: [40, 70] },
  { bucket: 1, keys: [11] },
  { bucket: 2, keys: [22, 52, 92] },
  { bucket: 3, keys: [] },
  { bucket: 4, keys: [14, 84] }
];

function render3DHashMatrixDemo(ctx, canvas) {
  const hud = document.getElementById('demo-hud');
  if (hud) hud.innerText = `Module 4: 3D Hash Table Matrix • Chaining Buckets (h(k) = k % 5) • Load Factor: 1.6`;

  ctx.clearRect(0, 0, canvas.width, canvas.height);
  const cx = 100;
  const startY = 60;

  hashBuckets.forEach((b, idx) => {
    const y = startY + idx * 56;
    // Draw 3D Bucket Slot
    drawIsoBlock(ctx, cx, y, 70, 35, 18, '#fbbf24', '#d97706', '#b45309', `B[${b.bucket}]`);

    // Draw Chained Keys extending horizontally with 3D depth
    b.keys.forEach((k, kIdx) => {
      const kX = cx + 90 + kIdx * 80;
      // Draw arrow
      ctx.strokeStyle = '#f59e0b';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(kX - 45, y);
      ctx.lineTo(kX - 22, y);
      ctx.stroke();

      drawIsoBlock(ctx, kX, y, 50, 26, 16, '#38bdf8', '#0284c7', '#0369a1', `${k}`);
    });
  });
}

// Helper: 3D Isometric Block
function drawIsoBlock(ctx, x, y, w, h, depth, topColor, leftColor, rightColor, label = '') {
  const hw = w / 2;
  const hh = h / 2;

  // Top Face
  ctx.fillStyle = topColor;
  ctx.beginPath();
  ctx.moveTo(x, y - hh);
  ctx.lineTo(x + hw, y);
  ctx.lineTo(x, y + hh);
  ctx.lineTo(x - hw, y);
  ctx.closePath();
  ctx.fill();
  ctx.strokeStyle = 'rgba(255,255,255,0.2)';
  ctx.stroke();

  // Left Face
  ctx.fillStyle = leftColor;
  ctx.beginPath();
  ctx.moveTo(x - hw, y);
  ctx.lineTo(x, y + hh);
  ctx.lineTo(x, y + hh + depth);
  ctx.lineTo(x - hw, y + depth);
  ctx.closePath();
  ctx.fill();
  ctx.stroke();

  // Right Face
  ctx.fillStyle = rightColor;
  ctx.beginPath();
  ctx.moveTo(x, y + hh);
  ctx.lineTo(x + hw, y);
  ctx.lineTo(x + hw, y + depth);
  ctx.lineTo(x, y + hh + depth);
  ctx.closePath();
  ctx.fill();
  ctx.stroke();

  if (label) {
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 10px monospace';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(label, x, y);
  }
}

// Helper: 3D Memory Segment
function draw3DMemorySegment(ctx, x, y, w, h, depth, block) {
  // Front
  ctx.fillStyle = block.allocated ? block.color : '#334155';
  ctx.fillRect(x, y, w, h);
  ctx.strokeStyle = '#000';
  ctx.strokeRect(x, y, w, h);

  // Top 3D Extrusion
  ctx.fillStyle = block.allocated ? '#6ee7b7' : '#475569';
  ctx.beginPath();
  ctx.moveTo(x, y);
  ctx.lineTo(x + 16, y - depth * 0.4);
  ctx.lineTo(x + w + 16, y - depth * 0.4);
  ctx.lineTo(x + w, y);
  ctx.closePath();
  ctx.fill();
  ctx.stroke();

  // Right 3D Extrusion
  ctx.fillStyle = block.allocated ? '#059669' : '#1e293b';
  ctx.beginPath();
  ctx.moveTo(x + w, y);
  ctx.lineTo(x + w + 16, y - depth * 0.4);
  ctx.lineTo(x + w + 16, y + h - depth * 0.4);
  ctx.lineTo(x + w, y + h);
  ctx.closePath();
  ctx.fill();
  ctx.stroke();

  // Text Label
  ctx.fillStyle = '#ffffff';
  ctx.font = 'bold 10px sans-serif';
  ctx.textAlign = 'center';
  ctx.fillText(block.id, x + w / 2, y + h / 2 - 4);
  ctx.font = '9px monospace';
  ctx.fillText(`${block.size} KB`, x + w / 2, y + h / 2 + 10);
}

// ==========================================
// 2. KNOWLEDGE GRAPH WITH MODULE FILTER & INSPECTOR
// ==========================================

const kgNodesData = [
  { id: "mod1_adt", label: "Data Abstraction & ADT", mod: 1, bloom: "K2 (Understand)", desc: "Separation of mathematical interface specification from implementation logic.", formula: "ADT = (Values, Operations)" },
  { id: "mod1_asymp", label: "Asymptotic Bounds (O, Ω, Θ)", mod: 1, bloom: "K3 (Apply)", desc: "Formal mathematical bounding of growth rates for algorithmic efficiency.", formula: "f(n) <= c * g(n) ∀ n >= n0" },
  { id: "mod1_stack", label: "Stack & Polish Parsing", mod: 1, bloom: "K3 (Apply)", desc: "LIFO evaluation of arithmetic expressions without parentheses.", formula: "Postfix: AB+C*" },
  { id: "mod2_sll", label: "Singly & Doubly Linked Lists", mod: 2, bloom: "K3 (Apply)", desc: "Dynamic pointer-chained nodes supporting non-contiguous memory utilization.", formula: "Node = [Data | Next | Prev]" },
  { id: "mod2_mem", label: "Dynamic Heap Allocation", mod: 2, bloom: "K2 (Understand)", desc: "First-Fit, Best-Fit, and Worst-Fit memory block assignment algorithms.", formula: "ExtFrag = TotalFree - MaxBlock" },
  { id: "mod3_bst", label: "Binary Search Trees", mod: 3, bloom: "K3 (Apply)", desc: "Hierarchical binary trees where left < root < right for logarithmic lookup.", formula: "Height = O(log n)" },
  { id: "mod3_heap", label: "Binary Heaps & Priority Queues", mod: 3, bloom: "K3 (Apply)", desc: "Complete binary tree satisfying heap-order property stored in flat arrays.", formula: "Parent = i/2, Left = 2i" },
  { id: "mod4_sort", label: "Quick & Merge Sorting", mod: 4, bloom: "K4 (Analyze)", desc: "Divide-and-conquer comparison sorting algorithms with optimal runtimes.", formula: "T(n) = 2T(n/2) + O(n)" },
  { id: "mod4_hash", label: "Hash Tables & Probing", mod: 4, bloom: "K3 (Apply)", desc: "Key-to-index mapping with linear/quadratic collision resolution.", formula: "h(k, i) = (h'(k) + i) % m" }
];

function setupKnowledgeGraph(filterMod = 'all') {
  const svg = document.getElementById('kg-svg');
  if (!svg) return;

  const filtered = filterMod === 'all' ? 
    kgNodesData : 
    kgNodesData.filter(n => n.mod === parseInt(filterMod));

  // Render SVG nodes
  let nodesHtml = '';
  const total = filtered.length;
  const radius = 135;
  const cx = 450;
  const cy = 180;

  // Center hub
  nodesHtml += `
    <circle cx="${cx}" cy="${cy}" r="38" fill="url(#kg-grad)" />
    <text x="${cx}" y="${cy + 5}" text-anchor="middle" fill="#000" font-weight="bold" font-size="11">COURSE CORE</text>
  `;

  filtered.forEach((n, idx) => {
    const angle = (idx / total) * Math.PI * 2;
    const nx = cx + radius * Math.cos(angle);
    const ny = cy + radius * Math.sin(angle);
    const color = n.mod === 1 ? '#38bdf8' : n.mod === 2 ? '#818cf8' : n.mod === 3 ? '#34d399' : '#fbbf24';

    nodesHtml += `
      <line x1="${cx}" y1="${cy}" x2="${nx}" y2="${ny}" stroke="rgba(255,255,255,0.18)" stroke-width="2" />
      <g style="cursor:pointer;" onclick="inspectKGNode('${n.id}')">
        <circle cx="${nx}" cy="${ny}" r="28" fill="rgba(15,23,42,0.8)" stroke="${color}" stroke-width="2.5" />
        <text x="${nx}" y="${ny + 4}" text-anchor="middle" fill="#fff" font-size="9" font-weight="600">M${n.mod}</text>
      </g>
    `;
  });

  svg.innerHTML = `
    <defs>
      <linearGradient id="kg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#38bdf8" />
        <stop offset="100%" stop-color="#818cf8" />
      </linearGradient>
    </defs>
    ${nodesHtml}
  `;

  // Update pills
  document.querySelectorAll('#kg-module-pills .module-pill').forEach(p => {
    p.classList.toggle('active', p.dataset.mod === String(filterMod));
  });
}

function filterKGModule(mod) {
  setupKnowledgeGraph(mod);
}

function inspectKGNode(nodeId) {
  const node = kgNodesData.find(n => n.id === nodeId);
  const panel = document.getElementById('kg-inspector-panel');
  if (!node || !panel) return;

  panel.style.display = 'block';
  panel.innerHTML = `
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
      <span class="glass-badge">Module ${node.mod} • ${node.bloom}</span>
      <button class="glass-btn" onclick="this.parentElement.parentElement.style.display='none'" style="padding:2px 8px; font-size:0.75rem;">✕ Close</button>
    </div>
    <h3 style="margin:0 0 0.5rem; color:var(--accent-primary); font-size:1.15rem;">${node.label}</h3>
    <p style="color:var(--text-secondary); margin:0 0 0.6rem; font-size:0.92rem; line-height:1.5;">${node.desc}</p>
    <div style="font-family:var(--font-mono); background:rgba(0,0,0,0.4); padding:6px 10px; border-radius:6px; font-size:0.85rem; color:#38bdf8;">
      Mathematical Formulation: ${node.formula}
    </div>
  `;
}

// ==========================================
// 3. MODULE-BY-MODULE GAMIFIED QUIZ ENGINE
// ==========================================

const allQuizzesData = [
  // Module 1
  {
    mod: 1,
    q: "Which asymptotic notation specifies the tight bound (both upper and lower) for an algorithm's running time?",
    options: ["Big-O (O)", "Big-Omega (Ω)", "Big-Theta (Θ)", "Little-o (o)"],
    answer: 2,
    expl: "Big-Theta (Θ) defines a tight bound: c1 * g(n) <= f(n) <= c2 * g(n) for all n >= n0."
  },
  {
    mod: 1,
    q: "In the conversion of infix expression A + B * C to postfix using a stack, what is the output?",
    options: ["A B C * +", "A B + C *", "* + A B C", "A B C + *"],
    answer: 0,
    expl: "Multiplication (*) has higher precedence than addition (+), so B and C are multiplied first, then added to A."
  },
  // Module 2
  {
    mod: 2,
    q: "What is the primary memory overhead of a Doubly Linked List compared to a Singly Linked List?",
    options: ["One extra data pointer per node", "One extra backward pointer (prev) per node", "Requires contiguous heap allocation", "Double the garbage collection cycles"],
    answer: 1,
    expl: "Each node in a doubly linked list stores an additional previous (prev) pointer, requiring 4 or 8 additional bytes per node."
  },
  {
    mod: 2,
    q: "Which dynamic memory allocation heuristic leaves the largest remaining free fragment after allocation?",
    options: ["First-Fit", "Best-Fit", "Worst-Fit", "Next-Fit"],
    answer: 2,
    expl: "Worst-Fit allocates the largest available hole, ensuring the leftover block is as large as possible for future requests."
  },
  // Module 3
  {
    mod: 3,
    q: "In a Binary Search Tree, what is the maximum number of pointers that must be re-linked when deleting a node with two children?",
    options: ["None", "Replaced with inorder successor and 2 pointer rewires", "Complete tree rebalancing", "Only the root pointer"],
    answer: 1,
    expl: "Deleting a node with two children involves copying the inorder successor's value and deleting the successor (which has at most one child)."
  },
  {
    mod: 3,
    q: "For a binary heap represented as an array with 1-based indexing, where is the parent of node i located?",
    options: ["2 * i", "2 * i + 1", "Math.floor(i / 2)", "i - 1"],
    answer: 2,
    expl: "In a 1-indexed binary heap array, Parent(i) = Math.floor(i / 2), LeftChild(i) = 2*i, RightChild(i) = 2*i + 1."
  },
  // Module 4
  {
    mod: 4,
    q: "What is the primary disadvantage of Linear Probing in hash collision resolution?",
    options: ["Infinite loops", "Primary Clustering", "Secondary Clustering", "Inability to hash strings"],
    answer: 1,
    expl: "Linear probing suffers from Primary Clustering, where occupied slots group together in contiguous blocks, degrading search time to O(n)."
  },
  {
    mod: 4,
    q: "What is the worst-case time complexity of Quick Sort when an unbalanced partition is chosen repeatedly?",
    options: ["O(n log n)", "O(n)", "O(n²)", "O(log n)"],
    answer: 2,
    expl: "When the pivot chosen is consistently the smallest or largest element, the recurrence becomes T(n) = T(n-1) + O(n), which resolves to O(n²)."
  }
];

function setupQuizEngine(filterMod = 'all') {
  const container = document.getElementById('quiz-container');
  if (!container) return;

  const filtered = filterMod === 'all' ? 
    allQuizzesData : 
    allQuizzesData.filter(q => q.mod === parseInt(filterMod));

  container.innerHTML = filtered.map((quiz, qIdx) => `
    <div class="quiz-card">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.6rem;">
        <span class="glass-badge" style="font-size:0.75rem;">Module ${quiz.mod} Exam MCQ</span>
        <span style="font-size:0.8rem; color:var(--text-muted);">Bloom's Taxonomy K3</span>
      </div>
      <div style="font-weight: 700; color: var(--text-primary); margin-bottom: 0.8rem; font-size:1.02rem;">
        Q${qIdx + 1}: ${quiz.q}
      </div>
      <div>
        ${quiz.options.map((opt, oIdx) => `
          <div class="quiz-option" onclick="checkQuizAnswer(this, ${qIdx}, ${oIdx}, ${quiz.answer})">
            ${opt}
          </div>
        `).join('')}
      </div>
      <div id="quiz-expl-${qIdx}" style="display:none; margin-top:10px; font-size:0.88rem; color:var(--text-muted); line-height:1.5;">
        ${quiz.expl}
      </div>
    </div>
  `).join('');

  // Update pills
  document.querySelectorAll('#quiz-module-pills .module-pill').forEach(p => {
    p.classList.toggle('active', p.dataset.mod === String(filterMod));
  });
}

function filterQuizModule(mod) {
  setupQuizEngine(mod);
}

function checkQuizAnswer(el, qIdx, chosen, correct) {
  const parent = el.parentElement;
  if (parent.dataset.answered) return;
  parent.dataset.answered = 'true';

  const options = parent.querySelectorAll('.quiz-option');
  if (chosen === correct) {
    el.classList.add('correct');
  } else {
    el.classList.add('incorrect');
    options[correct].classList.add('correct');
  }
  const expl = document.getElementById(`quiz-expl-${qIdx}`);
  if (expl) expl.style.display = 'block';
}

// ==========================================
// 4. EMBEDDED SLIDES PLAYER
// ==========================================

function initEmbeddedSlides() {
  const container = document.getElementById('embedded-slide-content');
  if (!container) return;

  if (window.COURSE_SLIDES && Array.isArray(window.COURSE_SLIDES)) {
    courseSlidesData = window.COURSE_SLIDES;
  }

  if (courseSlidesData.length > 0) {
    renderEmbeddedSlide(0);
  }

  document.addEventListener('keydown', (e) => {
    if (currentTab === 'slides') {
      if (e.key === 'ArrowRight' || e.key === ' ') nextEmbeddedSlide();
      if (e.key === 'ArrowLeft') prevEmbeddedSlide();
    }
  });
}

function renderEmbeddedSlide(idx) {
  const container = document.getElementById('embedded-slide-content');
  if (!container || !courseSlidesData || !courseSlidesData[idx]) return;

  currentSlideIdx = idx;
  const s = courseSlidesData[idx];
  const total = courseSlidesData.length;

  container.innerHTML = `
    <div>
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.8rem;">
        <span class="glass-badge">${s.module || 'Overview'}</span>
        <span style="font-size: 0.85rem; color: var(--text-muted);">${s.badge || ''}</span>
      </div>
      <h2 class="slide-viewer-title">${s.title}</h2>
      <div class="slide-viewer-body">
        <ul>
          ${(s.points || []).map(p => `<li>${p}</li>`).join('')}
        </ul>
        ${s.code ? `<div class="slide-viewer-code">${s.code}</div>` : ''}
      </div>
    </div>
    <div class="slide-viewer-controls">
      <button class="glass-btn" onclick="prevEmbeddedSlide()" ${idx === 0 ? 'disabled style="opacity:0.4; cursor:not-allowed;"' : ''}>
        &larr; Previous Slide
      </button>
      <span style="font-weight: 600; color: var(--accent-primary);">Slide ${idx + 1} of ${total}</span>
      <button class="glass-btn glass-btn-primary" onclick="nextEmbeddedSlide()" ${idx === total - 1 ? 'disabled style="opacity:0.4; cursor:not-allowed;"' : ''}>
        Next Slide &rarr;
      </button>
    </div>
  `;
}

function prevEmbeddedSlide() {
  if (currentSlideIdx > 0) renderEmbeddedSlide(currentSlideIdx - 1);
}

function nextEmbeddedSlide() {
  if (currentSlideIdx < courseSlidesData.length - 1) renderEmbeddedSlide(currentSlideIdx + 1);
}

// ==========================================
// 5. 46-HOUR TEACHING PLAN LOADER
// ==========================================

async function loadTeachingPlan() {
  const tbody = document.getElementById('plan-tbody');
  if (!tbody) return;

  try {
    let url = 'teaching-plan/teaching_plan_46h.json';
    if (window.location.protocol === 'file:') {
      url = '../teaching-plan/teaching_plan_46h.json';
    } else {
      const pathname = window.location.pathname;
      const base = pathname.endsWith('/') ? pathname : pathname + '/';
      url = `${base}teaching-plan/teaching_plan_46h.json`;
    }
    const res = await fetch(url);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    teachingPlanData = await res.json();
    renderTeachingPlan(teachingPlanData.lectures || []);
  } catch (e) {
    try {
      const res2 = await fetch('../teaching-plan/teaching_plan_46h.json');
      if (res2.ok) {
        teachingPlanData = await res2.json();
        renderTeachingPlan(teachingPlanData.lectures || []);
      }
    } catch (e2) {
      console.warn('Teaching plan fallback loaded:', e2);
    }
  }
}

function renderTeachingPlan(lectures) {
  const tbody = document.getElementById('plan-tbody');
  if (!tbody || !lectures.length) return;
  tbody.innerHTML = lectures.map(l => `
    <tr>
      <td style="font-weight:700; color:var(--accent-primary);">Lec ${l.lecture_no}</td>
      <td><span class="glass-badge" style="font-size:0.7rem;">Mod ${l.module_no}</span></td>
      <td style="font-weight:600; color:var(--text-primary);">${l.topic}</td>
      <td>${l.learning_objective}</td>
      <td><span style="color:var(--accent-secondary);">${l.teaching_method}</span></td>
      <td style="font-family:var(--font-mono); font-size:0.82rem;">${l.board_work_or_numerical}</td>
      <td>${l.real_life_application}</td>
    </tr>
  `).join('');
}
