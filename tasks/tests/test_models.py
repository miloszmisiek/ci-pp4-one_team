from django.test import TestCase
from ..models import Task, TASK_APPROVAL, TASK_PRIORITY, TASK_STATUS
from users.models import CustomUser
import datetime

class TestModels(TestCase):
    """Test the models for the users app."""

    def setUp(self):
        """Set up the test"""
        self.user_senior = CustomUser.objects.create_user(
            username='senior',
            email='senior@gmail.com',
            password='senior',
            first_name='senior',
            last_name='senior',
            rank=CustomUser.ROLES[1][0],
        )

        self.test_task = Task.objects.create(
            title='default',
            description='default@gmail.com',
            created_by=self.user_senior,
            assigned_to=self.user_senior,
            created_on=datetime.date(2022, 6, 10),
            updated_on=datetime.date(2022, 6, 10),
            end_date=datetime.date(2022, 6, 30),
        )


    def test_approval_status_default_to_scheduled(self):
        """Test default status value."""
        self.assertEquals(self.test_task.status, TASK_STATUS[0][0])

    def test_priority_default_to_low(self):
        """Test default priority value."""
        self.assertEquals(self.test_task.priority, TASK_PRIORITY[2][0])

    def test_approval_status_default_to_waiting(self):
        """Test default approval status value."""
        self.assertEquals(self.test_task.approval_status, TASK_APPROVAL[1][0])

    def test_start_date_default_to_today(self):
        """Test default start date is set to present date."""
        self.assertEquals(self.test_task.start_date, datetime.date.today)

    def test_duration(self):
        """Test duration method"""
        self.assertEqual(self.test_task.duration(), (self.test_task.end_date - self.test_task.start_date).days)

    def test_is_past_due(self):
        """Test is past due method"""
        self.assertEqual(self.test_task.is_past_due(), (datetime.date.today() > self.test_task.end_date, (self.test_task.end_date - datetime.date.today()).days))

    def test_updated_on_time(self):
        """Test is updated on time method"""
        self.assertEqual(self.test_task.updated_on_time(), (datetime.date.today() - self.test_task.updated_on).days)