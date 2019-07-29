from social_models import UserProfile


def save_profile(first_name, last_name, email, password, interests, friends):
    p = UserProfile(first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password,
                    interests=interests,
                    friends=friends)
    # if p:
    #     p.name = name
    #     p.description = description
    # else:
    #     p = UserProfile(email=email, name=name, description=description)
    p.put()


def get_user_profile(email):
    q = UserProfile.query(UserProfile.email == email)
    results = q.fetch(1)
    for profile in results:
        return profile
    return None


def get_profile_by_first_name(name):
    q = UserProfile.query(UserProfile.first_name == name)
    results = q.fetch(1)
    for profile in results:
        return profile
    return None


def get_recent_profiles():
    q = UserProfile.query().order(-UserProfile.last_update)
    return q.fetch(50)
