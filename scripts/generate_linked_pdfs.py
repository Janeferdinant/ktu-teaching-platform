import os
import pymupdf
import json

base_dir = r"c:\Users\Asus\Downloads\SYLLABUS"
output_dir = os.path.join(base_dir, "syllabus", "processed-pdfs")
os.makedirs(output_dir, exist_ok=True)

registry_path = os.path.join(base_dir, "registry", "course_registry.json")
with open(registry_path, "r", encoding="utf-8") as f:
    courses = json.load(f)

source_pdfs = [
    ("Computer Science and Engineering.pdf", "Computer Science and Engineering_with_course_links.pdf"),
    ("Computer Science and Engineering (Artificial Intelligence).pdf", "Computer Science and Engineering (Artificial Intelligence)_with_course_links.pdf"),
    ("Computer Science and Engineering (Cyber Security) .pdf", "Computer Science and Engineering (Cyber Security)_with_course_links.pdf")
]

base_url = "http://localhost:5173"

for src_name, out_name in source_pdfs:
    src_path = os.path.join(base_dir, src_name)
    out_path = os.path.join(output_dir, out_name)
    
    if not os.path.exists(src_path):
        print(f"Skipping {src_name} (not found).")
        continue
        
    print(f"Processing {src_name}...")
    doc = pymupdf.open(src_path)
    links_inserted = 0
    
    for code, info in courses.items():
        if info.get("source_pdf") == src_name:
            p_num = info.get("page_number", 1) - 1
            if 0 <= p_num < len(doc):
                page = doc[p_num]
                target_url = f"{base_url}{info.get('website_url', f'/courses/{code}/')}"
                
                rect = pymupdf.Rect(40, 20, 555, 42)
                page.draw_rect(rect, color=(0.14, 0.53, 0.85), fill=(0.94, 0.97, 1.0), width=1.0)
                link_text = f"🌐 Interactive Teaching Website & Notes: {target_url}"
                page.insert_text((50, 34), link_text, fontsize=8.5, fontname="helv", color=(0.02, 0.28, 0.58))
                
                link_dict = {
                    "kind": pymupdf.LINK_URI,
                    "from": rect,
                    "uri": target_url
                }
                page.insert_link(link_dict)
                links_inserted += 1
                
    doc.save(out_path)
    doc.close()
    print(f"Saved {out_name} with {links_inserted} clickable course links.")

print("\nAll 3 companion PDFs generated successfully with clickable links!")
