CLIENT_ACCESS_TOKEN = '<YOUR_CLIENT_ACCESS_TOKEN>' ai = yige.Yige(CLIENT_ACCESS_TOKEN)
>>> request = ai.text_request()
>>> request.query = "我想买鞋"
>>> response = request.getresponse() #注意置信度 confidence
>>> print(response.json())