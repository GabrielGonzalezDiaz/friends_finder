from google.appengine.api import users
from user_models import UserProfile
import helper


def find_suggestions():

    user = helper.get_user_email()
    user_interests = set(helper.get_user_interest(user))
    suggestions = {}
    for prospect in UserProfile.query():
        interests_in_common = 0
        for interest in helper.get_user_interest(prospect.email):
            if interest in user_interests:
                interests_in_common += 1
        suggestions[prospect.email] = interests_in_common
    prospect_list = suggestions.keys()
    prospect_list.sort(key=lambda name: suggestions[name])
    return prospect_list[::-1]
