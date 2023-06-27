from django.urls import path
from .views import ViewEnterprise, IndexEnterprises, LoginManager

urlpatterns = [
    path('login/', LoginManager.as_view(), name='login_manager'),
    path('enteprises/', IndexEnterprises.as_view(), name='manager_enterprises'),
    path('enteprises/<str:name>', ViewEnterprise.as_view(), name='enterprise')
]
