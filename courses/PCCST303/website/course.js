/**
 * PCCST303: Data Structures & Algorithms - Interactive Course Script
 * Jane Rose | Asst. Professor | CSE
 */

// Global State
let currentTab = 'overview';
let teachingPlanData = null;
let moduleNotesData = null;
let speechSynth = window.speechSynthesis;
let currentUtterance = null;
let isSpeaking = false;

// Initialize
document.addEventListener('DOMContentLoaded', async () => {
  setupTabs();
  await loadTeachingPlan();
  setupSortingVisualizer();
  setupStackVisualizer();
  setupTreeVisualizer();
  setupQuizEngine();
  setupKnowledgeGraph();
  setupVoiceNarration();
});

// Tab Navigation
function setupTabs() {
  const tabBtns = document.querySelectorAll('.nav-tab-btn');
  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
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
  window.scrollTo({ top: 400, behavior: 'smooth' });
}

// 46-Hour Teaching Plan Loader
async function loadTeachingPlan() {
  try {
    const res = await fetch('../teaching-plan/teaching_plan_46h.json');
    teachingPlanData = await res.json();
    renderTeachingPlan(teachingPlanData.lectures);
  } catch (e) {
    console.error('Failed to load teaching plan:', e);
  }
}

function renderTeachingPlan(lectures) {
  const tbody = document.getElementById('plan-tbody');
  if (!tbody) return;
  tbody.innerHTML = lectures.map(l => `
    <tr>
      <td style="font-weight:700; color:var(--accent-primary);">Lec ${l.lecture_no}</td>
      <td><span class="glass-badge" style="font-size:0.7rem;">Mod ${l.module_no}</span></td>
      <td style="font-weight:600; color:var(--text-primary);">${l.topic}</td>
      <td>${l.learning_objective}</td>
      <td><span style="color:var(--accent-secondary);">${l.teaching_method}</span></td>
      <td style="font-family:var(--font-mono); font-size:0.82rem;">${l.board_work_or_numerical}</td>
      <td>${l.real_life_application}</td>
      <td>
        <input type="checkbox" onchange="toggleLecStatus(${l.lecture_no}, this.checked)" title="Mark completed">
      </td>
    </tr>
  `).join('');
  updatePlanStats();
}

function filterPlanByModule(modNo) {
  if (!teachingPlanData) return;
  if (modNo === 'all') {
    renderTeachingPlan(teachingPlanData.lectures);
  } else {
    const filtered = teachingPlanData.lectures.filter(l => l.module_no === parseInt(modNo));
    renderTeachingPlan(filtered);
  }
}

function searchPlan(query) {
  if (!teachingPlanData) return;
  const q = query.toLowerCase();
  const filtered = teachingPlanData.lectures.filter(l => 
    l.topic.toLowerCase().includes(q) || 
    l.learning_objective.toLowerCase().includes(q) ||
    l.board_work_or_numerical.toLowerCase().includes(q)
  );
  renderTeachingPlan(filtered);
}

function toggleLecStatus(lecNo, isDone) {
  const key = `pccst303_lec_${lecNo}`;
  if (isDone) localStorage.setItem(key, 'done');
  else localStorage.removeItem(key);
  updatePlanStats();
}

function updatePlanStats() {
  let completed = 0;
  for (let i = 1; i <= 46; i++) {
    if (localStorage.getItem(`pccst303_lec_${i}`)) completed++;
  }
  const counter = document.getElementById('plan-completed-count');
  if (counter) counter.innerText = `${completed} / 46 Hours`;
  const bar = document.getElementById('plan-progress-bar');
  if (bar) bar.style.width = `${(completed / 46) * 100}%`;
}

// Interactive Sorting Visualizer
let sortArray = [45, 12, 89, 34, 67, 23, 90, 11, 56, 78, 30, 49];
let sortRunning = false;

function setupSortingVisualizer() {
  renderBars(sortArray);
}

