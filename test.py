from django.test import TestCase
from django.test import Client

class SimpleTest(TestCase):
    
    def setUp(self):
        c = Client()	

    def test_correct_user(self):

        c = Client()
        response = c.post('/login/', {'username': 'chris', 'password': '12345qwert'})


        self.assertEqual(response.status_code, 200)

    def test_incorrect_user(self):

    	c = Client()
        response = c.post('/login/', {'username': 'chris', 'password': 'lol'})

        self.assertEqual(response.status_code, 200)

    def test_invalid_pages(self):
     	c = Client()

     	response = c.get('/payment')
     	self.assertEqual(response.status_code, 404)

     	response = c.get('/thrills')
     	self.assertEqual(response.status_code, 404)

    def test_valid_pages_without_login(self):

    	c = Client()

    	response = c.get('/')
     	self.assertEqual(response.status_code, 200)

     	response = c.get('/login/')
     	self.assertEqual(response.status_code, 200)

     	response = c.get('/signup/')
     	self.assertEqual(response.status_code, 200)

     	response = c.get('/about/')
     	self.assertEqual(response.status_code, 200)

     	response = c.get('/index')
     	self.assertEqual(response.status_code, 404)

     	response = c.get('/profile')
     	self.assertEqual(response.status_code, 301)

     	response = c.get('/chatroom')
     	self.assertEqual(response.status_code, 404)

     	response = c.get('/wingmap')
     	self.assertEqual(response.status_code, 302)


    def test_valid_pages_with_login(self):

    	c = Client()

    	response = c.post('/login/', {'username': 'chris', 'password': '12345qwert'})

    	response = c.get('/')
     	self.assertEqual(response.status_code, 200)

     	response = c.get('/login/')
     	self.assertEqual(response.status_code, 200)

     	response = c.get('/signup/')
     	self.assertEqual(response.status_code, 200)

     	response = c.get('/about/')
     	self.assertEqual(response.status_code, 200)

     	response = c.get('/profile')
     	self.assertEqual(response.status_code, 301)

     	response = c.get('/chatroom')
     	self.assertEqual(response.status_code, 404)

     	response = c.get('/wingmap')
     	self.assertEqual(response.status_code, 302)
