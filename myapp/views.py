from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from rest_framework.exceptions import ValidationError

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from myapp.authentication import HardCodedTokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes

class ProtectedView(APIView):
    # Применяем аутентификацию и авторизацию только к этому эндпоинту
    authentication_classes = [HardCodedTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Доступ разрешён, токен принят."})

class PublicView(APIView):
    # Этот эндпоинт доступен всем без аутентификации
    permission_classes = []

    def get(self, request):
        return Response({"message": "Этот эндпоинт доступен без токена."})


class UserBaseView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @authentication_classes([HardCodedTokenAuthentication])
    @permission_classes([IsAuthenticated])
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


class UserDetail(generics.RetrieveAPIView):
    @authentication_classes([HardCodedTokenAuthentication])
    @permission_classes([IsAuthenticated])
    def get(self, request):
        user_id = request.data.get('id')
        chat_id = request.data.get('chat_id')
        tg_acc = request.data.get('tg_acc')

        if not user_id and not chat_id and not tg_acc:
            raise ValidationError("Вы не передали ни одного аргумента")

        if user_id:
            user = User.objects.get(id=user_id)
        elif chat_id:
            user = User.objects.get(chatid=chat_id)
        elif tg_acc:
            user = User.objects.get(tg_acc=tg_acc)

        return Response({'username': user.username,
                         'tg_acc': user.tg_acc,
                         'chatid': user.chatid,
                         'balance': user.balance,
                         'meeting_count': user.meeting_count,
                         }, status=status.HTTP_200_OK)

    
class UserDetailUpdate(generics.UpdateAPIView):
    @authentication_classes([HardCodedTokenAuthentication])
    @permission_classes([IsAuthenticated])
    def patch(self, request, *args, **kwargs):

        user_id = request.data.get('id')
        chat_id = request.data.get('chat_id')
        tg_acc = request.data.get('tg_acc')
        key = request.data.get('key')
        value = request.data.get('value')


        if not user_id and not chat_id and not tg_acc:
            raise ValidationError("Вы не передали ни одного аргумента по пользователю")
        
        if not key or not value:
            raise ValidationError("Вы не передали ни одного аргумента")

        if user_id:
            user = User.objects.get(id=user_id)
        elif chat_id:
            user = User.objects.get(chatid=chat_id)
        elif tg_acc:
            user = User.objects.get(tg_acc=tg_acc)


        if hasattr(user, key):
            setattr(user, key, value)
            user.save()
            return Response({'success': True}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid field'}, status=status.HTTP_400_BAD_REQUEST)

    @authentication_classes([HardCodedTokenAuthentication])
    @permission_classes([IsAuthenticated])
    def put(self, request, *args, **kwargs):
        return Response({'error': 'Method PUT is not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) # TODO: remove put decloration

class BalanceView(UserBaseView, generics.UpdateAPIView):
    @authentication_classes([HardCodedTokenAuthentication])
    @permission_classes([IsAuthenticated])
    def get(self, request):
        user_id = request.data.get('id')
        chat_id = request.data.get('chat_id')
        tg_acc = request.data.get('tg_acc')

        if not user_id and not chat_id and not tg_acc:
            raise ValidationError("Вы не передали ни одного аргумента")

        if user_id:
            user = User.objects.get(id=user_id)
        elif chat_id:
            user = User.objects.get(chatid=chat_id)
        elif tg_acc:
            user = User.objects.get(tg_acc=tg_acc)

        return Response({'balance': user.balance}, status=status.HTTP_200_OK)

    @authentication_classes([HardCodedTokenAuthentication])
    @permission_classes([IsAuthenticated])
    def patch(self, request):

        user_id = request.data.get('id')
        chat_id = request.data.get('chat_id')
        tg_acc = request.data.get('tg_acc')

        if not user_id and not chat_id and not tg_acc:
            raise ValidationError("Вы не передали ни одного аргумента")

        if user_id:
            user = User.objects.get(id=user_id)
        elif chat_id:
            user = User.objects.get(chatid=chat_id)
        elif tg_acc:
            user = User.objects.get(tg_acc=tg_acc)

        balance = int(request.data.get('balance', 0))

        user.balance += balance
        user.save()
        return Response({'balance': user.balance}, status=status.HTTP_200_OK)

    
    @authentication_classes([HardCodedTokenAuthentication])
    @permission_classes([IsAuthenticated])
    def put(self, request, *args, **kwargs):
        user_id = request.data.get('id')
        chat_id = request.data.get('chat_id')
        tg_acc = request.data.get('tg_acc')

        if not user_id and not chat_id and not tg_acc:
            raise ValidationError("Вы не передали ни одного аргумента")

        if user_id:
            user = User.objects.get(id=user_id)
        elif chat_id:
            user = User.objects.get(chatid=chat_id)
        elif tg_acc:
            user = User.objects.get(tg_acc=tg_acc)

        balance = int(request.data.get('balance', 0))

        user.balance = balance
        user.save()
        return Response({'balance': user.balance}, status=status.HTTP_200_OK)
