from django.test import TestCase

class CategoryListApiTest(TestCase):

    def test_category_list_api(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)