from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from rest_framework.exceptions import ValidationError


class UserBaseView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_filtered_queryset(self):
        queryset = self.queryset
        user_id = self.request.query_params.get('id')
        chat_id = self.request.query_params.get('chat_id')
        tg_acc = self.request.query_params.get('tg_acc')

        if not user_id and not chat_id and not tg_acc:
            raise ValidationError("Вы не передали ни одного аргумента")

        if user_id:
            queryset = queryset.filter(id=user_id)
        if chat_id:
            queryset = queryset.filter(chat_id=chat_id)
        if tg_acc:
            queryset = queryset.filter(tg_acc=tg_acc)

        return queryset


class CreateUser(UserBaseView, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(UserBaseView, generics.RetrieveAPIView):
    def get_queryset(self):
        return self.get_filtered_queryset()


class BalanceView(UserBaseView, generics.UpdateAPIView):
    def get(self, request, *args, **kwargs):
        user = self.get_object()
        return Response({'balance': user.balance}, status=status.HTTP_200_OK)

    def get_queryset(self):
        return self.get_filtered_queryset()


class UpdateUser(UserBaseView, generics.UpdateAPIView):
    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        key = request.data.get('key')
        value = request.data.get('value')

        if hasattr(user, key):
            setattr(user, key, value)
            user.save()
            return Response({'success': True}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid field'}, status=status.HTTP_400_BAD_REQUEST)


class AddBalanceView(UserBaseView, generics.UpdateAPIView):
    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        balance = request.data.get('balance', 0)
        user.balance += balance
        user.save()
        return Response({'balance': user.balance}, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        return self.patch(request, *args, **kwargs)
