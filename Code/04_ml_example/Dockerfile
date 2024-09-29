FROM python:3.9-slim-buster
WORKDIR /app
RUN pip install scikit-learn
COPY "01_email.py" .
CMD ["python", "01_email.py"]
