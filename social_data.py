from social_models import UserProfile
import helper

def save_profile(first_name, last_name, email, password, interests, friends):
    p = helper.get_user_profile(email)
    if p:
        p.first_name = first_name
        p.last_name = last_name
        p.email = email
        p.password = password
        p.interests = interests
        p.friends = friends
    else:
        p = UserProfile(first_name=first_name,
                        last_name=last_name,
                        email=email,
                        password=password,
                        interests=interests,
                        friends=friends)
    p.put()


def get_profile_by_first_name(name):
    q = UserProfile.query(UserProfile.first_name == name)
    results = q.fetch(1)
    for profile in results:
        return profile
    return None


def get_recent_profiles():
    q = UserProfile.query().order(-UserProfile.last_update)
    return q.fetch(50)
