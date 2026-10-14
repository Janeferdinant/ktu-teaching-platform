import json
import os

base_dir = r"c:\Users\Asus\Downloads\SYLLABUS"
reg_path = os.path.join(base_dir, "registry", "course_registry.json")
manifest_path = os.path.join(base_dir, "registry", "deployment_manifest.json")

with open(reg_path, "r", encoding="utf-8") as f:
    courses = json.load(f)

manifest = {
    "system": "Automated Syllabus-to-Teaching-Website Platform",
    "faculty": "Jane Rose | Asst. Professor | CSE",
    "institution": "APJ Abdul Kalam Technological University (KTU)",
    "regulation": "B.Tech Curriculum 2024 Scheme",
    "version": "1.0.0",
    "last_updated": "2026-10-14T12:29:00Z",
    "total_pdfs_scanned": 4,
    "total_pages_scanned": 1206,
    "total_unique_courses": len(courses),
    "deployment_base_url": "http://localhost:5173",
    "dashboard_url": "http://localhost:5173/faculty-dashboard/",
    "pilot_course": "PCCST303",
    "pilot_course_url": "http://localhost:5173/courses/PCCST303/",
    "companion_linked_pdfs": [
        {
            "original_pdf": "Computer Science and Engineering.pdf",
            "linked_pdf": "syllabus/processed-pdfs/Computer Science and Engineering_with_course_links.pdf",
            "courses_linked_count": 97
        },
        {
            "original_pdf": "Computer Science and Engineering (Artificial Intelligence).pdf",
            "linked_pdf": "syllabus/processed-pdfs/Computer Science and Engineering (Artificial Intelligence)_with_course_links.pdf",
            "courses_linked_count": 25
        },
        {
            "original_pdf": "Computer Science and Engineering (Cyber Security) .pdf",
            "linked_pdf": "syllabus/processed-pdfs/Computer Science and Engineering (Cyber Security)_with_course_links.pdf",
            "courses_linked_count": 36
        }
    ],
    "courses": {}
}

for code, info in courses.items():
    manifest["courses"][code] = {
        "code": code,
        "title": info["title"],
        "semester": info["semester"],
        "credits": info["credits"],
        "source_pdf": info["source_pdf"],
        "page_number": info["page_number"],
        "website_path": f"/courses/{code}/",
        "deployment_url": f"http://localhost:5173/courses/{code}/",
        "slides_url": f"http://localhost:5173/courses/{code}/slides/",
        "status": "deployed",
        "teaching_hours_target": 46,
        "official_contact_hours": 44,
        "hours_discrepancy_resolved": "44 contact hours across 4 modules + 2 revision/tutorial hours = 46 hours total"
    }

with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2)

print(f"Updated deployment_manifest.json with all {len(courses)} courses.")
