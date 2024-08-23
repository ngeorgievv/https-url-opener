FROM python:3.9

WORKDIR /app

RUN pip install flask

RUN pip install werkzeug

COPY . .

EXPOSE 8000

CMD ["python", "flask_web_app.py"]