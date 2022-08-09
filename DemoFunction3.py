#DemoFunction3.py
#정의되지 않은 인자 : 필수 + 옵션
def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL

#호출
print(userURIBuilder("test.com", "80", id="kim", name="mike"))
print(userURIBuilder("test.com", "80", id="kim", name="mike", age="30"))

