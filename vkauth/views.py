from django.shortcuts import render, redirect


def main(request):
    """main app page"""
    """redirect to user page"""
    return redirect('user_page', username="session")
    # потом юзернейм брать из сессии и передавать его

def user_page(request, username):
    """page with user information"""
    return render(request, 'somelogin/user.html', {})