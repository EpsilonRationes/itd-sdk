class NoCookie(Exception):
    def __str__(self):
        return 'No cookie for refresh-token required action'

class NoAuthData(Exception):
    def __str__(self):
        return 'No auth data. Provide token or cookies'

class InvalidCookie(Exception):
    def __str__(self):
        return f'Invalid cookie data'

class InvalidToken(Exception):
    def __str__(self):
        return f'Invalid access token'


class SamePassword(Exception):
    def __str__(self):
        return 'Old and new password must not equals'

class InvalidOldPassword(Exception):
    def __str__(self):
        return 'Old password is incorrect'

class NotFound(Exception):
    def __init__(self, obj):
        self.obj = obj
    def __str__(self):
        return f'{self.obj} not found'

class UserBanned(Exception):
    def __str__(self):
        return 'User banned'

class ValidationError(Exception):
    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value
    def __str__(self):
        return f'Failed validation on {self.name}: "{self.value}"'

class PendingRequestExists(Exception):
    def __str__(self):
        return 'Pending verifiaction request already exists'

class RateLimitExceeded(Exception):
    def __init__(self, retry_after: int):
        self.retry_after = retry_after
    def __str__(self):
        return f'Rate limit exceeded - too much requests. Retry after {self.retry_after} seconds'