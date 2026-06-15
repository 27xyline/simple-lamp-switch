# Роборука

FastAPI-проект для управления состоянием роборуки.

У роборуки есть два состояния:

- `open` - рука разжата;
- `closed` - рука сжата.

## Запуск

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

После запуска откройте `http://localhost:8000`.

## API

- `GET /` - страница управления роборукой
- `GET /status` - текущее состояние роборуки
- `POST /open` - разжать руку через кнопку или API
- `POST /close` - сжать руку через кнопку или API
- `GET /open` - разжать руку через URL-ссылку
- `GET /close` - сжать руку через URL-ссылку

Прямые ссылки:

- `http://localhost:8000/open` - разжать руку
- `http://localhost:8000/close` - сжать руку