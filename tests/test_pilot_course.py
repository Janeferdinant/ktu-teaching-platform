import os
import unittest
import json

class TestPilotCourse(unittest.TestCase):
    def setUp(self):
        self.base = r"c:\Users\Asus\Downloads\SYLLABUS\courses\PCCST303"
        self.website_html = os.path.join(self.base, "website", "index.html")
        self.plan_json = os.path.join(self.base, "teaching-plan", "teaching_plan_46h.json")
        self.notes_json = os.path.join(self.base, "notes", "module_notes.json")
        self.slides_html = os.path.join(self.base, "slides", "lecture_slides.html")

    def test_course_files_exist(self):
        self.assertTrue(os.path.exists(self.website_html), "Course index.html must exist")
        self.assertTrue(os.path.exists(self.plan_json), "teaching_plan_46h.json must exist")
        self.assertTrue(os.path.exists(self.notes_json), "module_notes.json must exist")
        self.assertTrue(os.path.exists(self.slides_html), "lecture_slides.html must exist")

    def test_teaching_plan_46_hours(self):
        with open(self.plan_json, "r", encoding="utf-8") as f:
            plan = json.load(f)
        self.assertEqual(len(plan["lectures"]), 46, "Teaching plan must have exactly 46 scheduled lecture hours")
        self.assertEqual(plan["course_code"], "PCCST303")
        self.assertTrue(plan["hours_discrepancy_reconciled"], "Discrepancy badge must be present and explained")

    def test_module_notes_all_modules(self):
        with open(self.notes_json, "r", encoding="utf-8") as f:
            notes = json.load(f)
        self.assertEqual(len(notes["modules"]), 4, "Must cover all 4 official modules")
        for m in notes["modules"]:
            self.assertTrue(len(m["sections"]) >= 3, f"Module {m['module_no']} must have comprehensive sections")
            self.assertIn("exam_tips", m)
            self.assertIn("summary", m)

    def test_branding_footer(self):
        with open(self.website_html, "r", encoding="utf-8") as f:
            html = f.read()
        self.assertIn("Jane Rose | Asst. Professor | CSE", html, "Mandatory branding footer missing")

if __name__ == "__main__":
    unittest.main()
