from django.test import TestCase
from django.utils import timezone
from billmng.models import Bill
from billmng.models import User

class BillTest(TestCase):

    def setUp(self):
        User.objects.create(id_card="080123123F",username="test1",password="test1",first_name="J",
                            last_name="CC",address="test direccion",city="sevilla",
                            province="sevilla",country="Es",zipcode="11050",age=50)
        userObject = User.objects.get(id_card="080123123F")

        Bill.objects.create(identifier="123456",user=userObject, bill_date=timezone.now(),amount_price=54.4,
                            taxes=21,power_consumed=234)

    def test_get_Bill(self):
        bill = Bill.objects.first()

        self.assertTrue(bill.taxes > 0)
