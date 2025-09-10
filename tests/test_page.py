def test_standard_user(login_user):
    start = login_user("standard_user")
    start.check_swag_logo_is_visible()

def test_locked_out_user(login_user):
    start = login_user("locked_out_user")
    start.error_message_is_visible()
    start.error_message_has_correct_text()

def test_problem_user(login_user):
    start = login_user("problem_user")
    start.check_swag_logo_is_visible()

def test_performance_glitch_user(login_user):
    start = login_user("performance_glitch_user")
    start.check_swag_logo_is_visible()

def test_error_user(login_user):
    start = login_user("error_user")
    start.check_swag_logo_is_visible()