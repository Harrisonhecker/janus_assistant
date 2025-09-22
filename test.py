import ApiRequest as AR

requestor = AR.ApiRequest()
link = "http://localhost:11434/api/generate"
prompt = {
    "model": "gpt-oss",
    "prompt": "What is 2 + 2",
    "stream": False
}

requestor.SendPostRequest(link, prompt)
dataToProcess = requestor.GetReturnData()
answer = dataToProcess['response']
print(answer)

'''requestor = AR.ApiRequest()
link = "https://jsonplaceholder.typicode.com/todos/1"
requestor.SendRequest(link)
datatoProcess = requestor.GetReturnData()
print(datatoProcess)'''