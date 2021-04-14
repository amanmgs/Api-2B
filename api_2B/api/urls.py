from django.urls import include, re_path, path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import User_ViewSet, LoginView, StripeView

router = DefaultRouter()
router.register('User', User_ViewSet)

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("StripeView/", StripeView.as_view(), name="StripeView"),
]

urlpatterns += router.urls