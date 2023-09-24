import json


def Paid_check(name, db, model):
    query = db.query(model).filter(model.name == name).first()
    paid = json.loads(query)
    is_paid = paid["paid"]
    if is_paid == True:
        pass
    if is_paid == False:
        return False