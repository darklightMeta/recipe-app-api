"""
Test for the django admin.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    """
    Test for the django admin.
    """

    def setUp(self):
        """
        Setup for the django admin.
        """
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='sample1234',
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='sample1234',
            name='Test user full name',
        )

    def test_users_listed(self):
        """ Test that users are listed on user page. """
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.user.email)
        self.assertContains(response, self.user.name)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_user_change_page(self):
        """ Test that the user edit page works. """
        url = reverse('admin:core_user_change', args=[self.user.id])
        # /admin/core/user/1
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        """ Test that the create user page works. """
        url = reverse('admin:core_user_add')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