function renderBars(arr, activeIndices = []) {
  const container = document.getElementById('sorting-bars');
  if (!container) return;
  container.innerHTML = arr.map((val, idx) => {
    const isActive = activeIndices.includes(idx);
    const bg = isActive ? 'var(--accent-warning)' : 'var(--accent-primary)';
    return `<div style="height:${val * 3}px; width:22px; background:${bg}; border-radius:4px 4px 0 0; display:flex; align-items:flex-end; justify-content:center; color:#000; font-size:0.75rem; font-weight:700;">${val}</div>`;
  }).join('');
}

function resetSortArray() {
  sortArray = Array.from({length: 12}, () => Math.floor(Math.random() * 85) + 10);
  renderBars(sortArray);
  document.getElementById('sort-status').innerText = 'Ready. Click Run Sort.';
}

async function runSort() {
  if (sortRunning) return;
  sortRunning = true;
  const algo = document.getElementById('sort-algo-select').value;
  document.getElementById('sort-status').innerText = `Running ${algo.toUpperCase()}...`;
  
  if (algo === 'bubble') {
    for (let i = 0; i < sortArray.length; i++) {
      for (let j = 0; j < sortArray.length - i - 1; j++) {
        renderBars(sortArray, [j, j + 1]);
        await new Promise(r => setTimeout(r, 120));
        if (sortArray[j] > sortArray[j + 1]) {
          let temp = sortArray[j];
          sortArray[j] = sortArray[j + 1];
          sortArray[j + 1] = temp;
          renderBars(sortArray, [j, j + 1]);
          await new Promise(r => setTimeout(r, 120));
        }
      }
    }
  } else if (algo === 'selection') {
    for (let i = 0; i < sortArray.length - 1; i++) {
      let minIdx = i;
      for (let j = i + 1; j < sortArray.length; j++) {
        renderBars(sortArray, [i, j]);
        await new Promise(r => setTimeout(r, 100));
        if (sortArray[j] < sortArray[minIdx]) minIdx = j;
      }
      let temp = sortArray[i];
      sortArray[i] = sortArray[minIdx];
      sortArray[minIdx] = temp;
      renderBars(sortArray, [i, minIdx]);
    }
  } else if (algo === 'insertion') {
    for (let i = 1; i < sortArray.length; i++) {
      let key = sortArray[i];
      let j = i - 1;
      while (j >= 0 && sortArray[j] > key) {
        sortArray[j + 1] = sortArray[j];
        renderBars(sortArray, [j, j + 1]);
        await new Promise(r => setTimeout(r, 120));
        j--;
      }
      sortArray[j + 1] = key;
      renderBars(sortArray, [j + 1]);
    }
  }

  renderBars(sortArray);
  document.getElementById('sort-status').innerText = `Completed! Array is fully sorted.`;
  sortRunning = false;
}

// Stack & Infix to Postfix Visualizer
function setupStackVisualizer() {}

function convertInfix() {
  const input = document.getElementById('infix-input').value.trim();
  if (!input) return;
  
  let stack = [];
  let output = [];
  let trace = [];
  
  function prec(op) {
    if (op === '^') return 3;
    if (op === '*' || op === '/') return 2;
    if (op === '+' || op === '-') return 1;
    return 0;
  }
  
  for (let ch of input) {
    if (/[a-zA-Z0-9]/.test(ch)) {
      output.push(ch);
      trace.push(`Operand '${ch}' &rarr; Append to output: [${output.join(' ')}]`);
    } else if (ch === '(') {
      stack.push(ch);
      trace.push(`Open bracket '(' &rarr; Push to stack: [${stack.join(' ')}]`);
    } else if (ch === ')') {
      while (stack.length && stack[stack.length - 1] !== '(') {
        const top = stack.pop();
        output.push(top);
      }
      stack.pop(); // discard '('
      trace.push(`Close bracket ')' &rarr; Pop until '(': Output=[${output.join(' ')}], Stack=[${stack.join(' ')}]`);
    } else if ('+-*/^'.includes(ch)) {
      while (stack.length && prec(stack[stack.length - 1]) >= prec(ch)) {
        output.push(stack.pop());
      }
      stack.push(ch);
      trace.push(`Operator '${ch}' &rarr; Stack=[${stack.join(' ')}], Output=[${output.join(' ')}]`);
    }
  }
  
  while (stack.length) {
    output.push(stack.pop());
  }
  trace.push(`End of expression &rarr; Final Postfix Output: <strong>${output.join(' ')}</strong>`);

  document.getElementById('postfix-result').innerText = output.join(' ');
  document.getElementById('postfix-trace').innerHTML = trace.map(t => `<div style="padding:4px 0; border-bottom:1px solid rgba(255,255,255,0.05); font-family:var(--font-mono); font-size:0.85rem;">${t}</div>`).join('');
}

