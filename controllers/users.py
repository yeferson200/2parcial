from flask import flash
from models import users
import hashlib

def getAllUsers():
    dataUsers = users.getAllUsers()
    
    return dataUsers

def crearUsuario(nombres, apellidos, email, contrasena):
    isValid = True

    if not nombres:
        flash('El nombre es obligatorio')
        isValid = False
    
    if not apellidos:
        flash('El apellido es obligatorio')
        isValid = False
    
    if not email:
        flash('El email es obligatorio')
        isValid = False

    if not contrasena:
        flash('El contrasena es obligatorio')
        isValid = False
    
    if not isValid:
        return False

    nuevaContrasena = hashlib.sha256(contrasena.encode())

    users.crearUsuario(nombres, apellidos, email, nuevaContrasena.hexdigest())

    return True