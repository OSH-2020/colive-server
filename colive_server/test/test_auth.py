from colive_server.auth import load_user, add_user, del_user


def test_user_action():
    user = add_user(1)
    user_loaded = load_user(user.id)
    assert user == user_loaded

    del_user(user.id)
    assert load_user(user.id) is None
