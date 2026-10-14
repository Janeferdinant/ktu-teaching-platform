import os
import json
import csv
import unittest

class TestCourseRegistry(unittest.TestCase):
    def setUp(self):
        self.base_dir = r"c:\Users\Asus\Downloads\SYLLABUS"
        self.json_path = os.path.join(self.base_dir, "registry", "course_registry.json")
        self.csv_path = os.path.join(self.base_dir, "registry", "course_registry.csv")
        self.manifest_path = os.path.join(self.base_dir, "registry", "deployment_manifest.json")

    def test_registry_files_exist(self):
        self.assertTrue(os.path.exists(self.json_path), "course_registry.json must exist")
        self.assertTrue(os.path.exists(self.csv_path), "course_registry.csv must exist")
        self.assertTrue(os.path.exists(self.manifest_path), "deployment_manifest.json must exist")

    def test_course_count_and_uniqueness(self):
        with open(self.json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertGreaterEqual(len(data), 150, f"Expected at least 150 unique courses, got {len(data)}")
        
        # Verify CSV row count
        with open(self.csv_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = list(reader)
        # Header + 158 rows
        self.assertEqual(len(rows) - 1, len(data), "CSV row count must match JSON count")

    def test_pilot_course_pccst303(self):
        with open(self.json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertIn("PCCST303", data, "PCCST303 must be registered")
        pilot = data["PCCST303"]
        self.assertEqual(pilot["code"], "PCCST303")
        self.assertIn("DATA STRUCTURES", pilot["title"].upper())
        self.assertEqual(pilot["semester"], "S3")
        self.assertEqual(str(pilot["credits"]), "4")
        self.assertEqual(pilot["website_url"], "/courses/PCCST303/")
        self.assertEqual(pilot["source_pdf"], "Computer Science and Engineering.pdf")

    def test_deployment_manifest(self):
        with open(self.manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)
        self.assertEqual(manifest["pilot_course"], "PCCST303")
        self.assertIn("PCCST303", manifest["courses"])
        self.assertEqual(manifest["courses"]["PCCST303"]["website_path"], "/courses/PCCST303/")

if __name__ == "__main__":
    unittest.main()
