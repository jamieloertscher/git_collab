FROM python:alpine
WORKDIR /app
COPY app.py /app/
RUN pip install flask
EXPOSE 8080
CMD ["python", "app.py"]