import webapp2
import helper
import renderer
from google.appengine.api import users


interest_list = helper.original_interest_list


class Handler(webapp2.RequestHandler):
    def get(self):
        values = helper.get_template_parameters()
        email = helper.get_user_email()
        p = helper.get_user_profile(email)
        if p:
            user_interest = helper.get_user_interest(helper.get_user_email())
            user_interest_state = []
            for interest in interest_list:
                user_interest_state.append({
                                            'name': interest,
                                            'value': interest in user_interest
                                            })

            values['interest_list'] = user_interest_state
        else:
            user_interest_state = []
            for interest in interest_list:
                user_interest_state.append({
                                            'name': interest,
                                            'value': False
                                            })

            values['interest_list'] = user_interest_state

        self.response.write(renderer.render_template(
                            self, "edit_profile.html", values))
