class ErrorResponse:
    REQUIRED_FIELDS_USER_RESPONSE = "Email, password and name are required fields" # 403
    USER_ALREADY_EXISTS_RESPONSE = "User already exists" # 403
    INCORRECT_FIELDS_RESPONSE = "email or password are incorrect"
    SHOULD_BE_AUTHORISED_RESPONSE = "You should be authorised"
