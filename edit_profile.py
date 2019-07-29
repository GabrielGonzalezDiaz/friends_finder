import webapp2
import renderer


class Handler(webapp2.RequestHandler):
    def get(self):
        values = {}
        self.response.write(renderer.render_template(
                                                    self,
                                                   "edit_profile.html",
                                                    values)
                            )