#!/bin/sh
# Run the python module while starting the python app with ./app/main.py
python3 -m uvicorn index.main:app --host 0.0.0.0 --port 8000 #& python3 src_app/gradio_main.py