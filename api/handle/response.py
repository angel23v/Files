# tu_app/handle/response.py

from rest_framework.response import Response
from rest_framework import status

def custom_response(data=None, message=None, status_code=status.HTTP_200_OK):

    response_data = {}
    if data is not None:
        response_data['data'] = data
    if message is not None:
        response_data['message'] = message

    return Response(response_data, status=status_code)