// Binary Search Tree Visualizer
let bstRoot = null;

class BSTNode {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
    this.x = 0;
    this.y = 0;
  }
}

function insertBST(root, val) {
  if (!root) return new BSTNode(val);
  if (val < root.val) root.left = insertBST(root.left, val);
  else if (val > root.val) root.right = insertBST(root.right, val);
  return root;
}

function setupTreeVisualizer() {
  [50, 30, 70, 20, 40, 60, 80].forEach(v => {
    bstRoot = insertBST(bstRoot, v);
  });
  drawTree();
}

function addNodeToBST() {
  const val = parseInt(document.getElementById('bst-node-val').value);
  if (isNaN(val)) return;
  bstRoot = insertBST(bstRoot, val);
  drawTree();
}

function drawTree() {
  const canvas = document.getElementById('tree-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  
  function assignCoords(node, depth, left, right) {
    if (!node) return;
    node.x = (left + right) / 2;
    node.y = 50 + depth * 70;
    assignCoords(node.left, depth + 1, left, node.x);
    assignCoords(node.right, depth + 1, node.x, right);
  }
  
  function drawLinks(node) {
    if (!node) return;
    if (node.left) {
      ctx.beginPath();
      ctx.moveTo(node.x, node.y);
      ctx.lineTo(node.left.x, node.left.y);
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2;
      ctx.stroke();
      drawLinks(node.left);
    }
    if (node.right) {
      ctx.beginPath();
      ctx.moveTo(node.x, node.y);
      ctx.lineTo(node.right.x, node.right.y);
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2;
      ctx.stroke();
      drawLinks(node.right);
    }
  }
  
  function drawNodes(node) {
    if (!node) return;
    ctx.beginPath();
    ctx.arc(node.x, node.y, 18, 0, Math.PI * 2);
    ctx.fillStyle = '#0f172a';
    ctx.fill();
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2;
    ctx.stroke();
    
    ctx.fillStyle = '#f8fafc';
    ctx.font = 'bold 12px sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(node.val, node.x, node.y);
    
    drawNodes(node.left);
    drawNodes(node.right);
  }

  assignCoords(bstRoot, 0, 0, canvas.width);
  drawLinks(bstRoot);
  drawNodes(bstRoot);
}

// Interactive Quiz Engine
const quizQuestions = [
  {
    q: "1. What is the time complexity of the Fast Transpose algorithm for a sparse matrix with n non-zero elements and c columns?",
    options: ["O(c * n)", "O(c + n)", "O(n^2)", "O(c^2)"],
    correct: 1,
    exp: "Fast Transpose utilizes frequency count array (row_terms) and prefix sum array (starting_pos) to place elements directly into the transposed triplet array in O(columns + non_zero) time."
  },
  {
    q: "2. In a circular queue of size N using array indices 0 to N-1, what is the condition for full queue?",
    options: ["front == rear", "rear == N - 1", "(rear + 1) % N == front", "rear + 1 == front"],
    correct: 2,
    exp: "The circular queue reserves one empty slot to disambiguate the full state from the empty state. Full condition is (rear + 1) % N == front."
  },
  {
    q: "3. For any non-empty binary tree with n0 leaf nodes and n2 nodes of degree 2, which equation strictly holds?",
    options: ["n0 = n2 - 1", "n0 = n2 + 1", "n0 = 2 * n2", "n2 = n0 + 1"],
    correct: 1,
    exp: "Theorem: In any binary tree where every node has degree 0, 1, or 2, total edges e = n - 1 and e = n1 + 2*n2. Equating both yields n0 = n2 + 1."
  },
  {
    q: "4. Which sorting algorithm achieves guaranteed O(n log n) worst-case time with in-place O(1) auxiliary memory?",
    options: ["Quick Sort", "Merge Sort", "Heap Sort", "Insertion Sort"],
    correct: 2,
    exp: "Heap Sort operates directly on the array representation of complete binary trees with O(1) auxiliary space and O(n log n) worst-case bound."
  },
  {
    q: "5. What phenomenon occurs in open addressing with Linear Probing where long sequences of occupied slots build up?",
    options: ["Secondary Clustering", "Primary Clustering", "Hash Overlap", "Linear Thrashing"],
    correct: 1,
    exp: "Linear probing searches adjacent cells, causing adjacent occupied clusters to merge together into increasingly larger clusters, known as Primary Clustering."
  }
];

let quizScore = 0;
let userAnswers = {};

function setupQuizEngine() {
  const container = document.getElementById('quiz-container');
  if (!container) return;
  container.innerHTML = quizQuestions.map((q, qIdx) => `
    <div class="quiz-card" id="qcard-${qIdx}">
      <h3 style="margin-top:0; font-family:var(--font-heading); font-size:1.1rem;">${q.q}</h3>
      <div class="quiz-options">
        ${q.options.map((opt, optIdx) => `
          <div class="quiz-option" onclick="selectQuizAnswer(${qIdx}, ${optIdx}, this)">
            ${String.fromCharCode(65 + optIdx)}) ${opt}
          </div>
        `).join('')}
      </div>
      <div id="qexp-${qIdx}" style="display:none; margin-top:10px; padding:10px; background:rgba(56,189,248,0.1); border-left:3px solid var(--accent-primary); font-size:0.88rem; color:var(--text-secondary);">
        <strong>Explanation:</strong> ${q.exp}
      </div>
    </div>
  `).join('');
}

