import json
from urllib import response
import requests

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from customPOS.apps.transaction.api.serializers import (
    TransactionSerializer
)
from customPOS.apps.transaction.models import ( Transaction, TransactionItem )


class TransactionViewset(ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.none()
    filterset_fields = ["library_id"]
    save_url = "http://cloud.erp.web.id:8080/roomart/weblayer/template/api,User.vm?method=saveProfile&email=yusmin.joe@gmail.com&password=trial&firstname=andre&lastname=kedua&dobday=7&dobmonth=11&dobyear=1992&phone=08129453333&address=jl. jeruk manis 7 no 10&tocust=true&ctype=DM151627192557861134072"

    def get_queryset(self, *args, **kwargs):
        return Transaction.objects.all()
    
    @action(["POST"], detail=False)
    def custom_create(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # request data di ubah jadi form data dulu sebelum save
            request = requests.get(self.save_url)
            print(request)
            print(request.headers['content-type'])
            print(request.json())
            response = request.json()
            print(response["userId"])
            # jika response server behasil, olah data untuk masuk serializer baru untuk di save
            # serializer.save()
            return Response(serializer.data)
        return Response({"SUCCESS": False})


