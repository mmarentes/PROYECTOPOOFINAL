# errores.py

class UsuarioMuyCortoError(Exception):
    def __init__(self, username):
        self.message = f"El nombre de usuario '{username}' es muy corto. Debe tener al menos 2 caracteres."
        super().__init__(self.message)

class LongitudContrasenaInvalidaError(Exception):
    def __init__(self, longitud):
        self.message = f"La contraseña debe tener entre 2 y 10 caracteres. Longitud actual: {longitud}."
        super().__init__(self.message)

class ContrasenaInvalidaError(Exception):
    def __init__(self):
        self.message = "La contraseña debe contener al menos un número."
        super().__init__(self.message)
