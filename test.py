import ApiRequest as AR

requestor = AR.ApiRequest()
link = "https://jsonplaceholder.typicode.com/todos/1"
requestor.SendRequest(link)
datatoProcess = requestor.GetReturnData()
print(datatoProcess)
