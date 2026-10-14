import os
import unittest
import pymupdf

class TestPDFLinks(unittest.TestCase):
    def setUp(self):
        self.base = r"c:\Users\Asus\Downloads\SYLLABUS"
        self.processed_dir = os.path.join(self.base, "syllabus", "processed-pdfs")
        self.linked_pdf = os.path.join(self.processed_dir, "Computer Science and Engineering_with_course_links.pdf")
        self.original_pdf = os.path.join(self.base, "Computer Science and Engineering.pdf")

    def test_original_pdf_preserved(self):
        self.assertTrue(os.path.exists(self.original_pdf), "Original PDF must be preserved unchanged")

    def test_linked_pdf_exists(self):
        self.assertTrue(os.path.exists(self.linked_pdf), "Companion linked PDF must exist")

    def test_clickable_link_in_pccst303_page(self):
        doc = pymupdf.open(self.linked_pdf)
        # PCCST303 is on page 11 (0-indexed 10)
        page = doc[10]
        links = page.get_links()
        self.assertTrue(len(links) > 0, "Page 11 must contain clickable link annotations")
        found_url = False
        for l in links:
            if l.get("uri") and "courses/PCCST303" in l.get("uri"):
                found_url = True
                break
        self.assertTrue(found_url, "Must have clickable link to /courses/PCCST303/")

if __name__ == "__main__":
    unittest.main()
