from entity.filiere import Filiere
from extensions import db

class FiliereRepository:
    def save(self, filiere):
        db.session.add(filiere)
        db.session.commit()
        return filiere

    def find_all(self):
        return Filiere.query.all()

    def find_by_id(self, id):
        return Filiere.query.get(id)

    def delete(self, id):
        filiere = Filiere.query.get(id)
        if filiere:
            db.session.delete(filiere)
            db.session.commit()
            return True
        return False