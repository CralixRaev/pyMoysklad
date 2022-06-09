class ApiError(Exception):
    code: int | None = None

    def __init__(self, *args, code: int | None = None):
        super().__init__(*args)
        if not self.code:
            self.code = code


class AuthError(ApiError):
    code = 1056


class EntityNotFoundError(ApiError):
    code = 1021


ERRORS = {
    1056: AuthError,
    1021: EntityNotFoundError
}
