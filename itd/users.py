from itd.request import fetch


def get_user(token: str, username: str):
    return fetch(token, 'get', f'users/{username}')