#program.py
#Project generation with the following command: py -m venv env
#Activar entorno virtual con los siguientes pasos: cd env/Scripts y despues: activate

#Check packages: pip freeze.

from datetime import *
from dateutil.relativedelta import *

#Activar antes de ejecutar py app.py

now = datetime.now()
print(now)

now = now + relativedelta(months=1, weeks=1, hour=10)

print(now)