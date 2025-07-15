FROM python:3.11.13-slim
RUN pip install flask
WORKDIR /myapp
COPY main.py /myapp/main.py 
CMD ["python", "/myapp/main.py"]
