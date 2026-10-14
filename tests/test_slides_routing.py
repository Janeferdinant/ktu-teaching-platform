import unittest
import urllib.request
import json
import re

class TestSlidesRoutingAndInteractiveDeck(unittest.TestCase):
    def setUp(self):
        self.sample_codes = ["PCCST303", "PCCST302", "GAEST305", "GAMAT301", "PBCST304"]

    def test_shared_components(self):
        """Verify core design and course client scripts load properly"""
        urls = [
            "http://localhost:5173/shared-components/themes/liquid-glass.css",
            "http://localhost:5173/shared-components/themes/theme-switcher.js",
            "http://localhost:5173/shared-components/course/course.css",
            "http://localhost:5173/shared-components/course/course.js"
        ]
        for u in urls:
            res = urllib.request.urlopen(u)
            self.assertEqual(res.status, 200, f"{u} must return 200")
            body = res.read().decode('utf-8')
            self.assertGreater(len(body), 50)

    def test_course_website_slides_tab(self):
        """Verify each course website contains the embedded slides player and dual-mode link"""
        for code in self.sample_codes:
            url = f"http://localhost:5173/courses/{code}/"
            res = urllib.request.urlopen(url)
            self.assertEqual(res.status, 200, f"Course home {url} must return 200")
            html = res.read().decode('utf-8')

            # Must contain the slides tab and section
            self.assertIn('data-tab="slides"', html, f"{code} must have slides tab button")
            self.assertIn('id="sec-slides"', html, f"{code} must have sec-slides section")
            self.assertIn('id="embedded-slide-content"', html, f"{code} must have embedded-slide-content container")

            # Must have dual-mode link pointing to /courses/{code}/slides/
            expected_href = f'/courses/{code}/slides/'
            self.assertIn(expected_href, html, f"{code} must link to {expected_href}")

            # Must define COURSE_SLIDES in window
            self.assertIn('window.COURSE_SLIDES', html, f"{code} must provide window.COURSE_SLIDES data")

            # Branding verification
            self.assertIn('Jane Rose | Asst. Professor | CSE', html)

    def test_fullscreen_presentation_deck(self):
        """Verify fullscreen lecture slides deck loads interactively with navigation controls"""
        for code in self.sample_codes:
            for endpoint in [f"/courses/{code}/slides/", f"/courses/{code}/slides/lecture_slides.html"]:
                url = f"http://localhost:5173{endpoint}"
                res = urllib.request.urlopen(url)
                self.assertEqual(res.status, 200, f"{url} must return 200")
                html = res.read().decode('utf-8')

                self.assertIn("Presentation", html, f"{url} must contain Presentation")
                self.assertIn("Deck", html, f"{url} must contain Deck")
                self.assertIn("slide-controls", html, f"{url} must have slide-controls")
                self.assertIn("nextSlide()", html, f"{url} must define nextSlide function")
                self.assertIn("prevSlide()", html, f"{url} must define prevSlide function")
                self.assertIn("Back to Course", html, f"{url} must have Back to Course link")

                # Branding verification
                self.assertIn('Jane Rose | Asst. Professor | CSE', html)

    def test_trailing_slash_normalization(self):
        """Verify non-slash routes redirect or serve properly without 404"""
        for code in ["PCCST303", "PCCST302"]:
            # Route /courses/:code
            url1 = f"http://localhost:5173/courses/{code}"
            res1 = urllib.request.urlopen(url1)
            self.assertEqual(res1.status, 200)

            # Route /courses/:code/slides
            url2 = f"http://localhost:5173/courses/{code}/slides"
            res2 = urllib.request.urlopen(url2)
            self.assertEqual(res2.status, 200)

    def test_relative_referer_slides_fallback(self):
        """Verify fallback when relative link ../slides/lecture_slides.html is requested with referer"""
        for code in ["PCCST303", "PCCST302", "GAEST305"]:
            req = urllib.request.Request(
                "http://localhost:5173/courses/slides/lecture_slides.html",
                headers={"Referer": f"http://localhost:5173/courses/{code}/"}
            )
            res = urllib.request.urlopen(req)
            self.assertEqual(res.status, 200)
            html = res.read().decode('utf-8')
            self.assertIn(code, html, f"Fallback must correctly serve deck for {code}")

if __name__ == "__main__":
    unittest.main()
