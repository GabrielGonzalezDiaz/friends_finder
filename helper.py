from google.appengine.api import users
from social_models import UserProfile

original_interest_list = [
                'Music',
                'Sports',
                'Games',
                'Academia',
                'Programming',
                'Stocks'
                ]


def get_user_profile(email):
    q = UserProfile.query(UserProfile.email == email)
    results = q.fetch(1)
    for profile in results:
        return profile


def get_user_email():
    user = users.get_current_user()
    if user:
        return user.email()
    else:
        return None


def get_user_first_name(email):
    q = UserProfile.query(UserProfile.email == email)
    results = q.fetch(1)
    for profile in results:
        return profile.first_name


def get_user_last_name(email):
    q = UserProfile.query(UserProfile.email == email)
    results = q.fetch(1)
    for profile in results:
        return profile.last_name


def get_user_interest(email):
    q = UserProfile.query(UserProfile.email == email)
    results = q.fetch(1)
    for profile in results:
        return profile.interest


def get_user_check_box_values(email):
    q = UserProfile.query(UserProfile.email == email)
    results = q.fetch(1)
    for profile in results:
        return profile.check_box_valies


def get_user_friends(email):
    q = UserProfile.query(UserProfile.email == email)
    results = q.fetch(1)
    for profile in results:
        return profile.friends


def get_template_parameters():
    values = {}
    if get_user_email():
        values['logout_url'] = users.create_logout_url('/')
    else:
        values['login_url'] = users.create_login_url('/')
    return values
