FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /app

CMD ["uvicorn", "index.main:app", "--host", "0.0.0.0", "--port", "80"]