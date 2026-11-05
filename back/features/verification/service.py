from app import db
from back.models import Verification

def record_verification(asset, result, remarks, username):
    record = Verification(asset=asset, result=result, remarks=remarks.strip(), verified_by=username)
    asset.status = result
    db.session.add(record)
    db.session.commit()
    return record
