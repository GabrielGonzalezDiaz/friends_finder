import webapp2
import helper
import renderer


class Handler(webapp2.RequestHandler):
    def post(self):
        values = helper.get_template_parameters()
        renderer.render_template(self, 'find_friends.html', values)
