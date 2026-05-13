# Лампочка

FastAPI-проект с одной кнопкой, которая переключает состояние лампочки.

## Запуск

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

После запуска откройте `http://localhost:8000`.

## API

- `GET /` - страница с лампочкой
- `GET /status` - текущее состояние
- `POST /toggle` - переключить состояние
- `GET /toggle` - переключить состояние через адресную строку