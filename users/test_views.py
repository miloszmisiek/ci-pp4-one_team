
from django.urls import reverse
from django.test.client import Client
from django.test import TestCase
from .models import CustomUser
from allauth.account.forms import ChangePasswordForm

class TestViews(TestCase):
    """Test the views for the users app."""
    def setUp(self):
        """Set up the test"""
        self.client = Client()
        self.user_master = CustomUser.objects.create_superuser(
            username='master',
            email='master@gmail.com',
            password='master',
            first_name='master',
            last_name='master',
            rank=CustomUser.ROLES[0][0],
        )
        self.user_senior = CustomUser.objects.create_user(
            username='senior',
            email='senior@gmail.com',
            password='senior',
            first_name='senior',
            last_name='senior',
            rank=CustomUser.ROLES[1][0],
        )
        self.user_junior = CustomUser.objects.create_user(
            username='junior',
            email='junior@gmail.com',
            password='junior',
            first_name='junior',
            last_name='junior',
            rank=CustomUser.ROLES[2][0],
        )
        self.user_bosun = CustomUser.objects.create_user(
            username='bosun',
            email='bosun@gmail.com',
            password='bosun',
            first_name='bosun',
            last_name='bosun',
            rank=CustomUser.ROLES[3][0],
        )

    
    def test_get_edit_profile_page(self):
        """Test edit profile page view"""
        self.client.force_login(self.user_bosun)
        response = self.client.get(f'/users/edit_profile/{self.user_bosun.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/edit_profile.html')
    
    def test_get_edit_profile_page_post_rank_same(self):
        """Test edit profile page view post method - rank reamins same"""
        self.client.force_login(self.user_bosun)
        response = self.client.post(f'/users/edit_profile/{self.user_bosun.id}', {
            'first_name': 'first',
            'last_name': 'last',
            'email': 'email@email.com',
            'rank': f'{self.user_bosun.rank}',
        })
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/tasks/my_tasks/')
        self.assertEquals(CustomUser.objects.get(id=self.user_bosun.id).first_name, 'first')
        self.assertEquals(CustomUser.objects.get(id=self.user_bosun.id).last_name, 'last')
        self.assertEquals(CustomUser.objects.get(id=self.user_bosun.id).email, 'email@email.com')
        self.assertEquals(CustomUser.objects.get(id=self.user_bosun.id).rank, self.user_bosun.rank)

    def test_get_edit_profile_page_post_new_rank(self):
        """Test edit profile page view post method - rank change requested"""
        self.client.force_login(self.user_junior)
        response = self.client.post(f'/users/edit_profile/{self.user_junior.id}', {
            'first_name': 'first',
            'last_name': 'last',
            'email': 'email@email.com',
            'rank': 1,
        })
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/inactive/')
        self.assertEquals(CustomUser.objects.get(id=self.user_junior.id).first_name, 'first')
        self.assertEquals(CustomUser.objects.get(id=self.user_junior.id).last_name, 'last')
        self.assertEquals(CustomUser.objects.get(id=self.user_junior.id).email, 'email@email.com')
        self.assertEquals(CustomUser.objects.get(id=self.user_junior.id).rank, 1)
        self.assertFalse(CustomUser.objects.get(id=self.user_junior.id).is_active)

        
    def test_get_edit_profile_page_user_not_matched(self):
        self.client.force_login(self.user_junior)
        response = self.client.get(f'/users/edit_profile/{self.user_master.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/no_permission.html')

    def test_can_delete_profile_page(self):
        self.client.force_login(self.user_senior)
        response = self.client.get(f'/users/delete_profile/{self.user_senior.id}')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        existing_users = CustomUser.objects.filter(id=self.user_senior.id)
        self.assertEqual(len(existing_users), 0)

    def test_cannot_delete_profile_page(self):
        self.client.force_login(self.user_senior)
        response = self.client.get(f'/users/delete_profile/{self.user_junior.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/no_permission.html')
        existing_users = CustomUser.objects.filter(id=self.user_senior.id)
        self.assertEqual(len(existing_users), 1)
    
    def test_superuser_can_delete_other_users(self):
        self.client.force_login(self.user_master)
        response = self.client.get(f'/users/delete_profile/{self.user_junior.id}')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        existing_users = CustomUser.objects.filter(id=self.user_junior.id)
        self.assertEqual(len(existing_users), 0)
    
    def test_superuser_can_edit_other_users(self):
        self.client.force_login(self.user_master)
        response = self.client.get(f'/users/edit_profile/{self.user_bosun.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/edit_profile.html')

    # def test_password_change_redirect(self):
    #     self.client.force_login(self.user_junior)

    #     form = ChangePasswordForm(
    #         data={
    #             'oldpassword': 'junior',
    #             'password1': 'password1',
    #             'password2': 'password1'
    #         },
    #         instance=self.user_junior
    #     )
    #     self.assertTrue(form.is_valid())
    #     self.assertEqual(response.status_code, 200)
    #     response = self.client.get(reverse('account_change_password'))
    #     response = self.client.post('/accounts/password/change/')
    #     print(response.status_code)
    #     self.assertTemplateUsed(response, 'users/edit_profile.html')
    #     self.assertRedirects(
    #         response,
    #         reverse("edit_profile", kwargs={"user_id": self.user_junior.id}),
    #         fetch_redirect_response=False,
    #     )