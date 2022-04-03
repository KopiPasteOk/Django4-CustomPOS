from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from customPOS.apps.user.api import views
from customPOS.apps.transaction.api.views import TransactionViewset

# if settings.DEBUG:
router = DefaultRouter()
# else:
# router = SimpleRouter()

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'transaction', TransactionViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]