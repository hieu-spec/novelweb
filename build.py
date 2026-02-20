import os
import json

# ====== CẤU HÌNH ======
TXT_FILE = "daiphungdacanhnhan.txt"
BASE_FOLDER = "stories/daiphungdacanhnhan"
CHAP_FOLDER = os.path.join(BASE_FOLDER, "chap")
JSON_FILE = os.path.join(BASE_FOLDER, "chapters.json")
# ======================

# Tạo thư mục nếu chưa tồn tại
os.makedirs(CHAP_FOLDER, exist_ok=True)

chapters = []
chapter_number = 0
current_title = None
content = []

def save_chapter(title, content_list):
    global chapter_number, chapters

    chapter_number += 1
    file_path = os.path.join(CHAP_FOLDER, f"{chapter_number}.txt")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(content_list))

    chapters.append({
        "id": chapter_number,
        "title": title,
        "file": f"chap/{chapter_number}.txt"
    })

# ====== ĐỌC FILE TXT NHẸ RAM ======
with open(TXT_FILE, "r", encoding="utf-8") as f:
    for line in f:
        text = line.strip()

        # Nhận diện chương (có thể mở rộng thêm nếu cần)
        if text.startswith("Chương"):
            if current_title and content:
                save_chapter(current_title, content)
                content = []

            current_title = text
        else:
            if text:
                content.append(text)

# Lưu chương cuối
if current_title and content:
    save_chapter(current_title, content)

# Ghi JSON
with open(JSON_FILE, "w", encoding="utf-8") as f:
    json.dump(chapters, f, ensure_ascii=False, indent=4)

print("Build hoàn tất!")
print("Tổng số chương:", len(chapters))
