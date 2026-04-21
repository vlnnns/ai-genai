# ai-genai — Lab 0: RAG System

Лабораторна робота №0 з курсу «Доповнена реальність і генеративний ШІ».
RAG-система на базі Wikipedia-статей про Чернівці та регіон.

## Стек

- Python 3.10
- LangChain + OpenAI (`gpt-4o-mini`, `text-embedding-3-small`)
- FAISS для вектор-індексу
- Jupyter Notebook

## Запуск

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# заповнити .env своїм OPENAI_API_KEY

python scripts/gather_data.py

jupyter notebook notebooks/rag_system.ipynb
```

У ноутбуку виконати комірки по порядку (**Cell → Run All**).

## Структура

- `data/` — текстові джерела (Wikipedia dumps, 4 статті)
- `notebooks/rag_system.ipynb` — основний ноутбук з 8 секціями
- `scripts/gather_data.py` — завантаження статей з української Wikipedia
- `requirements.txt` — фіксовані версії залежностей
- `.env.example` — шаблон для API-ключів
