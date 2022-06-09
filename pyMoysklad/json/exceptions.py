class ApiError(Exception):
    code: int | None = None

    def __init__(self, *args, code: int | None = None):
        super().__init__(*args)
        self.code = code


class AuthError(ApiError):
    code = 1056

