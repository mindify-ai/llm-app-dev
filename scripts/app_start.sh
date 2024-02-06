# Run two commands in the background at the same time
cd ../src
python3 -m uvicorn index.main:app --reload & python3 app/main.py 
