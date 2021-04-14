from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.response import Response
from .serializers import  User_Serializer
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
import stripe


# Create your views here.

class User_ViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    queryset = User.objects.all()
    serializer_class = User_Serializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        try:
            username = request.data.get("username")
            password = request.data.get("password")
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            user = authenticate(username=username, password=password)
            print(user)
            if user:
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                return Response({"token":token})
            else:
                return Response({"Wrong Credentials"})
        except User.DoesNotExist:
            queryset = None
            return Response({"Wrong Username"})


class StripeView(APIView):
    permission_classes = ([IsAuthenticated,])


    def post(self, request,):
        token = request.data.get("token")
        amount = request.data.get("amount")
        print(token)
        print(amount)

        stripe.api_key = "sk_test_51H2jtoAgAa2kDvY2OZ8azI3GW7XcDFP9OG1TSs8NPueomokE0o2SXruaPP2aXfps3n0xqIqOiYtswtAXbugZ5nsy00rUJpCMuH"
        try:
            charge = stripe.Charge.create(
                    amount=round(int(amount)*100),
                    currency="inr",
                    description='Example charge',
                    source=token,
                )

            return Response(charge)
        except:
            return Response("Wrong Detail")







