from appDjango.models import Familiar

Familiar(nombre="Nahuel", fecha_de_nacimiento="02/01/02",dni=43156879).save()
Familiar(nombre="Matias", fecha_de_nacimiento="20/02/90",dni=43156879).save()
Familiar(nombre="Martin", fecha_de_nacimiento="21/03/86",dni=43156879).save()
Familiar(nombre="Viviana", fecha_de_nacimiento="03/07/67",dni=43156879).save()
print("Se cargo con éxito los usuarios de pruebas")