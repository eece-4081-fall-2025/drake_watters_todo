from django.test import TestCase
from django.urls import reverse
from five.models import Task


class TaskTests(TestCase):
    def test_list_shows_tasks(self):
        Task.objects.create(title="Buy milk")
        resp = self.client.get(reverse("task_list"))
        self.assertContains(resp, "Buy milk")

    def test_create_task(self):
        resp = self.client.post(
            reverse("task_create"), {"title": "Write report", "notes": "", "due": ""}
        )
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(Task.objects.filter(title="Write report").exists())

    def test_edit_task(self):
        t = Task.objects.create(title="Draft")
        resp = self.client.post(
            reverse("task_update", args=[t.pk]),
            {"title": "Draft v2", "notes": "", "due": ""},
        )
        self.assertEqual(resp.status_code, 302)
        t.refresh_from_db()
        self.assertEqual(t.title, "Draft v2")

    def test_delete_task(self):
        t = Task.objects.create(title="Temp")
        resp = self.client.post(reverse("task_delete", args=[t.pk]))
        self.assertEqual(resp.status_code, 302)
        self.assertFalse(Task.objects.filter(pk=t.pk).exists())

    def test_toggle_complete(self):
        t = Task.objects.create(title="Check", is_completed=False)
        self.client.get(reverse("task_toggle_complete", args=[t.pk]))
        t.refresh_from_db()
        self.assertTrue(t.is_completed)
