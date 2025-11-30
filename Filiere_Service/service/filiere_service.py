from repository.filiere_repository import FiliereRepository
from mapper.filiere_mapper import FiliereMapper
from dto.request_filiere_dto import RequestFiliereDTO

class FiliereService:
    def __init__(self):
        self.repo = FiliereRepository()
        self.mapper = FiliereMapper()

    def add_filiere(self, dto: RequestFiliereDTO):
        filiere = self.mapper.dto_to_entity(dto)
        saved = self.repo.save(filiere)
        return self.mapper.entity_to_dto(saved)

    def get_all(self):
        return [self.mapper.entity_to_dto(f) for f in self.repo.find_all()]

    def get_by_id(self, id):
        filiere = self.repo.find_by_id(id)
        if not filiere:
            return None
        return self.mapper.entity_to_dto(filiere)

    def delete(self, id):
        return self.repo.delete(id)

    def update(self, id, dto: RequestFiliereDTO):
        filiere = self.repo.find_by_id(id)
        if not filiere:
            return None
        if dto.code is not None:
            filiere.code = dto.code
        if dto.libelle is not None:
            filiere.libelle = dto.libelle
        saved = self.repo.save(filiere)
        return self.mapper.entity_to_dto(saved)