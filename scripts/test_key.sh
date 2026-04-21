#!/bin/bash
set -euo pipefail

cd "$(dirname "$0")/.."

if [ ! -f .env ]; then
  echo "Помилка: .env не знайдено у $(pwd)"
  exit 1
fi

KEY=$(grep "^OPENAI_API_KEY=" .env | cut -d= -f2- | tr -d '"' | tr -d "'")

if [ -z "$KEY" ]; then
  echo "Помилка: OPENAI_API_KEY порожній у .env"
  exit 1
fi

echo "Ключ знайдено: ...${KEY: -8}"
echo "Запит до OpenAI..."
echo ""

curl -sS https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer $KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-4o-mini","messages":[{"role":"user","content":"ping"}]}'

echo ""
