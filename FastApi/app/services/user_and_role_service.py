from app.entities.user_and_role_entity import UserAndRoleEntity
from app.services.base_service import BaseService


class UserAndRoleService(BaseService):
    def __init__(self):
        super().__init__(entity_name="UserAndRole", entity=UserAndRoleEntity)


user_and_role_service = UserAndRoleService()


def get_user_and_role_service():
    return user_and_role_service
