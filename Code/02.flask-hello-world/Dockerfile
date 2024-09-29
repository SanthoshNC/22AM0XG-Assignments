FROM python:3.9-slim-buster

WORKDIR /app
COPY app.py .
RUN pip install flask

EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]