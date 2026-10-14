import os
import json

base_dir = r"c:\Users\Asus\Downloads\SYLLABUS"
courses_dir = os.path.join(base_dir, "courses")

def test_module_features():
    registry_file = os.path.join(base_dir, "registry", "course_registry.json")
    with open(registry_file, "r", encoding="utf-8") as f:
        courses = json.load(f)

    assert len(courses) >= 150, f"Expected >= 150 courses, found {len(courses)}"
    print(f"Verifying module components across {len(courses)} courses...")

    checked = 0
    for code, c in courses.items():
        idx_path = os.path.join(courses_dir, code, "website", "index.html")
        assert os.path.exists(idx_path), f"Missing index.html for {code}"

        with open(idx_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. 3D canvas demo
        assert "demo-3d-canvas" in content, f"{code} missing demo-3d-canvas"
        assert "switch3DModule" in content, f"{code} missing switch3DModule"

        # 2. Numerical solutions
        assert "sec-numerical" in content, f"{code} missing sec-numerical"
        assert "numerical-card" in content, f"{code} missing numerical-card"

        # 3. Solved PYQ with vector SVG figures
        assert "sec-pyq" in content, f"{code} missing sec-pyq"
        assert "<svg viewBox=\"0 0 760 170\"" in content, f"{code} missing SVG figure in PYQ"
        assert "Figure 1.1:" in content, f"{code} missing Figure 1.1"
        assert "Figure 2.1:" in content, f"{code} missing Figure 2.1"
        assert "Figure 3.1:" in content, f"{code} missing Figure 3.1"
        assert "Figure 4.1:" in content, f"{code} missing Figure 4.1"

        # 4. Applications
        assert "sec-projects" in content, f"{code} missing sec-projects"
        assert "Module 1 • Systems Architecture" in content or "Web Browser Navigation" in content, f"{code} missing Mod 1 application"

        # 5. Module-filtered Quizzes
        assert "quiz-module-pills" in content, f"{code} missing quiz-module-pills"
        assert "filterQuizModule" in content, f"{code} missing filterQuizModule"

        # 6. Module-filtered Knowledge Graph
        assert "kg-module-pills" in content, f"{code} missing kg-module-pills"
        assert "filterKGModule" in content, f"{code} missing filterKGModule"

        # 7. Branding
        assert "Jane Rose | Asst. Professor | CSE" in content, f"{code} missing branding footer"

        checked += 1

    print(f"SUCCESS: All {checked} courses passed all module component verifications!")

if __name__ == "__main__":
    test_module_features()
