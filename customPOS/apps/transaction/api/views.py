from distutils.log import error
import json
from urllib import response
import requests

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.status import HTTP_400_BAD_REQUEST

from customPOS.apps.transaction.api.serializers import (
    TransactionSerializer
)
from customPOS.apps.transaction.models import (Transaction, TransactionItem)
from customPOS.apps.settings.models import (Settings)


class TransactionViewset(ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.none()
    filterset_fields = ["library_id"]
    
    def get_queryset(self, *args, **kwargs):
        return Transaction.objects.all()

    @action(["POST"], detail=False)
    def custom_create(self, request):
        sett = Settings.objects.filter(name='url_save').first()
        default_url = "https://asiacloud.erp.web.id/teratai-demo/weblayer/template/api,CreateSI.vm?"
        save_url = sett.text_value
        post_data = request.data
        payment_amount = post_data["payment_amount"]
        payment_change = post_data["payment_change"]
        items = post_data["items"]
        total = 0
        for item in items: 
            price = item["price"].replace(".","").replace(",","")
            qty = item["qty"].replace(".","").replace(",","")
            total_price = int(price) * int(qty)
            total += total_price
        
        if not total ==  payment_amount:
            return Response(status=HTTP_400_BAD_REQUEST, data={"error": "Not valid payment amount"})
        
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            date = post_data["date"]
            date = f"{date[8:10]}/{date[5:7]}/{date[0:4]}"
            jsondata = {
                "sales_trans": [{
                    "trans_no": post_data["trans_no"],
                    "trans_type": post_data["trans_type"],
                    "location": post_data["location"],
                    "trans_dt": date,
                    "customer": post_data["customer_id"],
                    "create_by": post_data["create_by"],
                    "remark": post_data["remark"],
                    "pmttype": post_data["payment_type"],
                    "pmtterm": post_data["payment_term"],
                    "details": post_data["items"]
                }]
            }
            
            payload = {
                "docs": json.dumps(jsondata)
            }

            request = requests.post(save_url, payload, verify=False)
            response = request.json()
            if response["error"] == 0:
                serializer.save()
                return Response({"message": "transaction saved succesfully"})
            else:
                return Response(status=HTTP_400_BAD_REQUEST, data=response["message"])
