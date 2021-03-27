from django.test import TestCase
from django.contrib.auth.models import User
from .models import KeyboardReview, KeyboardName, KeyboardType
from .forms import KeyboardForm, KeyboardImageForm
import datetime
from django.urls import reverse_lazy, reverse

# Create your tests here.
class KeyboardTypeTest(TestCase):
    def setUp(self):
        self.type=KeyboardType(typename='membrane')
    
    def test_typestring(self):
        self.assertEqual(str(self.type), 'membrane')

    def test_tablename(self):
        self.assertEqual(str(KeyboardType._meta.db_table), 'keyboardtype')

class KeyboardNameTest(TestCase):
    def setUp(self):
        self.type=KeyboardType(typename='mechanical')
        self.user=User(username='batman')
        self.keyboardname=KeyboardName(keyboardname='K65 Mini', keyboardtype=self.type, user=self.user, dateentered=datetime.date(2021, 10, 20), price=90, keyboardurl='https://www.corsair.com/us/en/Categories/Products/Gaming-Keyboards/RGB-Mechanical-Gaming-Keyboards/K65-RGB-MINI-60%25-Mechanical-Gaming-Keyboard/p/CH-9194014-NA', description="good keyboard")

    def test_typestring(self):
        self.assertEqual(str(self.keyboardname), 'K65 Mini')

    def test_tablename(self):
        self.assertEqual(str(KeyboardName._meta.db_table), 'keyboardname')

class KeyboardReviewTest(TestCase):
    def setUp(self):
        self.name=KeyboardName(keyboardname='K65 Mini')
        self.user=User(username='batman')
        self.keyboardreview=KeyboardReview(keyboardname=self.name, user=self.user, dateentered=datetime.date(2021, 10, 20), keyboardimage="https://www.vortez.net/news_file/17397_logitech_g_pro_x_mechanical_gaming_keyboard.jpg", keyboardreview="A good keyboard")

    def test_typestring(self):
        self.assertEqual(str(self.keyboardreview), 'https://www.vortez.net/news_file/17397_logitech_g_pro_x_mechanical_gaming_keyboard.jpg')

    def test_tablename(self):
        self.assertEqual(str(KeyboardReview._meta.db_table), 'keyboardimage')

class NewKeyboardForm(TestCase):
    def test_keyboardform(self):
        data={
            'keyboardname' : 'K65 Mini', 
            'keyboardtype' : 'mechanical', 
            'user' : 'batman', 
            'dateentered' : '2021-10-20',
            'price' : '90',
            'keyboardurl' : 'https://www.vortez.net/news_file/17397_logitech_g_pro_x_mechanical_gaming_keyboard.jpg',
            'description' : 'A good keyboard'
        }
        form=KeyboardForm(data)
        self.assertTrue(form.is_valid)

class newKeyboardImage(TestCase):
    def test_keyboardimageform(self):
        data={
            'keyboardname' : 'K65 Mini', 
            'user' : 'batman', 
            'dateentered' : '2021-10-20',
            'keyboardimage' : 'https://www.vortez.net/news_file/17397_logitech_g_pro_x_mechanical_gaming_keyboard.jpg',
            'keyboardreview' : 'A good keyboard'
        }
        form=KeyboardImageForm(data)
        self.assertTrue(form.is_valid)

class New_Keyboard_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='user1', password='123456')
        self.type=KeyboardType.objects.create(typename='membrane')
        self.name=KeyboardName(keyboardname='K65 Mini', keyboardtype=self.type, user=self.test_user, dateentered=datetime.date(2021, 10, 20), price=90, keyboardurl='https://www.corsair.com/us/en/Categories/Products/Gaming-Keyboards/RGB-Mechanical-Gaming-Keyboards/K65-RGB-MINI-60%25-Mechanical-Gaming-Keyboard/p/CH-9194014-NA', description="good keyboard")
        self.review=KeyboardReview(keyboardname=self.name, user=self.test_user, dateentered=datetime.date(2021, 10, 20), keyboardimage="https://www.vortez.net/news_file/17397_logitech_g_pro_x_mechanical_gaming_keyboard.jpg", keyboardreview="A good keyboard")

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newkeyboard'))
        self.assertRedirects(response, '/accounts/login/?next=/keyboard/newkeyboard/')