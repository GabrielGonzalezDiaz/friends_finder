import webapp2
import social_data
import renderer
import helper
from social_models import UserProfile
import user_models
from google.appengine.api import users


class Handler(webapp2.RequestHandler):
    def get(self):
        values = helper.get_template_parameters()
        values['first_name'] = UserProfile.first_name
        values['last_name'] = UserProfile.last_name
        values['interest_list'] = user_models.get_user_interest(users.get_current_user())

        self.response.write(renderer.render_template(
                                    self, "profile_view.html", values))
