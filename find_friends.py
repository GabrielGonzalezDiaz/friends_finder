import webapp2
import helper
import renderer
import friends_suggestion


class Handler(webapp2.RequestHandler):
    def get(self):
        values = helper.get_template_parameters()
        emails = friends_suggestion.find_suggestions()
        first_names = []
        last_names = []
        for e in emails:
            first_names.append(helper.get_user_first_name(e))
        for e in emails:
            last_names.append(helper.get_user_last_name(e))
        prospects = []
        for i in range(0, len(emails)):
            prospects.append((first_names[i], last_names[i]))

        values['prospects'] = prospects
        renderer.render_template(self, 'find_friends.html', values)
