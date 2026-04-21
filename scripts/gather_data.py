import wikipediaapi
from pathlib import Path

TOPICS = [
    ("Чернівці", "chernivtsi_city.txt"),
    ("Чернівецький національний університет імені Юрія Федьковича", "chernivtsi_university.txt"),
    ("Буковина", "bukovyna.txt"),
    ("Ольга Кобилянська", "kobylyanska.txt"),
]

wiki = wikipediaapi.Wikipedia(user_agent="lab0-rag-student/1.0", language="uk")
data_dir = Path(__file__).parent.parent / "data"
data_dir.mkdir(exist_ok=True)

for title, fname in TOPICS:
    try:
        page = wiki.page(title)
        if not page.exists():
            print(f"[!] Стаття '{title}' не знайдена")
            continue
        (data_dir / fname).write_text(page.text, encoding="utf-8")
        print(f"[+] {fname}: {len(page.text)} символів")
    except Exception as e:
        print(f"[!] {title}: {e}")

print("\nГотово.")
