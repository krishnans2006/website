import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("creds.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


def get_projects():
    return list(db.collection("Projects")
                .order_by("Pinned", direction=firestore.Query.DESCENDING)
                .order_by("Winner", direction=firestore.Query.DESCENDING)
                .order_by("Order", direction=firestore.Query.DESCENDING)
                .stream()
                )
