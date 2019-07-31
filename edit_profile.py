import webapp2
import helper
import renderer

interest_list = helper.original_interest_list


class Handler(webapp2.RequestHandler):
    def get(self):
        values = helper.get_template_parameters()
        values['interest_list'] = interest_list
        values['check_boxs'] = [False]*len(interest_list)
        self.response.write(renderer.render_template(
                            self, "edit_profile.html", values))
