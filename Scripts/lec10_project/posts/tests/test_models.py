from django.test import TestCase
from ..models import *
class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print('setUpTestData: Run once to set up non-modified data for all class metods.')
        pass

    def setUp(self):
        print('setUp: Run once for every test method to setup clean data.')
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true")
        self.assertTrue(True)

    # def test_one_plus_one_equals_two(self):
    #     print("Method: test_one_plus_one_equals_two")
    #     post = Posts()
    #     self.assertEqual(1 + 1, 3)

    def test_compare_numbers(self):
        post = Posts()
        self.assertEqual(post.get_number(), 7)



