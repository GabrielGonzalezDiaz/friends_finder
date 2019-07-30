import webapp2
import helper
import renderer
from social_models import UserProfile


def get_user_profile(email):
    q = UserProfile.query(UserProfile.email == email)
    results = q.fetch(1)
    for profile in results:
        return profile
    return None


class Handler(webapp2.RequestHandler):
    def get(self):
        values = helper.get_template_parameters()
        self.response.write(renderer.render_template(
                                                    self,
                                                   "edit_profile.html",
                                                    values)
                            )


class InterestHandler(webapp2.RequestHandler):
    def post(self):
        music = self.request.get("music")
        print music
