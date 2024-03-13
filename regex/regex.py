#!/usr/bin/env pyhton3

import re

def validar_correo(correo):

    patron = r"\b[A-Za-z0-9._+-]+@[A-Za-z0-9]+\.[A-Za-z]{2,}\b"
    
    if re.findall(patron, correo):
        return True
    else:
        return False

print(validar_correo("soporte.test@hack4u.io"))
