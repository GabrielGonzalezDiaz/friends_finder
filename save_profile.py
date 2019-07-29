import webapp2
import social_data
import main
import renderer
from social_models import UserProfile


class Handler(webapp2.RequestHandler):
    def post(self):
        interests = []
        music = self.request.get("music")
        if music:
            interests.append("music")
        print(main.get_user_email())
        social_data.save_interests(interests, main.get_user_email())
