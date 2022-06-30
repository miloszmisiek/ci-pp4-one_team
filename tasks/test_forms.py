from django import forms
from django.test import TestCase
from .forms import AddTask
from .models import Task, TASK_APPROVAL, TASK_PRIORITY, TASK_STATUS
from users.models import CustomUser
from django.contrib.auth import get_user_model


USER = get_user_model()
ALL_USERS = USER.objects.all()


class TestForms(TestCase):
    """Test Case for forms"""

    def setUp(self):
        """Set up for unit tests"""
        self.user = CustomUser.objects.create_user(
            username="funny",
            email="just-for-testing@testing.com",
            password="dummy-insecure",
            first_name="John",
            last_name="Travolta",
            rank=CustomUser.ROLES[1][0],
        )

    def test_add_task_form_metafields_explicit(self):
        """Test the add task form - fields match the
        model with assigned_to argument passed in"""

        form = AddTask(
            assigned_to=ALL_USERS,
            data={
                "title": "title",
                "description": "description",
                "assigned_to": self.user,
                "priority": TASK_PRIORITY[0][0],
                "start_date": "2022-09-10",
                "end_date": "2022-09-20",
            },
        )
        self.assertTrue(form.is_valid())

        self.assertEquals(len(form.errors), 0)

        self.assertEqual(
            form.Meta.fields,
            [
                "title",
                "description",
                "assigned_to",
                "priority",
                "start_date",
                "end_date",
            ],
        )

        self.assertEquals(form.fields["assigned_to"].empty_label, None)

    def test_add_task_form_assigned_to_not_passed_in_form(self):
        """Test the add task form - assigned_to argument not passed"""

        form = AddTask(
            assigned_to=ALL_USERS,
            data={
                "title": "title",
                "description": "description",
                "assigned_to": None,
                "priority": TASK_PRIORITY[0][0],
                "start_date": "2022-09-10",
                "end_date": "2022-09-20",
            },
        )
        self.assertFalse(form.is_valid())

        self.assertEquals(len(form.errors), 1)

    def test_add_task_form_start_date_accepts_only_date_values(self):
        """Test the add task form -
        user input start date with incorect date format"""

        form = AddTask(
            assigned_to=ALL_USERS,
            data={
                "title": "title",
                "description": "description",
                "assigned_to": self.user,
                "priority": TASK_PRIORITY[0][0],
                "start_date": "hshs",
                "end_date": "2022-09-20",
            },
        )
        with self.assertRaises(
            TypeError
        ):  # for clean method called when AddTask instance created
            self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertIn("start_date", form.errors.keys())
        self.assertEqual(form.errors["start_date"][0], "Enter a valid date.")

    def test_add_task_form_end_date_accepts_only_date_values(self):
        """Test the add task form -
        user input end date with incorect date format"""
        form = AddTask(
            assigned_to=ALL_USERS,
            data={
                "title": "title",
                "description": "description",
                "assigned_to": self.user,
                "priority": TASK_PRIORITY[0][0],
                "start_date": "2022-09-10",
                "end_date": "asdas",
            },
        )
        with self.assertRaises(
            TypeError
        ):  # for clean method called when AddTask instance created
            self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertIn("end_date", form.errors.keys())
        self.assertEqual(form.errors["end_date"][0], "Enter a valid date.")

    def test_add_task_form_title_no_value(self):
        """Test the add task form - no title input"""

        form = AddTask(
            assigned_to=ALL_USERS,
            data={
                "title": "",
                "description": "description",
                "assigned_to": self.user,
                "priority": TASK_PRIORITY[0][0],
                "start_date": "2022-09-10",
                "end_date": "2022-09-20",
            },
        )

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertIn("title", form.errors.keys())
        self.assertEqual(form.errors["title"][0], "This field is required.")

    def test_add_task_form_description_no_value(self):
        """Test the add task form - no description input"""

        form = AddTask(
            assigned_to=ALL_USERS,
            data={
                "title": "title",
                "description": "",
                "assigned_to": self.user,
                "priority": TASK_PRIORITY[0][0],
                "start_date": "2022-09-10",
                "end_date": "2022-09-20",
            },
        )

        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)

    def test_add_task_form_assigned_to_no_value(self):
        """Test the add task form - assigned_to no input"""

        form = AddTask(
            assigned_to=ALL_USERS,
            data={
                "title": "title",
                "description": "description",
                "assigned_to": " ",
                "priority": TASK_PRIORITY[0][0],
                "start_date": "2022-09-10",
                "end_date": "2022-09-20",
            },
        )

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertIn("assigned_to", form.errors.keys())
        self.assertEqual(
            form.errors["assigned_to"][0],
            "Select a valid choice. That choice is not one of the available choices.",
        )

    def test_add_task_form_priority_no_value(self):
        """Test the add task form - priority no input"""

        form = AddTask(
            assigned_to=ALL_USERS,
            data={
                "title": "title",
                "description": "description",
                "assigned_to": self.user,
                "priority": "",
                "start_date": "2022-09-10",
                "end_date": "2022-09-20",
            },
        )

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertIn("priority", form.errors.keys())
        self.assertEqual(form.errors["priority"][0], "This field is required.")

    def test_add_task_form_start_date_no_value(self):
        """Test the add task form - start_date no input"""

        form = AddTask(
            assigned_to=ALL_USERS,
            data={
                "title": "title",
                "description": "description",
                "assigned_to": self.user,
                "priority": TASK_PRIORITY[0][0],
                "start_date": "",
                "end_date": "2022-09-20",
            },
        )

        with self.assertRaises(
            TypeError
        ):  # for clean method called when AddTask instance created
            self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertIn("start_date", form.errors.keys())
        self.assertEqual(form.errors["start_date"][0], "This field is required.")

    def test_add_task_form_end_date_no_value(self):
        """Test the add task form - end_date no input"""

        form = AddTask(
            assigned_to=ALL_USERS,
            data={
                "title": "title",
                "description": "description",
                "assigned_to": self.user,
                "priority": TASK_PRIORITY[0][0],
                "start_date": "2022-09-10",
                "end_date": "",
            },
        )

        with self.assertRaises(
            TypeError
        ):  # for clean method called when AddTask instance created
            self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertIn("end_date", form.errors.keys())
        self.assertEqual(form.errors["end_date"][0], "This field is required.")

    def test_add_task_form_start_date_greater_than_end_date(self):
        """Test the add task form -
        start_date greater than end_date  raises error"""

        form = AddTask(
            assigned_to=ALL_USERS,
            data={
                "title": "title",
                "description": "description",
                "assigned_to": self.user,
                "priority": TASK_PRIORITY[0][0],
                "start_date": "2022-09-13",
                "end_date": "2022-09-10",
            },
        )
        self.assertRaises(forms.ValidationError)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["__all__"][0],
            "End date should be greater or equal than start date.",
        )
