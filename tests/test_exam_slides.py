import os
import json
import re

base_dir = r"c:\Users\Asus\Downloads\SYLLABUS"
json_path = os.path.join(base_dir, "courses", "PCCST303", "slides", "exam_slides_320.json")
js_path = os.path.join(base_dir, "courses", "PCCST303", "slides", "exam_slides_data.js")
html_path = os.path.join(base_dir, "courses", "PCCST303", "slides", "lecture_slides.html")
website_path = os.path.join(base_dir, "courses", "PCCST303", "website", "index.html")

def test_exam_slides():
    print("Testing 320 Exam Slides Integrity...")
    
    # 1. Check JSON file exists
    assert os.path.exists(json_path), f"JSON file missing: {json_path}"
    with open(json_path, "r", encoding="utf-8") as f:
        slides = json.load(f)
        
    print(f"Total slides loaded: {len(slides)}")
    assert len(slides) == 320, f"Expected 320 slides, got {len(slides)}"
    
    # 2. Check each module has exactly 80 slides
    m1 = [s for s in slides if s["module_no"] == 1]
    m2 = [s for s in slides if s["module_no"] == 2]
    m3 = [s for s in slides if s["module_no"] == 3]
    m4 = [s for s in slides if s["module_no"] == 4]
    
    assert len(m1) == 80, f"Module 1 count mismatch: {len(m1)}"
    assert len(m2) == 80, f"Module 2 count mismatch: {len(m2)}"
    assert len(m3) == 80, f"Module 3 count mismatch: {len(m3)}"
    assert len(m4) == 80, f"Module 4 count mismatch: {len(m4)}"
    print("  [PASS] All 4 modules have exactly 80 slides (80 * 4 = 320).")
    
    # 3. Check for KTU Previous Year Questions (PYQs)
    pyq_slides = [s for s in slides if s.get("category") == "pyq_solution" or "KTU" in s.get("title", "") or "KTU" in s.get("badge", "")]
    assert len(pyq_slides) >= 12, f"Expected at least 12 PYQ slides, got {len(pyq_slides)}"
    print(f"  [PASS] Found {len(pyq_slides)} KTU PYQ exam solution slides across all modules.")
    
    # Check Dec 2023, Jan 2024, May 2024 mentions
    titles_and_badges = " ".join([s["title"] + " " + s["badge"] for s in slides])
    assert "Dec 2023" in titles_and_badges, "Dec 2023 PYQ missing"
    assert "Jan 2024" in titles_and_badges, "Jan 2024 PYQ missing"
    assert "May 2024" in titles_and_badges, "May 2024 PYQ missing"
    print("  [PASS] KTU University exam sessions (Dec 2023, Jan 2024, May 2024) verified.")
    
    # 4. Check JS data file exists and contains EXAM_SLIDES_320
    assert os.path.exists(js_path), f"JS data file missing: {js_path}"
    with open(js_path, "r", encoding="utf-8") as f:
        js_content = f.read()
    assert "window.EXAM_SLIDES_320" in js_content, "EXAM_SLIDES_320 not defined in JS"
    print("  [PASS] exam_slides_data.js defines window.EXAM_SLIDES_320.")
    
    # 5. Check HTML slide presenter and 10 Liquid Glass Theme classes
    assert os.path.exists(html_path), f"HTML presenter missing: {html_path}"
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
        
    themes = [
        "theme-liquid", "theme-frosted", "theme-aurora", "theme-crystal",
        "theme-holographic", "theme-translucent", "theme-neumorphic",
        "theme-scifi", "theme-academic", "theme-highcontrast"
    ]
    for th in themes:
        assert th in html_content, f"Theme {th} missing from lecture_slides.html"
    print("  [PASS] All 10 Liquid Glass themes are present and selectable in lecture_slides.html.")
    
    # 6. Check website/index.html includes exam_slides_data.js
    assert os.path.exists(website_path), f"Website index.html missing: {website_path}"
    with open(website_path, "r", encoding="utf-8") as f:
        web_content = f.read()
    assert "exam_slides_data.js" in web_content, "exam_slides_data.js not referenced in website/index.html"
    assert "window.EXAM_SLIDES_320" in web_content, "EXAM_SLIDES_320 not referenced in website/index.html"
    print("  [PASS] website/index.html embedded viewer linked to 320 exam slides.")

    print("\nALL 320 EXAM SLIDES TESTS PASSED PERFECTLY!\n")

if __name__ == "__main__":
    test_exam_slides()
