"""

# Read the API key from the WSL environment variable
dev = False
if dev:
    openai.api_key = os.environ["OPENAI_API_KEY"]
else:
    openai.api_key = settings.OPENAI_API_KEY
    
@app.post("/api/docs")
async def generateDocs(request: Request, aiReq: str = Form(...)):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="class Log:\n"+aiReq+"Here's what the above class is doing, explained in a concise way:\n1.",
        temperature=0,
        max_tokens=300,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\"\"\""]
    )
    result = response.choices[0].text
    
    return {"result": result, "request": aiReq}
"""