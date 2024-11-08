# app/services/user_service.py
from app.dao.user_dao import UserDAO
from app.dto.user_dto import UserDTO

class UserService:
    def __init__(self):
        self.user_dao = UserDAO()

    def create_user(self, user_data):
        user_dto = UserDTO(**user_data)
        self.user_dao.save_user(user_dto)
