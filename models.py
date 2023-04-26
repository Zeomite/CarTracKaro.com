from firebase_admin import db

def get_data():
    ref = db.reference('/')
    data = {}

    def update_data(event):
        nonlocal data
        data = event.data

    ref.listen(update_data)
    return data
