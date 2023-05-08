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

def test_logout(client, client_instance):
    client.login(username='testuser', password='testpass')
    response = client.get(reverse('logout'))
    assert response.status_code == 302 # Expected redirect after logout
    assert response.url == reverse('login') # Ensure that user is redirected to correct page after logout

def test_login_required(client):
    response = client.get(reverse('home')) # Attempt to get access to home page without sending propper post request
    assert response.status_code == 302 # Check whether user is redirected
    
@pytest.mark.django_db
def test_user_creation():
    # Create a new user
    user = User.objects.create_user(
        username='testuser',
        email='testuser@example.com',
        password='testpassword'
    )

    # Check that the user was created successfully
    assert user.id is not None
    assert user.username == 'testuser'
    assert user.email == 'testuser@example.com'

    # Check that the user's password was hashed properly
    assert user.check_password('testpassword')

    # Try to create a user with a duplicate username
    with pytest.raises(Exception):
        User.objects.create_user(
            username='testuser',
            email='testuser2@example.com',
            password='testpassword2'
        )

    # Try to create a user with a missing required field
    with pytest.raises(Exception):
        User.objects.create_user(
            email='testuser3@example.com',
            password='testpassword3'
        )