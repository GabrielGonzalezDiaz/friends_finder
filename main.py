
import webapp2
import renderer
import edit_profile
import save_profile
import view_profile
import social_data
import helper


class MainHandler(webapp2.RequestHandler):
    def get(self):
        values = helper.get_template_parameters()
        email = helper.get_user_email()
        p = social_data.get_user_profile(email)
        if p:
            self.response.write(renderer.render_template(
                                    self, "main_page.html", values))
        else:
            self.response.write(renderer.render_template(
                                    self, "edit_profile.html", values))

app = webapp2.WSGIApplication([
    ('/profile-edit', edit_profile.Handler),
    ('/profile-save', save_profile.Handler),
    ('/profile-view', view_profile.Handler),
    ('/*', MainHandler),
])
