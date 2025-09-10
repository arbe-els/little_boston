def test_standard_user(login_user):
    start = login_user("standard_user")
    start.check_swag_logo_is_visible()