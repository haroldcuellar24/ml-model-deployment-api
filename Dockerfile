FROM python:3.13-bookworm

WORKDIR /app

COPY requirements.txt src/
COPY src/modelo_random_forest.pkl src/
COPY src/app.py src/
COPY src/static/index.html src/static/
COPY src/static/script.js src/static/
COPY src/static/style.css src/static/
COPY src/static/img/history.jpg src/static/img/
COPY src/static/img/recient.jpg src/static/img/

RUN pip install --no-cache-dir -r src/requirements.txt

EXPOSE 5000

CMD ["python", "src/app.py"]