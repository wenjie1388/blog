from rest_framework.test import APIRequestFactory

# 使用标准的RequestFactory API去创建从POST来的请求
factory = APIRequestFactory()
request = factory.post("/notes/", {"title": "new idea"})
