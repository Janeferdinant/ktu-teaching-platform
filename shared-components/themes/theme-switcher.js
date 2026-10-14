/**
 * Liquid Glass Theme Switcher Engine
 * Jane Rose | Asst. Professor | CSE
 */

const THEMES = [
  { id: 'theme-liquid', name: 'Liquid Glass (Default)', desc: 'Glossy specular fluid reflections' },
  { id: 'theme-frosted', name: 'Frosted Glass', desc: 'Soft diffused matte texture' },
  { id: 'theme-aurora', name: 'Aurora Glass', desc: 'Polar teal & violet glow' },
  { id: 'theme-crystal', name: 'Crystal Glass', desc: 'Prism edges & clear refraction' },
  { id: 'theme-holographic', name: 'Holographic Glass', desc: 'Prismatic chromatic dispersion' },
  { id: 'theme-translucent', name: 'Layered Translucent', desc: 'Multi-depth cascading glass panes' },
  { id: 'theme-neumorphic', name: 'Neumorphic Hybrid', desc: 'Soft extruded tactile bevels' },
  { id: 'theme-scifi', name: 'Sci-Fi Laboratory', desc: 'Cybernetic terminal with deep glow' },
  { id: 'theme-academic', name: 'Light Academic', desc: 'Crisp ivory & university blue' },
  { id: 'theme-highcontrast', name: 'High-Contrast Mode', desc: 'WCAG AAA black & yellow contrast' }
];

function initThemeEngine() {
  const savedTheme = localStorage.getItem('agy_glass_theme') || 'theme-liquid';
  const savedMode = localStorage.getItem('agy_color_mode') || 'dark';
  setGlassTheme(savedTheme);
  setColorMode(savedMode);
}

function setGlassTheme(themeId) {
  const body = document.body;
  THEMES.forEach(t => body.classList.remove(t.id));
  if (THEMES.some(t => t.id === themeId)) {
    body.classList.add(themeId);
    localStorage.setItem('agy_glass_theme', themeId);
  } else {
    body.classList.add('theme-liquid');
    localStorage.setItem('agy_glass_theme', 'theme-liquid');
  }

  // Update select input if present
  const select = document.getElementById('glass-theme-select');
  if (select && select.value !== themeId) {
    select.value = themeId;
  }
}

function toggleDarkMode() {
  const currentMode = document.documentElement.getAttribute('data-mode') || 'dark';
  const newMode = currentMode === 'dark' ? 'light' : 'dark';
  setColorMode(newMode);
}

function setColorMode(mode) {
  document.documentElement.setAttribute('data-mode', mode);
  localStorage.setItem('agy_color_mode', mode);
  const btn = document.getElementById('dark-mode-toggle-btn');
  if (btn) {
    btn.innerHTML = mode === 'dark' ? '☀️ Light' : '🌙 Dark';
  }
}

// Auto initialize on DOM ready
if (typeof document !== 'undefined') {
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initThemeEngine);
  } else {
    initThemeEngine();
  }
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { THEMES, setGlassTheme, toggleDarkMode, setColorMode, initThemeEngine };
}
