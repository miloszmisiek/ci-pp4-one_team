from django.test import TestCase
from .models import CustomUser

class TestModels(TestCase):
    """Test the models for the users app."""

    def setUp(self):
        """Set up the test"""
        self.default_rank_user = CustomUser.objects.create_user(
            username='default',
            email='default@gmail.com',
            password='default',
            first_name='default',
            last_name='default',
        )

    def test_rank_default_to_bosun(self):
        """Test default rank value."""
        self.assertTrue(self.default_rank_user.rank, 3)

    def test_string_representation_user(self):
        """Test string representation of created user"""
        self.assertEqual(str(self.default_rank_user), self.default_rank_user.username)


