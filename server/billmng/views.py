from rest_framework import viewsets, generics, permissions
from django.shortcuts import render, render_to_response
from models import User, Bill
from serializers import UserSerializer, BillSerializer
from forms import BillForm
from django.utils import timezone
from django.utils.crypto import get_random_string
import simplejson

def mainPage(request):
    return render(request, 'base.html', {})

def usersInfo(request):
    return render(request, 'views/user.html', {})

def singleUserDetails(request,id):
    ident = id
    return render(request, 'views/user-info.html', {})

def billsInfo(request):
    return render(request, 'views/bill.html', {})

def chart(request):
    bills = list(Bill.objects.all())
    amountPriceList = []

    for bill in bills:
        amountPriceList.append(bill.amount_price)

    jsonList = simplejson.dumps(amountPriceList)
    return render_to_response('base.html', {"amount_list":jsonList})

def add_bill(request):
    saved = False

    if request.method == 'POST':
        form = BillForm(request.POST)

        if form.is_valid():
            bill = Bill()

            bill.identifier = get_random_string(length=20)

            """Get user"""
            user = User.objects.get(id_card='080123123F')

            bill.user = user
            bill.bill_date = timezone.now()
            bill.amount_price = form.cleaned_data['amount_price']
            bill.taxes = form.cleaned_data['taxes']
            bill.power_consumed = form.cleaned_data['power_consumed']
            saved = True
            bill.save()
        else:
            print(form.errors)
            form = BillForm()


    return render(request, 'views/bill-new.html',locals())

def deleteBill(request, id):
    ident = id
    # delete an object and send a confirmation response
    Bill.objects.get(identifier=request.DELETE['id_bill']).delete()

    return render(request, 'views/bill.html', {})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class UserList(generics.ListCreateAPIView):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserBillsList(generics.ListAPIView):
    serializer_class = BillSerializer

    def get_queryset(self):
        userIdCard = self.kwargs['idcard']
        userObject = User.objects.get(id_card=userIdCard)

        return Bill.objects.filter(user=userObject)


class BillPostList(generics.ListAPIView):
    model = Bill
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    def get_queryset(self):
        queryset = super(BillPostList, self).get_queryset()
        usernamePar = self.kwargs.get('username')
        user = User.objects.get(username=usernamePar)
        return queryset.filter(user=user)
