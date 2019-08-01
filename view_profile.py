import webapp2
import renderer
import helper
import random


class Handler(webapp2.RequestHandler):
    def get(self):
        values = helper.get_template_parameters()
        email = helper.get_user_email()
        values['first_name'] = helper.get_user_first_name(email)
        values['last_name'] = helper.get_user_last_name(email)
        values['interest_list'] = list()
        for interest in helper.get_user_interest(email):
            i = random.randint(1,3)
            values['interest_list'].append({
                'interest': interest,
                'image': '/i/images/' + interest.lower() + '/image' + str(i) + '.JPG'
            })
        renderer.render_template(self, "profile_view.html", values)
