from email_validator import validate_email, EmailNotValidError

def _validate_email(email):
    msg = ''
    validated_email = None
    is_valid = False

    try:
        valid_email = validate_email(email, check_deliverability=True)
        validated_email = valid_email.normalized
        is_valid = True

    except EmailNotValidError as e:
        msg = e
    return is_valid, msg, validated_email

# def validate_unique_email(email):
#     unique = True
#     msg = None
#     user = UserModel.find_one(UserModel.User.email == email)
#     if user.exists():
#         unique = False
#         msg = 'Ooops....An account has already been created with this email.'
#     return unique, msg
    

        
