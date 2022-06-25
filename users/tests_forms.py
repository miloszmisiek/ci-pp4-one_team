from django.test import TestCase
from .forms import (
    CustomUserCreationForm,
    UserSignupForm,
    EditProfileForm,
    MyCustomResetPasswordKeyForm,
    SELECT_YOUR_RANK
    )
from .models import CustomUser


class TestForms(TestCase):

    def test_user_signup_form_placeholders(self):
        """Test the simple signup form - widgets render proper data."""
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
        """Test the simple signup form with invalid email."""
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


    def test_user_signup_form_emails_no_match(self):
        """Test the simple signup form - confirm email does not match the email input."""
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

    def test_user_signup_form_password1_no_match(self):
        """Test the simple signup form - password does not match the confirm password input."""
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

    def test_user_signup_form_password2_no_match(self):
        """Test the simple signup form - confirm password does not match the password input."""
        form = UserSignupForm(
            data={
                'username': 'username',
                'email': 'username@mail.com',
                'email2': 'username@mail.com',
                'password1': 'passwor34Rd',
                'password2': 'passwor34Rd333',
                'first_name': 'first_name',
                'last_name': 'last_name',
                'rank': CustomUser.ROLES[1][0]
            })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertIn('password2', form.errors.keys())
        self.assertEqual(form.errors['password2'][0], 'You must type the same password each time.')

    def test_user_signup_form_username_is_required(self):
        """Test the simple signup form - username is required field."""
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

    def test_user_signup_form_email_is_required(self):
        """Test the simple signup form - email is required field."""
        form = UserSignupForm(
            data={
                'username': 'username',
                'email': '',
                'email2': 'username@mail.com',
                'password1': 'passwor34Rd',
                'password2': 'passwor34Rd',
                'first_name': 'first_name',
                'last_name': 'last_name',
                'rank': CustomUser.ROLES[1][0]
            })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_user_signup_form_email2_is_required(self):
        """Test the simple signup form - confirm email is required field."""
        form = UserSignupForm(
            data={
                'username': 'username',
                'email': 'username@mail.com',
                'email2': '',
                'password1': 'passwor34Rd',
                'password2': 'passwor34Rd',
                'first_name': 'first_name',
                'last_name': 'last_name',
                'rank': CustomUser.ROLES[1][0]
            })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertIn('email2', form.errors.keys())
        self.assertEqual(form.errors['email2'][0], 'This field is required.')

    def test_user_signup_form_password1_is_required(self):
        """Test the simple signup form - password is required field."""
        form = UserSignupForm(
            data={
                'username': 'username',
                'email': 'username@mail.com',
                'email2': 'username@mail.com',
                'password1': '',
                'password2': 'passwor34Rd',
                'first_name': 'first_name',
                'last_name': 'last_name',
                'rank': CustomUser.ROLES[1][0]
            })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertIn('password1', form.errors.keys())
        self.assertEqual(form.errors['password1'][0], 'This field is required.')

    def test_user_signup_form_password2_is_required(self):
        """Test the simple signup form - confirm password is required field."""
        form = UserSignupForm(
            data={
                'username': 'username',
                'email': 'username@mail.com',
                'email2': 'username@mail.com',
                'password1': 'passwor34Rd',
                'password2': '',
                'first_name': 'first_name',
                'last_name': 'last_name',
                'rank': CustomUser.ROLES[1][0]
            })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertIn('password2', form.errors.keys())
        self.assertEqual(form.errors['password2'][0], 'This field is required.')

    def test_user_signup_form_first_name_is_required(self):
        """Test the simple signup form - first name is required field."""
        form = UserSignupForm(
            data={
                'username': 'username',
                'email': 'username@mail.com',
                'email2': 'username@mail.com',
                'password1': 'passwor34Rd',
                'password2': 'passwor34Rd',
                'first_name': '',
                'last_name': 'last_name',
                'rank': CustomUser.ROLES[1][0]
            })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(form.errors['first_name'][0], 'This field is required.')

    def test_user_signup_form_last_name_is_required(self):
        """Test the simple signup form - last name is required field."""
        form = UserSignupForm(
            data={
                'username': 'username',
                'email': 'username@mail.com',
                'email2': 'username@mail.com',
                'password1': 'passwor34Rd',
                'password2': 'passwor34Rd',
                'first_name': 'first_name',
                'last_name': '',
                'rank': CustomUser.ROLES[1][0]
            })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertIn('last_name', form.errors.keys())
        self.assertEqual(form.errors['last_name'][0], 'This field is required.')

    def test_user_signup_form_rank_is_required(self):
        """Test the simple signup form - rank must be selected"""
        form = UserSignupForm(
            data={
                'username': 'username',
                'email': 'username@mail.com',
                'email2': 'username@mail.com',
                'password1': 'passwor34Rd',
                'password2': 'passwor34Rd',
                'first_name': 'first_name',
                'last_name': 'last_name',
                'rank': SELECT_YOUR_RANK[0][0]
            })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertIn('rank', form.errors.keys())
        self.assertEqual(form.errors['rank'][0], 'This field is required.')

    def test_user_signup_form_fields_are_empty(self):
        """Test the simple signup form - all fields are empty"""
        form = UserSignupForm(
            data={
                'username': '',
                'email': '',
                'email2': '',
                'password1': '',
                'password2': '',
                'first_name': '',
                'last_name': '',
                'rank': SELECT_YOUR_RANK[0][0]
            })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 8)


    def test_edit_profile_form_metafields_explicit(self):
        """Test the edit profile form - widgets render proper data."""
        form = EditProfileForm(
            data={
                'first_name': 'first_name',
                'last_name': 'last_name',
                'email': 'username@mail.com',
                'rank': CustomUser.ROLES[1][0]
            }
        )

        self.assertTrue(form.is_valid())

        self.assertEquals(len(form.errors), 0)

        self.assertEqual( form.Meta.fields, ('first_name', 'last_name', 'email', 'rank') )

    def test_edit_profile_form_invalid_email(self):
        """Test the simple signup form with invalid email."""
        form = EditProfileForm(
            data={
                'first_name': 'first_name',
                'last_name': 'last_name',
                'email': 'username@mail.com',
                'rank': CustomUser.ROLES[1][0]
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'Enter a valid email address.')


