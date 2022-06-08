class ApiError(Exception):
    __code = None


class AuthError(ApiError):
    __code = 1056

