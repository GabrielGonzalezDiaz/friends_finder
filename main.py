import os
import webapp2
import social_data
import renderer
import edit_profile
import save_profile
import view_profile
import helper

from google.appengine.api import users
from google.appengine.ext.webapp import template



class MainHandler(webapp2.RequestHandler):
    def get(self):
        values = helper.get_template_parameters()
        email = helper.get_user_email()

        self.response.write(renderer.render_template(
                                    self, "main_page.html", values))


social_data.save_profile("bob", "billy", helper.get_user_email() , "hello", [], [])


app = webapp2.WSGIApplication([
    ('/profile-edit', edit_profile.Handler),
    ('/profile-save', save_profile.Handler),
    ('/profile-view', view_profile.Handler),
    ('/*', MainHandler),
])
