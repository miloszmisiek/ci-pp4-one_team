from django.test import TestCase
from .forms import (
    CustomUserCreationForm,
    UserSignupForm,
    EditProfileForm,
    MyCustomResetPasswordKeyForm
    )
from .models import CustomUser


class TestForms(TestCase):

    def test_user_signup_form(self):
        form = UserSignupForm(
            data={
                'username': 'username',
                'email': 'username@mail.com',
                'email2': 'username@mail.com',
                'password1': 'passwor34Rd',
                'password2': 'passwor34Rd',
                'first_name': 'first_name',
                'last_name': 'last_name',
                'rank': CustomUser.ROLES[0][0]
            }
        )
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)
        self.assertEqual(
            form.fields['username'].widget.attrs['placeholder'],
            'Username'
        )
        self.assertEqual(
            form.fields['first_name'].widget.attrs['placeholder'],
            'First Name'
        )
        self.assertEqual(
            form.fields['last_name'].widget.attrs['placeholder'],
            'Last Name'
        )

        self.assertEqual(
            form.fields['email'].widget.attrs['placeholder'],
            'E-mail address'
        )

        self.assertEqual(
            form.fields['email2'].widget.attrs['placeholder'],
            'Confirm e-mail'
        )

        self.assertEqual(
            form.fields['email2'].widget.attrs['placeholder'],
            'Confirm e-mail'
        )

        self.assertEqual(
            form.fields['password2'].widget.attrs['placeholder'],
            'Confirm password'
        )
    
    def test_user_signup_form_invalid_email(self):
        """Test the simple signup form with invalid data."""
        form = UserSignupForm(
            data={
                'username': 'username',
                'email': 'mail.com',
                'email2': 'username@mail.com',
                'password1': 'passwor34Rd',
                'password2': 'passwor34Rd',
                'first_name': 'first_name',
                'last_name': 'last_name',
                'rank': CustomUser.ROLES[1][0]
            })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'Enter a valid email address.')

    def test_user_signup_form_username_is_required(self):
        """Test the simple signup form with invalid data."""
        form = UserSignupForm(
            data={
                'username': '',
                'email': 'username@mail.com',
                'email2': 'username@mail.com',
                'password1': 'passwor34Rd',
                'password2': 'passwor34Rd',
                'first_name': 'first_name',
                'last_name': 'last_name',
                'rank': CustomUser.ROLES[1][0]
            })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'][0], 'This field is required.')


    def test_user_signup_form_emails_no_match(self):
        form = UserSignupForm(
            data={
                'username': 'username',
                'email': 'username@mail.com',
                'email2': 'username2@mail.com',
                'password1': 'passwor34Rd',
                'password2': 'passwor34Rd',
                'first_name': 'first_name',
                'last_name': 'last_name',
                'rank': CustomUser.ROLES[1][0]
            })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertIn('email2', form.errors.keys())
        self.assertEqual(form.errors['email2'][0], 'You must type the same email each time.')

    def test_user_signup_form_passwords_no_match(self):
        form = UserSignupForm(
            data={
                'username': 'username',
                'email': 'username@mail.com',
                'email2': 'username@mail.com',
                'password1': 'passwor34Rd333',
                'password2': 'passwor34Rd',
                'first_name': 'first_name',
                'last_name': 'last_name',
                'rank': CustomUser.ROLES[1][0]
            })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertIn('password2', form.errors.keys())
        self.assertEqual(form.errors['password2'][0], 'You must type the same password each time.')

    def test_user_signup_form_passwords_no_match(self):
        form = UserSignupForm(
            data={
                'username': 'username',
                'email': 'username@mail.com',
                'email2': 'username@mail.com',
                'password1': 'passwor34Rd333',
                'password2': 'passwor34Rd',
                'first_name': 'first_name',
                'last_name': 'last_name',
                'rank': CustomUser.ROLES[1][0]
            })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertIn('password2', form.errors.keys())
        self.assertEqual(form.errors['password2'][0], 'You must type the same password each time.')

    def test_user_signup_form_passwords_no_match(self):
        form = UserSignupForm(
            data={
                'username': 'username',
                'email': 'username@mail.com',
                'email2': 'username@mail.com',
                'password1': 'passwor34Rd',
                'password2': 'passwor34Rd',
                'first_name': 'first_name',
                'last_name': 'last_name',
                'rank': CustomUser.ROLES[1][0]
            })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertIn('password2', form.errors.keys())
        self.assertEqual(form.errors['password2'][0], 'You must type the same password each time.')
    




    # def test_user_signup_form_invalid_password(self):
    #     """Test the simple signup form with invalid data."""
    #     form = UserSignupForm(
    #         data={
    #             'username': 'username',
    #             'email': 'usename@gmail.com',
    #             'password1': 'password',
    #             'password2': 'password',
    #             'first_name': 'first_name',
    #             'last_name': 'last_name',
    #             'phone': '456987786',
    #             'role': CustomUser.ROLES[5][0]
    #         }
    #     )
    #     self.assertFalse(form.is_valid())
    #     self.assertEquals(len(form.errors), 1)

    # def test_user_signup_form_invalid_no_data(self):
    #     """Test the simple signup form with invalid data."""
    #     form = UserSignupForm(data={})
    #     self.assertFalse(form.is_valid())
    #     self.assertEquals(len(form.errors), 8)

    # def test_user_signup_form_invalid_no_username(self):
    #     """Test the simple signup form with invalid data."""
    #     form = UserSignupForm(
    #         data={
    #             'username': '',
    #             'email': 'username@mail.com',
    #             'password1': 'passwor34Rd',
    #             'password2': 'passwor34Rd',
    #             'first_name': 'first_name',
    #             'last_name': 'last_name',
    #             'phone': '456987786',
    #             'role': CustomUser.ROLES[5][0]
    #         }
    #     )
    #     self.assertFalse(form.is_valid())
    #     self.assertEquals(len(form.errors), 1)

    # def test_user_signup_form_invalid_no_email(self):
    #     """Test the simple signup form with invalid data."""
    #     form = UserSignupForm(
    #         data={
    #             'username': 'username',
    #             'email': '',
    #             'password1': 'passwor34Rd',
    #             'password2': 'passwor34Rd',
    #             'first_name': 'first_name',
    #             'last_name': 'last_name',
    #             'phone': '456987786',
    #             'role': CustomUser.ROLES[5][0]
    #         }
    #     )
    #     self.assertFalse(form.is_valid())
    #     self.assertEquals(len(form.errors), 1)

    # def test_user_signup_form_invalid_no_password(self):
    #     """Test the simple signup form with invalid data."""
    #     form = UserSignupForm(
    #         data={
    #             'username': 'username',
    #             'email': 'username@gmail.com',
    #             'password1': '',
    #             'password2': '',
    #             'first_name': 'first_name',
    #             'last_name': 'last_name',
    #             'phone': '456987786',
    #             'role': CustomUser.ROLES[5][0]
    #         }
    #     )
    #     self.assertFalse(form.is_valid())
    #     self.assertEquals(len(form.errors), 2)

    # def test_user_signup_form_invalid_no_first_name(self):
    #     """Test the simple signup form with invalid data."""
    #     form = UserSignupForm(
    #         data={
    #             'username': 'username',
    #             'email': 'username@gmail.com',
    #             'password1': 'passwor34Rd',
    #             'password2': 'passwor34Rd',
    #             'first_name': '',
    #             'last_name': 'last_name',
    #             'phone': '456987786',
    #             'role': CustomUser.ROLES[5][0]
    #         }
    #     )
    #     self.assertFalse(form.is_valid())
    #     self.assertEquals(len(form.errors), 1)

    # def test_user_signup_form_invalid_no_last_name(self):
    #     """Test the simple signup form with invalid data."""
    #     form = UserSignupForm(
    #         data={
    #             'username': 'username',
    #             'email': 'username@gmail.com',
    #             'password1': 'passwor34Rd',
    #             'password2': 'passwor34Rd',
    #             'first_name': 'first_name',
    #             'last_name': '',
    #             'phone': '456987786',
    #             'role': CustomUser.ROLES[5][0]
    #         }
    #     )
    #     self.assertFalse(form.is_valid())
    #     self.assertEquals(len(form.errors), 1)

    # def test_user_signup_form_invalid_no_phone(self):
    #     """Test the simple signup form with invalid data."""
    #     form = UserSignupForm(
    #         data={
    #             'username': 'username',
    #             'email': 'username@gmail.com',
    #             'password1': 'passwor34Rd',
    #             'password2': 'passwor34Rd',
    #             'first_name': 'first_name',
    #             'last_name': 'last_name',
    #             'phone': '',
    #             'role': CustomUser.ROLES[5][0]
    #         }
    #     )
    #     self.assertFalse(form.is_valid())
    #     self.assertEquals(len(form.errors), 1)

