import random
import string

def random_username(prefix, maxlen):
    symbol = string.ascii_letters
    return prefix+"".join([random.choice(symbol) for i in range(random.randrange(maxlen))])
def test_signup_new_account(app):
    app.session.ensure_logout()
    username = random_username("user_", 10)
    print(username)
    password = "test"
    email = username+"@localhost"
    app.james.ensure_user_exist(username, password)
    app.signup.new_user(username, email, password)
    assert app.soap.can_login(username, password)
