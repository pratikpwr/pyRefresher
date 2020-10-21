# decorating function with parameter
import functools

user = {'username': 'Jose', 'access_level': 'admin'}


def make_secure(funct):
    @functools.wraps(funct)
    def secure_function(*args, **kwargs):
        if user['access_level'] == 'admin':
            return funct(*args, **kwargs)
        else:
            return f"No admin permission for {user['username']}"

    return secure_function


@make_secure
def get_admin_password():
    return '1234'


# we can pass parameters to decorated function with args and kwargs
@make_secure
def get_password(panel):
    if panel == 'admin':
        return '1234'
    elif panel == 'billing':
        return 'Secured password.'


# this line is replaced by @ above function
# get_admin_password = make_secure(get_admin_password())

print(get_password('billing'))
