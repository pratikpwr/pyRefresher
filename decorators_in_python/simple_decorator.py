import functools
user = {'username': 'Jose', 'access_level': 'admin'}


def make_secure(funct):
    @functools.wraps(funct)
    def secure_function():
        if user['access_level'] == 'admin':
            return funct
        else:
            return f"No admin permission for {user['username']}"

    return secure_function


@make_secure
def get_admin_password():
    return '1234'


# this line is replaced by @ above function
# get_admin_password = make_secure(get_admin_password())

print(get_admin_password())
