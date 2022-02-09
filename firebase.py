import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('C:\Users\mukul\Downloads\webrtc1-b74b3-firebase-adminsdk-7by0o-942fca23d7.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
print(db);