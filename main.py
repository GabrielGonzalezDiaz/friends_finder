import webapp2
import renderer


class MainHandler(webapp2.RequestHandler):
    def get(self):
        values = {}
        self.response.write(renderer.render_template(
                                                    self,
                                                   "main_page.html",
                                                    values)
                            )


app = webapp2.WSGIApplication([
    ('/*', MainHandler),
])
