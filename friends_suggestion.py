from google.appengine.api import users
from user_models import UserProfile
from user_models import get_user_interest


def find_suggestions():

    user = users.get_current_user()
    user_interests = set(get_user_interest(user))
    suggestions = {}
    for prospect in UserProfile.query():
        interests_in_common = 0
        for interest in get_user_interest(prospect):
            if interest in user_interests:
                interests_in_common += 1
        suggestions[prospect.email] = interests_in_common
    prospect_list = suggestions.keys()
    return prospect_list.sort(key=lambda name: suggestions[name])[::-1]

