import unittest
import sys

from test_registry import TestCourseRegistry
from test_theme_engine import TestThemeEngine
from test_pilot_course import TestPilotCourse
from test_dashboard import TestFacultyDashboard
from test_pdf_links import TestPDFLinks

def suite():
    s = unittest.TestSuite()
    loader = unittest.TestLoader()
    s.addTests(loader.loadTestsFromTestCase(TestCourseRegistry))
    s.addTests(loader.loadTestsFromTestCase(TestThemeEngine))
    s.addTests(loader.loadTestsFromTestCase(TestPilotCourse))
    s.addTests(loader.loadTestsFromTestCase(TestFacultyDashboard))
    s.addTests(loader.loadTestsFromTestCase(TestPDFLinks))
    return s

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite())
    sys.exit(0 if result.wasSuccessful() else 1)
