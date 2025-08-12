def is_valid(username, password):
    # Write code here
    if username == "admin":
        return (True)
    elif username == "user":
        if password == "qweasd":
            return (True)
        else:
            return (False)
    else:
        return (False)