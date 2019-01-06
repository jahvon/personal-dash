from dash import models

def seed():
    test_user = models.User('tester', 'tester', 'tester@jahvon.me')
    admin_user = models.User('admin', 'admin', 'admin@jahvon.me')
    models.db.session.add(test_user)
    print("Creating {}".format(test_user))
    models.db.session.add(admin_user)
    print("Creating {}".format(admin_user))
    models.db.session.commit()

if __name__ == '__main__':
    seed()