import webapp2
import helper
from user_models import UserProfile


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

        interest_list = helper.original_interest_list
        for interest in interest_list:
            if(self.request.get(interest) and not (interest in p.interest)):
                p.interest.append(interest)
            if(not self.request.get(interest) and interest in p.interest):
                p.interest.remove(interest)

        p.put()

        # self.response.write(renderer.render_template(
        #                             self, "profile_view.html", values))
        self.redirect('/profile-view')
