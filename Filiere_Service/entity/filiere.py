from app import db

class Filiere(db.Model):
    __tablename__ = "filiere"
    id_filiere = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(255), nullable=False)
    libelle = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Filiere {self.idFiliere} {self.code}>"