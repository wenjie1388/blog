from rest_framework import authentication
from rest_framework import exceptions
from consumer.models import Consumer as User

# class IsConsumerAuthentication(authentication.BaseAuthentication):
#     def authenticate(self, request):
#         req_query = request.query_params
#         account = req_query
#         try:
#           user=User.objects.get(req_query.)
