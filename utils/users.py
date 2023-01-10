users = [
        {"name": "invalid_user", "email": "invalidUser@test.com", "password": "qwert1235"},
        {"name": "11111", "password": "admin"},#valid user
        {"name": "Staff2", "email": "staff@test.com", "password": "qwert1235"},
        {"name": "Admin0", "email": "admin@test.com", "password": "qwert1234"},
        {"name": "Admin1", "email": "admin@test.com", "password": "qwert1234"},
        {"name": "Admin2", "email": "admin@test.com", "password": "qwert1234"},
    ]
class getUser():
    def get_user(name):
        try:
            return next(user for user in users if user["name"] == name)
        except:
            print("\n     User %s is not defined, enter a valid user.\n" % name)
