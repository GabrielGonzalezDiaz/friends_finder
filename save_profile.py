import webapp2
import helper
from user_models import UserProfile


interest_list = helper.original_interest_list


class Handler(webapp2.RequestHandler):
    def post(self):

        p = helper.get_user_profile(helper.get_user_email())

        if p:
            pass
        else:
            p = UserProfile()
            p.first_name = self.request.get('first_name')
            p.last_name = self.request.get('last_name')
            p.email = helper.get_user_email()
            p.friends = []
            p.interest = []

        for i in range(0, len(interest_list)):
            if(self.request.get(interest_list[i]) and not interest_list[i] in p.interest):
                p.interest.append(interest_list[i])

        p.put()

        # self.response.write(renderer.render_template(
        #                             self, "profile_view.html", values))
        self.redirect('/profile-view')
