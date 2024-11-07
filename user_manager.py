# user_manager.py

from errores import UsuarioMuyCortoError, LongitudContrasenaInvalidaError, ContrasenaInvalidaError

class UserManager:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def register_user(self, username, password):
        # Validaciones
        if len(username) < 2:
            raise UsuarioMuyCortoError(username)
        
        if len(password) < 2 or len(password) > 10:
            raise LongitudContrasenaInvalidaError(len(password))

        if not any(char.isdigit() for char in password):
            raise ContrasenaInvalidaError()
        
        if username in self.users:
            return False
        
        self.users[username] = password
        return True

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            self.current_user = username
            return True
        return False

    def logout(self):
        self.current_user = None

    def get_current_user(self):
        return self.current_user
