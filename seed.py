from dash import models

def seed():
    test_user = models.User('tester', 'tester@jahvon.me', 'jahvon', True)
    models.db.session.add(test_user)
    print("Creating {}".format(test_user))
    models.db.session.commit()

if __name__ == '__main__':
    seed()