function selectQuizAnswer(qIdx, optIdx, el) {
  if (userAnswers[qIdx] !== undefined) return;
  userAnswers[qIdx] = optIdx;
  const q = quizQuestions[qIdx];
  const card = document.getElementById(`qcard-${qIdx}`);
  const options = card.querySelectorAll('.quiz-option');
  
  if (optIdx === q.correct) {
    el.classList.add('correct');
    quizScore++;
  } else {
    el.classList.add('incorrect');
    options[q.correct].classList.add('correct');
  }
  
  document.getElementById(`qexp-${qIdx}`).style.display = 'block';
  document.getElementById('quiz-score-badge').innerText = `Score: ${quizScore} / ${quizQuestions.length}`;
}

// Knowledge Graph
function setupKnowledgeGraph() {
  const svg = document.getElementById('kg-svg');
  if (!svg) return;
  
  const nodes = [
    { id: "PCCST303", label: "PCCST303: DSA", x: 450, y: 50, color: "#38bdf8", r: 35 },
    { id: "M1", label: "Module 1: Linear", x: 180, y: 160, color: "#818cf8", r: 25 },
    { id: "M2", label: "Module 2: Linked", x: 360, y: 160, color: "#818cf8", r: 25 },
    { id: "M3", label: "Module 3: Non-Linear", x: 540, y: 160, color: "#818cf8", r: 25 },
    { id: "M4", label: "Module 4: Sort/Search", x: 720, y: 160, color: "#818cf8", r: 25 },
    { id: "T1", label: "Stacks & Queues", x: 100, y: 280, color: "#34d399", r: 20 },
    { id: "T2", label: "Sparse Matrix", x: 220, y: 280, color: "#34d399", r: 20 },
    { id: "T3", label: "Memory GC", x: 360, y: 280, color: "#34d399", r: 20 },
    { id: "T4", label: "BST & Heaps", x: 500, y: 280, color: "#34d399", r: 20 },
    { id: "T5", label: "BFS & DFS", x: 600, y: 280, color: "#34d399", r: 20 },
    { id: "T6", label: "Quick / Merge", x: 700, y: 280, color: "#34d399", r: 20 },
    { id: "T7", label: "Hash Collision", x: 800, y: 280, color: "#34d399", r: 20 }
  ];

  const links = [
    ["PCCST303", "M1"], ["PCCST303", "M2"], ["PCCST303", "M3"], ["PCCST303", "M4"],
    ["M1", "T1"], ["M1", "T2"],
    ["M2", "T3"],
    ["M3", "T4"], ["M3", "T5"],
    ["M4", "T6"], ["M4", "T7"]
  ];

  let svgContent = '';
  links.forEach(([srcId, tgtId]) => {
    const s = nodes.find(n => n.id === srcId);
    const t = nodes.find(n => n.id === tgtId);
    svgContent += `<line x1="${s.x}" y1="${s.y}" x2="${t.x}" y2="${t.y}" stroke="rgba(255,255,255,0.2)" stroke-width="2" />`;
  });

  nodes.forEach(n => {
    svgContent += `
      <g style="cursor:pointer;" onclick="kgNodeClick('${n.id}')">
        <circle cx="${n.x}" cy="${n.y}" r="${n.r}" fill="${n.color}" opacity="0.9" stroke="#fff" stroke-width="1.5" />
        <text x="${n.x}" y="${n.y + 4}" text-anchor="middle" fill="#000" font-size="10px" font-weight="700" font-family="sans-serif">${n.label}</text>
      </g>
    `;
  });

  svg.innerHTML = svgContent;
}

