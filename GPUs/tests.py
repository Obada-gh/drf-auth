from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import rtx

# Create your tests here.
class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='testuser', password='password')
        test_user.save()

        test_rtx = rtx.objects.create(
            company = test_user,
            title = 'rtx3070',
            description = 'It feel good when you walk at night, espcially with a cup of coffee'
        )
        test_rtx.save()

    def test_blog_content(self):
        rtxtest_rtx = rtx.objects.get(id=1)
        actual_company = str(rtxtest_rtx.company)
        actual_title = str(rtxtest_rtx.title)
        actual_body = str(rtxtest_rtx.description)
        self.assertEqual(actual_company, 'testuser')
        self.assertEqual(actual_title, 'rtx3070')
        self.assertEqual(actual_body, 'It feel good when you walk at night, espcially with a cup of coffee')
