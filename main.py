import os
import webapp2
import social_data
import renderer

from google.appengine.api import users
from google.appengine.ext.webapp import template

def get_user_email():
    user = users.get_current_user()
    if user:
        return user.email()
    else:
        return None


def get_template_parameters():
    values = {}
    if get_user_email():
        values['logout_url'] = users.create_logout_url('/')
    else:
        values['login_url'] = users.create_login_url('/')
    return values


class MainHandler(webapp2.RequestHandler):
    def get(self):
        values = get_template_parameters()
        email = get_user_email()

        self.response.write(renderer.render_template(
                                    self, "main_page.html", values))

class ProfileTestHandler(webapp2.RequestHandler):
    def get(self):
        values = get_template_parameters()
        self.response.write(renderer.render_template(
                                    self, "profile_test.html", values))

app = webapp2.WSGIApplication([
    ("/profile-test", ProfileTestHandler),
    ('/*', MainHandler),
])
