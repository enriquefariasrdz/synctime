FROM python:3.9-slim-buster

WORKDIR /app

COPY global_clock.py /app/
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "global_clock:app", "--host", "0.0.0.0", "--port", "8000"]
