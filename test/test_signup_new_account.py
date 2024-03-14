def test_signup_new_account(app):
    username = "user2"
    password = "test2"
    app.james.ensure_user_exist(username, password)