from google.appengine.ext import ndb
import helper

interest_list = helper.original_interest_list


class UserProfile(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    email = ndb.StringProperty()
    password = ndb.StringProperty()
    interest = ndb.StringProperty(repeated=True)
    friends = ndb.IntegerProperty(repeated=True)
    last_update = ndb.DateTimeProperty(auto_now=True)


def get_user_interest(user):
    q = UserProfile.query(UserProfile.email == user.email())
    results = q.fetch(1)
    for profile in results:
        return profile.interests
    return None
