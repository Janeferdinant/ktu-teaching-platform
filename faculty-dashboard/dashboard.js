/**
 * Centralized Faculty Dashboard Script
 * Jane Rose | Asst. Professor | CSE
 */

let allCourses = [];
let filteredCourses = [];

document.addEventListener('DOMContentLoaded', async () => {
  await loadCourseRegistry();
  setupFilters();
});

async function loadCourseRegistry() {
  try {
    const res = await fetch('../registry/course_registry.json');
    const data = await res.json();
    allCourses = Object.values(data);
    filteredCourses = [...allCourses];
    renderCoursesTable(filteredCourses);
  } catch (e) {
    console.error('Failed to load course registry:', e);
  }
}

function renderCoursesTable(courses) {
  const tbody = document.getElementById('courses-tbody');
  if (!tbody) return;
  
  document.getElementById('table-course-count').innerText = `${courses.length} Courses`;

  tbody.innerHTML = courses.map(c => {
    const isPilot = c.code === 'PCCST303';
    const siteUrl = `/courses/${c.code}/`;
    const slidesUrl = `/courses/${c.code}/slides/`;
    const statusBadge = isPilot ? 
      `<span class="glass-badge" style="background:rgba(52,211,153,0.2); color:#34d399; border-color:#34d399;">Active Pilot</span>` :
      `<span class="glass-badge" style="background:rgba(56,189,248,0.15); color:#38bdf8; border-color:#38bdf8;">Deployed</span>`;

    return `
      <tr>
        <td style="font-weight:700; color:var(--accent-primary);">${c.code}</td>
        <td style="font-weight:600; color:var(--text-primary);">${c.title}</td>
        <td><span class="glass-badge" style="font-size:0.72rem;">${c.semester}</span></td>
        <td>${c.credits} Cr</td>
        <td><span style="font-family:var(--font-mono); font-size:0.82rem;">${c.ltpr}</span></td>
        <td>${statusBadge}</td>
        <td>
          <div style="display:flex; gap:6px;">
            <a href="${siteUrl}" class="glass-btn" style="padding:4px 10px; font-size:0.8rem;">
              🚀 Course Site
            </a>
            <a href="${slidesUrl}" target="_blank" class="glass-btn" style="padding:4px 8px; font-size:0.8rem;" title="Lecture Slides">
              📊 Slides
            </a>
          </div>
        </td>
      </tr>
    `;
  }).join('');
}

function setupFilters() {
  const searchInput = document.getElementById('course-search-input');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      const q = e.target.value.toLowerCase();
      filteredCourses = allCourses.filter(c => 
        c.code.toLowerCase().includes(q) || 
        c.title.toLowerCase().includes(q)
      );
      renderCoursesTable(filteredCourses);
    });
  }
}

function filterSemester(sem) {
  if (sem === 'all') {
    filteredCourses = [...allCourses];
  } else {
    filteredCourses = allCourses.filter(c => c.semester === sem || c.semester.startsWith(sem));
  }
  renderCoursesTable(filteredCourses);
}

function triggerBatchGeneration() {
  alert("All 158 course websites and teaching plans are currently generated and live.\nClick any course's 'Course Site' or 'Slides' button to view its dedicated teaching materials.");
}
