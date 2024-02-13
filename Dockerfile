# Use the custom FastAPI image
# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
# Use ubuntu as base image
FROM ubuntu:20.04

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=noninteractive

# Update apt repositories and install Python and Pip
RUN apt-get update && \
    apt-get install -y python3-pip python3-dev

# Check if the symbolic links already exist and create them if they don't
RUN if [ ! -e /usr/bin/python ]; then ln -s /usr/bin/python3 /usr/bin/python; fi && \
    if [ ! -e /usr/bin/pip ]; then ln -s /usr/bin/pip3 /usr/bin/pip; fi

# Set default values for environment variables
ENV OPENAI_ORG_ID=default_org_id
ENV OPENAI_API_KEY=default_api_key
ENV HUGGINGFACE_API_TOKEN=default_huggingface_token

# Set environment variables for Matplotlib and Fontconfig
ENV MPLCONFIGDIR=/app/matplotlib_cache
ENV FONTCONFIG_PATH=/app/fontconfig

# Create the directories for Matplotlib cache and Fontconfig
RUN mkdir -p /app/matplotlib_cache /app/fontconfig && \
    chmod -R 777 /app/matplotlib_cache /app/fontconfig

# Create a writable directory for Fontconfig cache
RUN mkdir -p /app/fontconfig_cache && chmod -R 777 /app/fontconfig_cache

# Set the environment variable so Fontconfig uses the writable directory
ENV FONTCONFIG_PATH=/app/fontconfig_cache

# Copy the requirements file and install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy your application source code and script
COPY ./api /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]