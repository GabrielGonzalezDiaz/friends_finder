import webapp2
import social_data
import helper


class Handler(webapp2.RequestHandler):
    def post(self):
        interests = []
        music = self.request.get("music")
        sports = self.request.get("sports")
        games = self.request.get("games")
        if music:
            interests.append("music")
        if sports:
            interests.append("sports")
        if games:
            interests.append("games")
        print(helper.get_user_email())
        social_data.save_interests(interests, helper.get_user_email())
        self.redirect("/profile-view")
