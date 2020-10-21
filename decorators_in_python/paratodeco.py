# decorating function with parameter
import functools

user = {'username': 'Jose', 'access_level': 'guest'}


def make_secure(access_level):
    def decorator(funct):
        @functools.wraps(funct)
        def secure_function(*args, **kwargs):
            if user['access_level'] == access_level:
                return funct(*args, **kwargs)
            else:
                return f"No {access_level} permission for {user['username']}"

        return secure_function
    return decorator


@make_secure('admin')
def get_admin_password():
    return 'admin: 1234'


@make_secure('guest')
def get_dashboard_password():
    return 'user: user_password'


# we can pass parameters to decorated function with args and kwargs
@make_secure
def get_password(panel):
    if panel == 'admin':
        return '1234'
    elif panel == 'billing':
        return 'Secured password.'


# this line is replaced by @ above function
# get_admin_password = make_secure(get_admin_password())

print(get_admin_password())
print(get_dashboard_password())

