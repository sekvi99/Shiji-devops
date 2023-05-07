from django.contrib.auth.models import User
from django.urls import reverse
import pytest

@pytest.fixture
def client_instance():
    """
    Declaring pytest fixture so we can avoid code redundance.
    Returns:
        User: Returing instance of new created User class object.
    """
    return User.objects.create_user(
        username='testuser',
        password='testpassword'
    )


def test_login_success(client, client_instance):
    """
    Test case to check whether after login operation user is propperly redirected with propper response status.
    """
    response = client.post(reverse('login'), {'username': 'testuser', 'password': 'testpass'})
    assert response.status_code == 302 # Expected redirect
    assert response.url == reverse('home') # Redirection to login page

def test_login_failure(client, client_instance):
    response = client.post(reverse('login'), {'username': 'testuser', 'password': 'wrongpass'})
    assert response.status_code == 200 # Expected 200 status after failed login attempt
    assert 'Please enter a correct username and password.' in response.content.decode() # Check whether propper message is displayed after failed login attempt

def test_logout(client, client_instance):
    client.login(username='testuser', password='testpass')
    response = client.get(reverse('logout'))
    assert response.status_code == 302 # Expected redirect after logout
    assert response.url == reverse('login') # Ensure that user is redirected to correct page after logout

def test_login_required(client):
    response = client.get(reverse('home')) # Attempt to get access to home page without sending propper post request
    assert response.status_code == 302 # Check whether user is redirected
    assert response.url == reverse('login') + '?next=' + reverse('home') # Ensure that the user is redirected to the login page if they try to access a page that requires authentication