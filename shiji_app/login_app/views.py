from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_page(request) -> render:
    """
    Function view of login.html.\n
    Function responsible for handling user authentication.
    
    Based on given conditions:
    1. User is already authenticated (owns token in his/ her cookies in browser):
        * Redirect to home page, after accessing the login page.
    
    2. User is not authenticated and POST request has been sent:
        * Extract passed username and password,
        * Try to extract user from database, if its possible try to authenticate user with given credentials. Authenticated is based on hash weight not sent string.
        * If user is not None, login and redirect user to home page.

    Args:
        request : Request send from form embedded in login page.
        
    Returns:
        render : Rendering propper html template.

    """
    # If user is already authenticated with token, only redirect
    if request.user.is_authenticated:
        # TODO Add redirect to home page after its creation
        return redirect('grafana_app:home')
    
    else:
        # Check whether propper request has been sent
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            try:
                # ! Trying to extract user with given login
                user = User.object.get(username = username)
                
            except:
                # ! When could not extract skip
                pass
            
            # Trying to authenticate user with given credentials
            user = authenticate(request, username = username, password = password)
            
            if user is not None:
                # If user with given credentials exist
                # Login into system
                login(request, user)
                messages.success(request, f'Successfully logged in: {request.user.username}!')
                # TODO add propper redirect to home page after its creation
                return redirect('grafana_app:home')
            
            else:
                messages.error(request, 'Credentials does not match user in our database!')
            
        return render(
            request,
            'login.html',
            {}
        )
        

def logout_page(request) -> render:
    """
    Function view responsible for logging out user from application:
        * If requests has been sent log out from system,
        * Add message to display,
        * Redirect to login page and render its template.
    Args:
        request : Request sent by user. 

    Returns:
        render : Rendering propper html template.
    """
    logout(request)
    messages.success(request, 'Successfully logged out from application!')
    # TODO add redirect to login page after its creation
    return redirect('login_app:login')