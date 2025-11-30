from dto.response_filiere_dto import ResponseFiliereDTO
from entity.filiere import Filiere

class FiliereMapper:
    def dto_to_entity(self, dto):
        return Filiere(code=dto.code, libelle=dto.libelle)

    def entity_to_dto(self, filiere: Filiere):
        return ResponseFiliereDTO(
            id_filiere=filiere.id_filiere,
            code=filiere.code,
            libelle=filiere.libelle
        )