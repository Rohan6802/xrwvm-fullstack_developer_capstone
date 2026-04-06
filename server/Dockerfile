FROM python:3.12-slim

ENV PYTHONBUFFERED=1
ENV PYTHONWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8000

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["/bin/bash", "./entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]