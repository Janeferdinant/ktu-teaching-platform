/**
 * Academic Teaching Platform - Interactive Course Client Script
 * Jane Rose | Asst. Professor | CSE
 */

let currentTab = 'overview';
let teachingPlanData = null;
let currentSlideIdx = 0;
let courseSlidesData = [];

document.addEventListener('DOMContentLoaded', async () => {
  setupTabs();
  initEmbeddedSlides();
  await loadTeachingPlan();
  setupSortingVisualizer();
  setupQuizEngine();
  setupKnowledgeGraph();
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
}

// Embedded Slide Deck Viewer
function initEmbeddedSlides() {
  const container = document.getElementById('embedded-slide-content');
  if (!container) return;

  // Read slides from global variable or default from page data
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
  if (currentSlideIdx > 0) {
    renderEmbeddedSlide(currentSlideIdx - 1);
  }
}

function nextEmbeddedSlide() {
  if (currentSlideIdx < courseSlidesData.length - 1) {
    renderEmbeddedSlide(currentSlideIdx + 1);
  }
}

// 46-Hour Teaching Plan Loader
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
    console.warn('Direct teaching plan fetch fallback:', e);
    // Try relative fallback
    try {
      const res2 = await fetch('../teaching-plan/teaching_plan_46h.json');
      if (res2.ok) {
        teachingPlanData = await res2.json();
        renderTeachingPlan(teachingPlanData.lectures || []);
      }
    } catch (e2) {
      console.error('All plan fetch attempts failed:', e2);
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

// Sorting Visualizer Demo
let sortArray = [45, 12, 89, 34, 67, 23, 90, 11, 56, 78, 30, 49];
let isSorting = false;

function setupSortingVisualizer() {
  const container = document.getElementById('sorting-bars');
  if (!container) return;
  renderSortBars(sortArray);
}

function renderSortBars(arr, activeIdx = -1) {
  const container = document.getElementById('sorting-bars');
  if (!container) return;
  container.innerHTML = arr.map((val, idx) => {
    const bg = idx === activeIdx ? 'var(--accent-warning)' : 'var(--accent-primary)';
    return `<div style="height:${val * 2.5}px; width:22px; background:${bg}; border-radius:4px 4px 0 0; display:flex; align-items:flex-end; justify-content:center; color:#000; font-size:0.72rem; font-weight:700;">${val}</div>`;
  }).join('');
}

async function runSort() {
  if (isSorting) return;
  isSorting = true;
  const status = document.getElementById('sort-status');
  if (status) status.innerText = 'Sorting in progress (Bubble Sort)...';

  for (let i = 0; i < sortArray.length; i++) {
    for (let j = 0; j < sortArray.length - i - 1; j++) {
      renderSortBars(sortArray, j);
      await new Promise(r => setTimeout(r, 60));
      if (sortArray[j] > sortArray[j + 1]) {
        let temp = sortArray[j];
        sortArray[j] = sortArray[j + 1];
        sortArray[j + 1] = temp;
      }
    }
  }
  renderSortBars(sortArray);
  if (status) status.innerText = 'Sorting complete! Array ordered in O(n²) time.';
  isSorting = false;
}

function resetSortArray() {
  if (isSorting) return;
  sortArray = Array.from({length: 12}, () => Math.floor(Math.random() * 80) + 15);
  renderSortBars(sortArray);
  const status = document.getElementById('sort-status');
  if (status) status.innerText = 'Ready. Click Run Simulation.';
}

// Quiz Engine
function setupQuizEngine() {
  const container = document.getElementById('quiz-container');
  if (!container) return;

  const defaultQuizzes = [
    {
      q: "Which asymptotic notation represents the formal worst-case upper bound of an algorithm?",
      options: ["Big-Theta (Θ)", "Big-O (O)", "Big-Omega (Ω)", "Little-o (o)"],
      answer: 1,
      expl: "Big-O notation specifies an asymptotic upper bound: f(n) <= c * g(n) for all n >= n0."
    },
    {
      q: "What is the primary motivation for using a circular queue over a linear array queue?",
      options: ["Reduces memory to half", "Avoids false overflow due to vacant front positions", "Supports priority sorting", "Eliminates pointer usage"],
      answer: 1,
      expl: "In a circular queue, rear wraps around to 0 when reaching capacity, reclaiming space left by de-queued elements."
    }
  ];

  container.innerHTML = defaultQuizzes.map((quiz, qIdx) => `
    <div class="quiz-card">
      <div style="font-weight: 700; color: var(--text-primary); margin-bottom: 0.8rem;">
        Question ${qIdx + 1}: ${quiz.q}
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

// Knowledge Graph (SVG Tree)
function setupKnowledgeGraph() {
  const svg = document.getElementById('kg-svg');
  if (!svg) return;

  svg.innerHTML = `
    <defs>
      <linearGradient id="kg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#38bdf8" />
        <stop offset="100%" stop-color="#818cf8" />
      </linearGradient>
    </defs>
    <!-- Central Course Root -->
    <circle cx="475" cy="190" r="42" fill="url(#kg-grad)" />
    <text x="475" y="195" text-anchor="middle" fill="#000" font-weight="bold" font-size="12">COURSE CORE</text>

    <!-- Branch Module 1 -->
    <line x1="475" y1="190" x2="180" y2="80" stroke="rgba(255,255,255,0.2)" stroke-width="2" />
    <circle cx="180" cy="80" r="32" fill="rgba(56,189,248,0.2)" stroke="#38bdf8" stroke-width="2" />
    <text x="180" y="85" text-anchor="middle" fill="#fff" font-size="11">Module 1</text>

    <!-- Branch Module 2 -->
    <line x1="475" y1="190" x2="770" y2="80" stroke="rgba(255,255,255,0.2)" stroke-width="2" />
    <circle cx="770" cy="80" r="32" fill="rgba(129,140,248,0.2)" stroke="#818cf8" stroke-width="2" />
    <text x="770" y="85" text-anchor="middle" fill="#fff" font-size="11">Module 2</text>

    <!-- Branch Module 3 -->
    <line x1="475" y1="190" x2="180" y2="300" stroke="rgba(255,255,255,0.2)" stroke-width="2" />
    <circle cx="180" cy="300" r="32" fill="rgba(52,211,153,0.2)" stroke="#34d399" stroke-width="2" />
    <text x="180" y="305" text-anchor="middle" fill="#fff" font-size="11">Module 3</text>

    <!-- Branch Module 4 -->
    <line x1="475" y1="190" x2="770" y2="300" stroke="rgba(255,255,255,0.2)" stroke-width="2" />
    <circle cx="770" cy="300" r="32" fill="rgba(251,191,36,0.2)" stroke="#fbbf24" stroke-width="2" />
    <text x="770" y="305" text-anchor="middle" fill="#fff" font-size="11">Module 4</text>
  `;
}
