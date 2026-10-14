import os
import unittest

class TestFacultyDashboard(unittest.TestCase):
    def setUp(self):
        self.base = r"c:\Users\Asus\Downloads\SYLLABUS\faculty-dashboard"
        self.html_path = os.path.join(self.base, "index.html")
        self.css_path = os.path.join(self.base, "dashboard.css")
        self.js_path = os.path.join(self.base, "dashboard.js")

    def test_dashboard_files_exist(self):
        self.assertTrue(os.path.exists(self.html_path), "faculty-dashboard index.html must exist")
        self.assertTrue(os.path.exists(self.css_path), "dashboard.css must exist")
        self.assertTrue(os.path.exists(self.js_path), "dashboard.js must exist")

    def test_dashboard_kpis_and_branding(self):
        with open(self.html_path, "r", encoding="utf-8") as f:
            html = f.read()
        self.assertIn("Jane Rose | Asst. Professor | CSE", html)
        self.assertIn("PCCST303", html)
        self.assertIn("158", html) # Total courses KPI
        self.assertIn("1,206", html) # Total pages scanned KPI

    def test_dashboard_theme_controls(self):
        with open(self.html_path, "r", encoding="utf-8") as f:
            html = f.read()
        self.assertIn("glass-theme-select", html)
        self.assertIn("dark-mode-toggle-btn", html)

if __name__ == "__main__":
    unittest.main()
