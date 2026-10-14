import os
import unittest
import re

class TestThemeEngine(unittest.TestCase):
    def setUp(self):
        self.base_dir = r"c:\Users\Asus\Downloads\SYLLABUS"
        self.css_path = os.path.join(self.base_dir, "shared-components", "themes", "liquid-glass.css")
        self.js_path = os.path.join(self.base_dir, "shared-components", "themes", "theme-switcher.js")

    def test_css_file_exists(self):
        self.assertTrue(os.path.exists(self.css_path), "liquid-glass.css must exist")

    def test_js_file_exists(self):
        self.assertTrue(os.path.exists(self.js_path), "theme-switcher.js must exist")

    def test_all_10_glass_themes_defined(self):
        with open(self.css_path, "r", encoding="utf-8") as f:
            css = f.read()
        
        required_themes = [
            "theme-frosted",
            "theme-liquid",
            "theme-aurora",
            "theme-crystal",
            "theme-holographic",
            "theme-translucent",
            "theme-neumorphic",
            "theme-scifi",
            "theme-academic",
            "theme-highcontrast"
        ]
        
        for theme in required_themes:
            self.assertIn(f".{theme}", css, f"CSS must contain class definition for .{theme}")

    def test_core_css_tokens(self):
        with open(self.css_path, "r", encoding="utf-8") as f:
            css = f.read()
            
        required_vars = [
            "--glass-bg",
            "--glass-border",
            "--glass-blur",
            "--accent-primary",
            "--text-primary"
        ]
        for var in required_vars:
            self.assertIn(var, css, f"CSS must define variable {var}")

    def test_js_switcher_logic(self):
        with open(self.js_path, "r", encoding="utf-8") as f:
            js = f.read()
            
        self.assertIn("setGlassTheme", js)
        self.assertIn("toggleDarkMode", js)
        self.assertIn("localStorage", js)
        self.assertIn("theme-frosted", js)

if __name__ == "__main__":
    unittest.main()
