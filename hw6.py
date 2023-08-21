def readable_function_name(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__.replace('_', ' ').title()
        args_str = ', '.join([f"{arg_name}={arg_value}" for arg_name, arg_value in kwargs.items()])
        result = f'"{func_name} [{args_str}]"'
        print(result)
        return result

    return wrapper


@readable_function_name
def open_browser(browser_name):
    pass


@readable_function_name
def go_to_companyname_homepage(page_url):
    pass


@readable_function_name
def find_registration_button_on_login_page(page_url, button_text):
    pass


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


test_readable_function()
