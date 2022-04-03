from rest_framework import serializers
from customPOS.apps.transaction.models import Transaction, TransactionItem


class TransactionItemSerializer(serializers.ModelSerializer):
    # url = serializers.CharField(allow_blank=True, required=False)
    class Meta:
        model = TransactionItem
        fields = '__all__'
        extra_kwargs = {
            'transaction': {'required': False},
        }


class TransactionSerializer(serializers.ModelSerializer):
    # url = serializers.CharField(allow_blank=True, required=False)
    items = TransactionItemSerializer(many=True)
    
    class Meta:
        model = Transaction
        fields = '__all__'
            
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        transaction = Transaction.objects.create(**validated_data)
        for item_data in items_data:
            TransactionItem.objects.create(transaction=transaction, **item_data)
        return transaction

