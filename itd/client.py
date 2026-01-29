from itd.users import get_user

class Client:
    def __init__(self, token: str):
        self.token = token.replace('Bearer ', '')

    def get_user(self, username: str) -> dict:
        return get_user(self.token, username)

    def get_me(self) -> dict:
        return self.get_user('me')