from google.appengine.ext import ndb


class UserProfile(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    email = ndb.StringProperty()
    password = ndb.StringProperty()
    interests = ndb.StringProperty(repeated=True)
    friends = ndb.IntegerProperty(repeated=True)
    last_update = ndb.DateTimeProperty(auto_now=True)
