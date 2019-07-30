import webapp2
import social_data
import helper
from google.appengine.api import users
from social_models import UserProfile

interest_list = [
                'Music',
                'Sports',
                'Games',
                'Academia',
                'Programming',
                'Stocks'
                ]


class Handler(webapp2.RequestHandler):
    def post(self):
        interests = []
        for i in range(0, len(interest_list)):
            if(self.request.get(interest_list[i])):
                interests.append(interest_list[i])

        social_data.save_interests(
                            interests, helper.get_user_email())
        self.redirect("/profile-view")
