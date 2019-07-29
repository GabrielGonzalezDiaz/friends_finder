from social_models import UserProfile


def save_profile(first_name, last_name, email, password, interests, friends):
    p = get_user_profile(email)
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


def save_interests(interests, email):
    p = get_user_profile(email)
    print(email)
    print("##################################################3")
    p.interests = interests
    print(p)
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
