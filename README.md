# Building your generative AI API in Python 生成式AI後端開發部署實戰

## Course intro:
This course provides a comprehensive guide to designing and developing a backend for an AI chatbot using Python. Participants will learn how to create a robust LLM backend, deploy it with modern CI/CD pipelines and GitHub, and monitor its performance using Microsoft Azure. The course is targeted towards software engineers and developers who want to build an LLM-powered chatbot for their applications. Basic understanding of Python programming is required, and previous experience in software development is a plus. Participants will need an Azure subscription, GitHub account, OpenAI API subscription, Visual Studio Code, Python version 3.8 or higher, and Pip installed. The course covers various topics, including the fundamentals of AI and large-language models, utilizing FastAPI for building an LLM backend, setting up development environments, containerization with Docker, implementing CI/CD pipelines with GitHub Actions, and monitoring AI applications using status pages. Upon completion of the course, participants will have gained the necessary skills to develop and deploy a powerful LLM backend for their AI chatbot projects.

## Getting started
#### Prerequisites
- Python 3.8 or higher
- Docker Installed

#### Installation
```
pip3 install -r requirements.txt
```
#### Start the application
```
cd src/
python3 -m uvicorn index.main:app --reload
```
#### Run unit tests
```
python3 -m pytest
```
