import qrcode
import pyotp
from PIL import Image

class Servicio:
    #Identificador que proporciona información sobre la entidad que emite el código TOTP
    #En este caso yo, ALBERTO
    ISSUER_NAME = "ALBERTO"

    def __init__(self, nombre):
        self.nombre = nombre
        #Genera un secreto en base 32 de 32 caracteres compatible con Google Authenticator y otras aplicaciones OTP.
        self.secreto = pyotp.random_base32()
        self.totp = pyotp.TOTP(self.secreto)

    def generar_qr(self):
        uri = self.totp.provisioning_uri(name=self.nombre, issuer_name=self.ISSUER_NAME)
        img = qrcode.make(uri)
        img.show()

    def validar_totp(self, codigo):
        return self.totp.verify(codigo)

# Ejemplo de uso
nombre_servicio = "M8T1" #Modulo 8 Tarea 1
mi_servicio = Servicio(nombre_servicio)

# Generar y mostrar el código QR para añadir el servicio
mi_servicio.generar_qr()

# Simular la entrada del usuario para validar el código TOTP
codigo_ingresado = input("Ingresa el código TOTP: ")

# Validar el código TOTP
if mi_servicio.validar_totp(codigo_ingresado):
    print("Código TOTP válido. Acceso concedido.")
else:
    print("Código TOTP inválido. Acceso denegado.")
