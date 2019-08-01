import webapp2
import helper
import renderer
import friends_suggestion


class Handler(webapp2.RequestHandler):
    def post(self):

        values = helper.get_template_parameters()
        suggestions = friends_suggestion.find_suggestions(
            self.request.get('wanted_interest'))
        values['prospects'] = suggestions
        values['user_interest'] = helper.original_interest_list
        # emails = suggestions[0]
        # interest_in_common = suggestions[1]
        # first_names = []
        # last_names = []
        # for e in emails:
        #     first_names.append(helper.get_user_first_name(e))
        # for e in emails:
        #     last_names.append(helper.get_user_last_name(e))
        # prospects = []
        # for i in range(0, len(emails)):
        #     prospects.append((first_names[i], last_names[i], interest_in_common[emails[i]]))

        # values['prospects'] = prospects
        renderer.render_template(self, 'find_friends.html', values)
