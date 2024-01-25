FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Set default values for environment variables
ENV OPENAI_ORG_ID=default_org_id
ENV OPENAI_API_KEY=default_api_key

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /app

CMD ["uvicorn", "index.main:app", "--host", "0.0.0.0", "--port", "80"]
