def check_only_digit(var):
    value = var.get()
    if len(value) > 1:
        var.set(value[:1])
    elif not value.isdigit() and value != "":
        var.set("")


def check_only_letter(var):
    value = var.get()
    if len(value) > 1:
        var.set(value[:1])
    elif value.isdigit() and value != "":
        var.set("")


def find_coordinates(options, search_term):
    for option in options:
        if option[0] == search_term:
            return option[1]["x"], option[1]["y"]
    return None, None


def get_value(key, options):
    for element, category in options:
        if element == key:
            return category



