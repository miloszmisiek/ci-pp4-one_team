from django.contrib.auth.models import User
from django.test.client import Client
from django.test import TestCase
from .models import CustomUser

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        # create users
        self.user_master = CustomUser.objects.create(
            username='master',
            email='master@gmail.com',
            password='master',
            first_name='master',
            last_name='master',
            rank=CustomUser.ROLES[0][0],
        )
        self.user_senior = CustomUser.objects.create(
            username='senior',
            email='senior@gmail.com',
            password='senior',
            first_name='senior',
            last_name='senior',
            rank=CustomUser.ROLES[1][0],
        )
        self.user_junior = CustomUser.objects.create(
            username='junior',
            email='junior@gmail.com',
            password='junior',
            first_name='junior',
            last_name='junior',
            rank=CustomUser.ROLES[2][0],
        )
        self.user_bosun = CustomUser.objects.create(
            username='bosun',
            email='bosun@gmail.com',
            password='bosun',
            first_name='bosun',
            last_name='bosun',
            rank=CustomUser.ROLES[3][0],
        )

    
    def test_get_edit_profile_page(self):
        self.client.force_login(self.user_master)
        response = self.client.get(f'/users/edit_profile/{self.user_master.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/edit_profile.html')
        self.client.logout()
        self.client.force_login(self.user_junior)
        response = self.client.get(f'/users/edit_profile/{self.user_master.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/edit_profile.html')
        
    # def test_get_edit_profile_page_user_not_matched(self):
    #     self.client.force_login(self.user_junior)
    #     response = self.client.get(f'/users/edit_profile/{self.user_master.id}')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'users/edit_profile.html')
    # def test_can_delete_profile_page(self):

    # def test_password_change_view_redirect(self):