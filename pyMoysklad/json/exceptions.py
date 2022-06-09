class ApiError(Exception):
    code = None

    def __init__(self, *args, code=None):
        super().__init__(*args)
        self.code = code


class AuthError(ApiError):
    code = 1056

