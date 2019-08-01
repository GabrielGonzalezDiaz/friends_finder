import webapp2
import renderer
import edit_profile
import save_profile
import view_profile
import helper
import friends_suggestion
import find_friends


class MainHandler(webapp2.RequestHandler):
    def get(self):
        values = helper.get_template_parameters()
        email = helper.get_user_email()
        p = helper.get_user_profile(email)
        if p:
            values['user_interest'] = helper.get_user_interest(email)

            values['prospects'] = friends_suggestion.find_suggestions(
                                    self.request.get('Music'))

            self.response.write(renderer.render_template(
                                    self, "main_page.html", values))
        else:
            self.redirect('/profile-edit')


class ErrorHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Something went wrong :(')


app = webapp2.WSGIApplication([
    ('/find_friends', find_friends.Handler),
    ('/profile-edit', edit_profile.Handler),
    ('/profile-save', save_profile.Handler),
    ('/profile-view', view_profile.Handler),
    # ('/.*', ErrorHandler),
    ('/*', MainHandler),
])
