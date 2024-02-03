import os 
config = {
    'apiKey': os.environ.get('API_KEY'),
    'authDomain': os.environ.get('YOUR_PROJECT_ID_firebaseapp_com'),
    'databaseURL': os.environ.get('YOUR_PROJECT_ID_firebaseio_com'),
    'projectId': os.environ.get('YOUR_PROJECT_ID'),
    'storageBucket': os.environ.get('YOUR_PROJECT_ID_appspot_com'),
    'messagingSenderId': os.environ.get('YOUR_MESSAGING_SENDER_ID'),
    'appId': os.environ.get('YOUR_APP_ID'),
    'measurementId': os.environ.get('YOUR_MEASUREMENT_ID)'
}
