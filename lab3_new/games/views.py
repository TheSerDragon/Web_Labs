import this

from django.http import HttpResponse
from rest_framework import viewsets
from django.db.models import Max, Min, Avg
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# информация о стоимости игры
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_game_pricing(request):
    return Response(Game.objects.aggregate(max_price=Max('price'), min_price=Min('price'), average_cost=Avg('price')))

# выход пользователя
@api_view(['GET'])
def logout_user(request):
    logout(request)
    response = Response({"result": "U_ARE_NO_LONGER_AUTHORIZED"})
    response.set_cookie("is_logged_in",
                        value=False)
    return response


# авторизация
@api_view(['POST'])
def login_user(request):
    username = request.data['login']
    password = request.data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        response = Response({'success': 'U_HAVE_BEEN_AUTHORIZED'})
        response.set_cookie("is_logged_in",
                            value=True,
                            expires=request.session.get_expiry_date())
        print(Users.objects.all())
        return response
    else:
        return Response({'error': 'U_ARE_NOT_AUTHORIZED'})


# регистрация нового пользователя
@api_view(['POST'])
def reg_new_user(request):
    try:
        User.objects.create_user(username=request.data['login'],
                                 password=request.data['password'])
        Users.objects.create(login=request.data['login'],
                             username=request.data['username'],
                             password=request.data['password']).save()
        print(request.data)
        return Response({'success': 'NEW_USER_CREATED'})
    except Exception as e:
        print(e)
        return Response({'error': 'LOGIN_IS_USED'})

# список игры, в т.ч. с поиском и сортировкой
class GameViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GameSerializer
        else:
            return GameSimpleSerializer

    def get_queryset(self):
        queryset = Game.objects.all()
        if self.request.method == 'GET':
            params = self.request.query_params.dict()
            try:
                queryset = queryset.filter(game_name__icontains=params['name'])
            except:
                pass
            try:
                queryset = queryset.filter(price__lte=params['max_price'])
            except:
                pass
            try:
                queryset = queryset.filter(price__gte=params['min_price'])
            except:
                pass
        return queryset.order_by("date_release")

# список заказов
class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GETOrderSerializer
        else:
            return POSTOrderSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user_id = Users.objects.get(login=self.request.user).id
            return Order.objects.filter(userid=user_id)
        else:
            return Order.objects.all()


# корзина
class CartViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user_id = Users.objects.get(login=self.request.user).id
            order_id = Order.objects.filter(userid=user_id, order_statusid=6).first().id
            queryset = Cart.objects.filter(order_id=order_id)
            return queryset
        else:
            queryset = Cart.objects.all()
            return queryset


class OrdersCartViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = None

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user_id = Users.objects.get(login=self.request.user).id
            print(user_id)
            queryset = Cart.objects.filter()
            return queryset
        else:
            queryset = Cart.objects.all()
            return

# получение текущей корзины пользователя
class CurrentCart(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = GameInCartSerializer

    def get_queryset(self):
        print(self.request.user)
        user = Users.objects.get(login=self.request.user)
        user_id = user.id
        order = Order.objects.filter(userid=user_id, order_statusid=6)
        if order.count() != 0:
            self.serializer_class = GameInCartSerializer
            cart = Cart.objects.filter(order_id=order.first().id)
            if cart.count() > 0:
                print('okey')
                return cart
            else:
                self.serializer_class = POSTOrderSerializer
                queryset = Order.objects.filter(id=order.first().id)
                return queryset
        else:
            # у пользователя нет корзины
            # либо все корзины подтверждены и нет новой
            new_order = Order.objects.create(userid=user)
            new_order_id = new_order.id
            new_order.save()
            self.serializer_class = POSTOrderSerializer
            queryset = Order.objects.filter(id=new_order_id)
            return queryset

class GenreViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Genre.objects.all().order_by('genre_name')
    serializer_class = GenreSerializer  # Сериализатор для модели

class PlatformViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Platform.objects.all().order_by('plat_name')
    serializer_class = PlatformSerializer  # Сериализатор для модели

class PublisherViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Publisher.objects.all().order_by('year_found')
    serializer_class = PublisherSerializer  # Сериализатор для модели

class GameFullInfoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = GameSerializer

    def get_queryset(self):
        queryset = Game.objects.select_related('')
        return queryset

class UsersViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  # только менеджерам или админам!
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class OrderStatusViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer