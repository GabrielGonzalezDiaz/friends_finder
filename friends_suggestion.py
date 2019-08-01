from google.appengine.api import users
from user_models import UserProfile
import helper


def find_suggestions(user_interest):
    results = []
    for prospect in UserProfile.query():
        email = prospect.email
        if user_interest in helper.get_user_interest(email):
            results.append((
                            helper.get_user_first_name(email),
                            helper.get_user_last_name(email),
                            email
                            ))

    # for profile in results:
    #     email = profile.email
    #     results.append((helper.get_user_first_name(email),
    #                     helper.get_user_last_name(email),
    #                     email))

    if(len(results) < 1):
        return [("", "", "")]
    return results

    # suggestions = {}
    # for prospect in UserProfile.query():
    #     interests_in_common = 0
    #     for interest in helper.get_user_interest(prospect.email):
    #         if interest in user_interests:
    #             interests_in_common += 1
    #     suggestions[prospect.email] = interests_in_common
    # prospect_list = suggestions.keys()
    # prospect_list.sort(key=lambda name: suggestions[name])
    # return (prospect_list[::-1], suggestions)
