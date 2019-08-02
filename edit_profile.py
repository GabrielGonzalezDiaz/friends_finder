import webapp2
import helper
import renderer


class Handler(webapp2.RequestHandler):
    def get(self):
        values = helper.get_template_parameters()
        email = helper.get_user_email()
        p = helper.get_user_profile(email)
        interest_list = helper.original_interest_list
        user_interest_state = []
        if p:
            user_interest = helper.get_user_interest(helper.get_user_email())
            for interest in interest_list:
                user_interest_state.append({
                                            'name': interest,
                                            'value': interest in user_interest
                                            })
            print user_interest_state
            values['interest_list'] = user_interest_state
            values['first_name'] = helper.get_user_first_name(email)
            values['last_name'] = helper.get_user_last_name(email)
        else:
            for interest in interest_list:
                user_interest_state.append({
                                            'name': interest,
                                            'value': False
                                            })

            values['interest_list'] = user_interest_state

        renderer.render_template(self, "edit_profile.html", values)
