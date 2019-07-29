import webapp2
import social_data
import renderer
import helper
from social_models import UserProfile



class Handler(webapp2.RequestHandler):
    def get(self):
        values = helper.get_template_parameters()
        email = helper.get_user_email()

        self.response.write(renderer.render_template(
                                    self, "profile_view.html", values))

