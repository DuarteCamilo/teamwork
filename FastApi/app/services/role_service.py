from app.entities.role_entity import RoleEntity
from app.services.base_service import BaseService


class RoleService(BaseService):
    def __init__(self):
        super().__init__(entity_name="Role", entity=RoleEntity)


role_service = RoleService()


def get_role_service():
    return role_service
