from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def main(request):
    """main app page"""
    """redirect to user page"""
    name = request.user.username
    # if we meet  new user
    if request.user.is_anonymous():
        return redirect('user_page', vkuser="new_user")
    return redirect('user_page', vkuser=name)

def user_page(request, vkuser):
    """page with user information"""
    if vkuser != "new_user":
        user = User.objects.get(username=vkuser)
    else:
        user = False
    return render(request, 'somelogin/user.html', {'user': user})