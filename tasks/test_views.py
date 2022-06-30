from django.test import TestCase
from django.test.client import Client
from users.models import CustomUser
from .models import Task, TASK_APPROVAL, TASK_PRIORITY, TASK_STATUS
from .views import ALL_USERS
from datetime import date, timedelta

TODAY = date.today()
CLEAR_UPDATED = TODAY - timedelta(days=2)
YESTERDAY = TODAY - timedelta(days=1)
CLEAR_UPDATED = TODAY - timedelta(days=2)


class TestViews(TestCase):
    """Test the views for the task app."""

    def setUp(self):
        """Set up the test"""
        self.client = Client()
        self.user_master = CustomUser.objects.create_superuser(
            username="master",
            email="master@gmail.com",
            password="master",
            first_name="master",
            last_name="master",
            rank=CustomUser.ROLES[0][0],
        )
        self.user_senior = CustomUser.objects.create_user(
            username="senior",
            email="senior@gmail.com",
            password="senior",
            first_name="senior",
            last_name="senior",
            rank=CustomUser.ROLES[1][0],
        )
        self.user_junior = CustomUser.objects.create_user(
            username="junior",
            email="junior@gmail.com",
            password="junior",
            first_name="junior",
            last_name="junior",
            rank=CustomUser.ROLES[2][0],
        )
        self.user_bosun = CustomUser.objects.create_user(
            username="bosun",
            email="bosun@gmail.com",
            password="bosun",
            first_name="bosun",
            last_name="bosun",
            rank=CustomUser.ROLES[3][0],
        )

        self.test_task = Task.objects.create(
            title="testtask",
            description="taskdescription",
            status=TASK_STATUS[0][0],
            created_by=self.user_junior,
            assigned_to=self.user_junior,
            priority=TASK_PRIORITY[0][0],
            approval_status=TASK_APPROVAL[0][0],
            created_on="2022-10-09",
            updated_on="2022-10-09",
            start_date="2022-10-09",
            end_date="2022-10-13",
        )
        self.tasks = Task.objects.all()

    def test_get_profile_home_view(self):
        """Test tasks home page view"""
        self.client.force_login(self.user_senior)
        response = self.client.get(f"/tasks/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/profile_home.html")
        self.assertIn(self.test_task, response.context["tasks"])
        self.assertTrue(len(response.context["tasks"]), 1)

    def test_get_profile_home_view_overdue(self):
        """Test tasks home page view - overdue tasks"""
        self.client.force_login(self.user_senior)
        self.test_task.end_date = YESTERDAY
        self.test_task.status = TASK_STATUS[0][0]
        self.test_task.save()
        response = self.client.get(f"/tasks/")
        self.assertEqual(response.status_code, 200)
        self.assertNotEquals(self.test_task.status, response.context["tasks"][0].status)
        self.assertEquals(response.context["tasks"][0].status, 2)

    def test_get_profile_home_view_overdue_to_scheduled(self):
        """Test tasks home page view - overdue tasks"""
        self.client.force_login(self.user_senior)
        self.test_task.end_date = TODAY
        self.test_task.status = TASK_STATUS[2][0]
        self.test_task.save()
        response = self.client.get(f"/tasks/")
        self.assertEqual(response.status_code, 200)
        self.assertNotEquals(self.test_task.status, response.context["tasks"][0].status)
        self.assertEquals(response.context["tasks"][0].status, 0)

    def test_get_profile_home_view_months_filter_no_match(self):
        """Test tasks home page view with months filter not matching"""
        self.client.force_login(self.user_junior)
        response = self.client.get(f"/tasks/?months=3")
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(self.test_task, response.context["tasks"])

    def test_get_profile_home_view_months_filter_match(self):
        """Test tasks home page view with months filter matching"""
        self.client.force_login(self.user_junior)
        response = self.client.get(f"/tasks/?months=6")
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.test_task, response.context["tasks"])

    def test_get_profile_home_view_clear_completed_post_status_completed(self):
        """Test tasks home page view with clear completed post request - task status completed"""
        self.client.force_login(self.user_bosun)
        self.test_task.status = TASK_STATUS[1][0]
        self.test_task.save()
        response = self.client.post("/tasks/", {"hide-completed": ""})
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(self.test_task, response.context["tasks"])

    def test_get_profile_home_view_clear_completed_post_status_scheduled(self):
        """Test tasks home page view with clear completed post request - task status scheduled"""
        self.client.force_login(self.user_bosun)
        response = self.client.post("/tasks/", {"hide-completed": ""})
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.test_task, response.context["tasks"])

    def test_get_profile_home_view_clear_completed_post_status_overdue(self):
        """Test tasks home page view with clear completed post request - task status overdue"""
        self.client.force_login(self.user_bosun)
        self.test_task.status = TASK_STATUS[2][0]
        self.test_task.save()
        response = self.client.post("/tasks/", {"hide-completed": ""})
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.test_task, response.context["tasks"])

    def test_my_tasks_view_task_is_assigned_to_user(self):
        """Test my tasks view - task is assigned to user"""
        self.client.force_login(self.user_junior)
        self.test_task.assigned_to = self.user_junior
        self.test_task.save()
        response = self.client.get("/tasks/my_tasks/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/my_tasks.html")
        self.assertIn(self.test_task, response.context["tasks"])

    def test_my_tasks_view_task_is_not_assigned_to_user(self):
        """Test my tasks view - task is not assigned to user"""
        self.client.force_login(self.user_junior)
        self.test_task.assigned_to = self.user_senior
        self.test_task.save()
        response = self.client.get("/tasks/my_tasks/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/my_tasks.html")
        self.assertNotIn(self.test_task, response.context["tasks"])

    def test_add_task_view_bosun(self):
        """Test add task view - bosun"""
        self.client.force_login(self.user_bosun)
        response = self.client.get("/tasks/create/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/no_permission.html")

    def test_add_task_view_junior_get(self):
        """Test add task view - junior get view"""
        self.client.force_login(self.user_junior)
        response = self.client.get("/tasks/create/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/add_task.html")
        self.assertEquals(
            response.context["form"].initial["assigned_to"], self.user_junior.id
        )
        self.assertEquals(
            response.context["form"].assigned_to[0],
            ALL_USERS.filter(id=self.user_junior.id)[0],
        )

    def test_approve_task_bosun(self):
        """Test approve task view - bosun rank"""
        self.client.force_login(self.user_bosun)
        response = self.client.get(f"/tasks/approve/{self.test_task.id}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/no_permission.html")

    def test_approve_task_junior(self):
        """Test approve task view - junior rank"""
        self.client.force_login(self.user_junior)
        response = self.client.get(f"/tasks/approve/{self.test_task.id}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/no_permission.html")

    def test_approve_task_senior_priority_high(self):
        """Test approve task view - senior rank with high priority task"""
        self.client.force_login(self.user_senior)
        response = self.client.get(f"/tasks/approve/{self.test_task.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.tasks[0].approval_status, 0)
        self.assertTemplateUsed(response, "users/no_permission.html")

    def test_approve_task_senior_priority_medium_waiting(self):
        """Test approve task view - senior rank with medium priority task"""
        self.client.force_login(self.user_senior)
        self.test_task.priority = TASK_PRIORITY[1][0]
        self.test_task.save()
        response = self.client.get(f"/tasks/approve/{self.test_task.id}")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.tasks[0].approval_status, 1)
        self.assertRedirects(response, "/tasks/")

    def test_approve_task_senior_priority_low_waiting(self):
        """Test approve task view - senior rank with low priority task"""
        self.client.force_login(self.user_senior)
        self.test_task.priority = TASK_PRIORITY[2][0]
        self.test_task.save()
        response = self.client.get(f"/tasks/approve/{self.test_task.id}")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.tasks[0].approval_status, 1)
        self.assertRedirects(response, "/tasks/")

    def test_approve_task_senior_priority_medium_approved(self):
        """Test approve task view - senior rank with low priority task"""
        self.client.force_login(self.user_senior)
        self.test_task.priority = TASK_PRIORITY[1][0]
        self.test_task.approval_status = TASK_APPROVAL[1][0]
        self.test_task.save()
        response = self.client.get(f"/tasks/approve/{self.test_task.id}")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.tasks[0].approval_status, 0)
        self.assertRedirects(response, "/tasks/")

    def test_approve_task_senior_priority_low_approved(self):
        """Test approve task view - senior rank with low priority task"""
        self.client.force_login(self.user_senior)
        self.test_task.priority = TASK_PRIORITY[2][0]
        self.test_task.approval_status = TASK_APPROVAL[1][0]
        self.test_task.save()
        response = self.client.get(f"/tasks/approve/{self.test_task.id}")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.tasks[0].approval_status, 0)
        self.assertRedirects(response, "/tasks/")

    def test_approve_task_master(self):
        """Test approve task view - master"""
        self.client.force_login(self.user_master)
        self.test_task.priority = TASK_PRIORITY[0][0]
        self.test_task.approval_status = TASK_APPROVAL[1][0]
        self.test_task.assigned_to = self.user_master
        self.test_task.save()
        response = self.client.get(f"/tasks/approve/{self.test_task.id}")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.tasks[0].approval_status, 0)
        self.assertRedirects(response, "/tasks/")

    def test_approve_task_assigned_to_master(self):
        """Test approve task view - assigned to master, but not to current user"""
        self.client.force_login(self.user_senior)
        self.test_task.priority = TASK_PRIORITY[2][0]
        self.test_task.approval_status = TASK_APPROVAL[1][0]
        self.test_task.assigned_to = self.user_master
        self.test_task.save()
        response = self.client.get(f"/tasks/approve/{self.test_task.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.tasks[0].approval_status, self.test_task.approval_status)
        self.assertTemplateUsed(response, "users/no_permission.html")

    def test_complete_task_bosun(self):
        """Test complete task view - bosun"""
        self.client.force_login(self.user_bosun)
        response = self.client.get(f"/tasks/complete/{self.test_task.id}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/no_permission.html")

    def test_complete_task_junior_scheduled(self):
        """Test complete task view - junior rank scheduled task to complete"""
        self.client.force_login(self.user_junior)
        response = self.client.get(f"/tasks/complete/{self.test_task.id}")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.tasks[0].status, 1)
        self.assertRedirects(response, "/tasks/")

    def test_complete_task_junior_scheduled_not_assigned_to(self):
        """Test complete task view - junior rank task not assgned to user"""
        self.client.force_login(self.user_junior)
        self.test_task.assigned_to = self.user_senior
        self.test_task.save()
        response = self.client.get(f"/tasks/complete/{self.test_task.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.tasks[0].status, self.test_task.status)
        self.assertTemplateUsed(response, "users/no_permission.html")

    def test_complete_task_waiting_to_be_approved(self):
        """Test complete task view - task waiting to be approved"""
        self.client.force_login(self.user_junior)
        self.test_task.approval_status = TASK_APPROVAL[1][0]
        self.test_task.save()
        response = self.client.get(f"/tasks/complete/{self.test_task.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.tasks[0].status, self.test_task.status)
        self.assertTemplateUsed(response, "users/no_permission.html")

    def test_complete_task_assigned_to_master_not_master(self):
        """Test complete task view - task assigned to master, but user is not master"""
        self.client.force_login(self.user_senior)
        self.test_task.assigned_to = self.user_master
        self.test_task.save()
        response = self.client.get(f"/tasks/complete/{self.test_task.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.tasks[0].status, self.test_task.status)
        self.assertTemplateUsed(response, "users/no_permission.html")

    def test_complete_task_status_completed(self):
        """Test complete task view - task status completed to scheduled"""
        self.client.force_login(self.user_senior)
        self.test_task.status = TASK_STATUS[1][0]
        self.test_task.save()
        response = self.client.get(f"/tasks/complete/{self.test_task.id}")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.tasks[0].status, 0)
        self.assertRedirects(response, "/tasks/")

    def test_complete_task_status_overdue(self):
        """Test complete task view - task status overdue to completed"""
        self.client.force_login(self.user_junior)
        self.test_task.status = TASK_STATUS[2][0]
        self.test_task.save()
        response = self.client.get(f"/tasks/complete/{self.test_task.id}")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.tasks[0].status, 1)
        self.assertRedirects(response, "/tasks/")

    def test_delete_task_bosun(self):
        """Test delete task view - bosun"""
        self.client.force_login(self.user_bosun)
        response = self.client.get(f"/tasks/delete/{self.test_task.id}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/no_permission.html")

    def test_delete_task_junior_not_assigned_to(self):
        """Test delete task view - junior rank task not assigned to user"""
        self.client.force_login(self.user_junior)
        self.test_task.assigned_to = self.user_senior
        self.test_task.save()
        response = self.client.get(f"/tasks/delete/{self.test_task.id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.test_task, self.tasks)
        self.assertTemplateUsed(response, "users/no_permission.html")

    def test_delete_task_junior_assigned_to(self):
        """Test delete task view - junior rank task assigned to user"""
        self.client.force_login(self.user_junior)
        response = self.client.get(f"/tasks/delete/{self.test_task.id}")
        self.assertEqual(response.status_code, 302)
        self.assertNotIn(self.test_task, self.tasks)
        self.assertRedirects(response, "/tasks/")

    def test_delete_task_waiting_to_be_approved(self):
        """Test delete task view - task waiting to be approved"""
        self.client.force_login(self.user_junior)
        self.test_task.approval_status = TASK_APPROVAL[1][0]
        self.test_task.save()
        response = self.client.get(f"/tasks/delete/{self.test_task.id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.test_task, self.tasks)
        self.assertTemplateUsed(response, "users/no_permission.html")

    def test_delete_task_assigned_to_master_not_master(self):
        """Test delete task view - task assigned to master, but user is not master"""
        self.client.force_login(self.user_senior)
        self.test_task.assigned_to = self.user_master
        self.test_task.save()
        response = self.client.get(f"/tasks/delete/{self.test_task.id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.test_task, self.tasks)
        self.assertTemplateUsed(response, "users/no_permission.html")

    def test_delete_task_assigned_to_master_master(self):
        """Test delete task view - task assigned to master and user is master"""
        self.client.force_login(self.user_master)
        self.test_task.assigned_to = self.user_master
        self.test_task.save()
        response = self.client.get(f"/tasks/delete/{self.test_task.id}")
        self.assertEqual(response.status_code, 302)
        self.assertNotIn(self.test_task, self.tasks)
        self.assertRedirects(response, "/tasks/")