function kgNodeClick(nodeId) {
  alert(`Knowledge Graph Concept: ${nodeId}\nExploration details linked to KTU 2024 Course Outcomes.`);
}

// Voice Narration Engine
function setupVoiceNarration() {}

function toggleNarration() {
  if (!speechSynth) {
    alert("Speech Synthesis API not supported in your browser.");
    return;
  }
  
  if (isSpeaking) {
    speechSynth.cancel();
    isSpeaking = false;
    document.getElementById('voice-play-btn').innerText = '▶ Speak Notes';
    document.getElementById('voice-caption-box').style.display = 'none';
    return;
  }
  
  const textToRead = "Welcome to course P C C S T 303: Data Structures and Algorithms. Taught by Jane Rose, Assistant Professor, Computer Science and Engineering. This KTU 2024 curriculum course covers 4 modules: Linear data structures, dynamic linked lists and memory management, trees and graphs, and sorting, searching, and hashing techniques. Explore the 46-hour teaching plan and algorithm visualizers below.";
  
  currentUtterance = new SpeechSynthesisUtterance(textToRead);
  const speed = parseFloat(document.getElementById('voice-speed-select').value) || 1.0;
  currentUtterance.rate = speed;
  
  currentUtterance.onstart = () => {
    isSpeaking = true;
    document.getElementById('voice-play-btn').innerText = '⏸ Pause';
    document.getElementById('voice-caption-box').style.display = 'block';
    document.getElementById('voice-caption-text').innerText = textToRead;
  };
  
  currentUtterance.onend = () => {
    isSpeaking = false;
    document.getElementById('voice-play-btn').innerText = '▶ Speak Notes';
    document.getElementById('voice-caption-box').style.display = 'none';
  };
  
  speechSynth.speak(currentUtterance);
}
