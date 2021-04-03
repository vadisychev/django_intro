from django.test import TestCase
from django.test import Client
from forms.models import UserInfo


class RegistrationBookTest(TestCase):

    def test_reg_book_is_available(self):
        response = Client().get('/forms/registration_book/')
        self.assertEqual(response.status_code, 200)

    def test_reg_book_is_not_available(self):
        response = Client().get('/forms/')
        self.assertEqual(response.status_code, 404)

    def test_reg_book_sequence_is_correct(self):
        users = UserInfo.objects.all()
        user_index = 1
        for user in users:
            self.assertEqual(user_index, user.id)
            user_index += 1

    def test_content_is_not_empty(self):
        response = self.client.get('/forms/registration_book/')
        self.assertTrue(response.content)

    def test_csrf(self):
        response = Client(enforce_csrf_checks=True).get('/forms/registration_book/')
        self.assertEqual(response.status_code, 200)


class InputInfo(TestCase):

    def test_input_info_page_availability(self):
        response = Client().get('/forms/input_info/')
        self.assertEqual(response.status_code, 200)

    def test_redirect_chain_post(self):
        response = Client(follow=True).post('forms/input_info/', {
                                'first_name': 'test',
                                'last_name': 'test',
                                'user_email': 'test@test.ru'
                                })
        self.assertEqual(response.redirect_chain, '/forms/registration_book/')
        self.assertEqual(response.status_code, 301)
        response = Client(follow=True).post('forms/input_info/', {
                                'first_name': 'test',
                                'last_name': 'test',
                                'user_email': 'testtest.ru'})
        self.assertEqual(response.redirect_chain, '/forms/input_info.html')
        self.assertEqual(response.status_code, 301)
        response = Client(follow=True).post('forms/input_info/',
                               {
                                'first_name': 'test',
                                'last_name': '',
                                'user_email': 'test@test.ru'})
        self.assertEqual(response.redirect_chain, '/forms/input_info.html')
        response = Client(follow=True).post('forms/input_info/',
                               {
                                'first_name': '',
                                'last_name': 'test',
                                'user_email': 'test@test.ru'})
        self.assertEqual(response.redirect_chain, '/forms/input_info.html')

