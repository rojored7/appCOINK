# appCOINK

#Paso 1 Clonar el repositorio
#utilice el siguiente comando en consola para windows
$ git clone https://github.com/rojored7/appCOINK.git

#dirijase a la carpeta del repositorio y cree un entorno virtual para ejecutar 
#con el siguiente comando puede crear un entorno virtual
py -m venv venv 

#active el entorno virtual para trabajar dentro del mismo 
.\venv\Scripts\activate

#instale el paquete de django
pip install django

#puede iniciar su git para trabajar en linea
git init

#Utilizando el siguiente comando puede Ignorar archivos de carga a git
fsutil file createnew .gitignore 0

#para realizar la prueba de testing entre a la carpeta donde se encuentra el archivo manage.py 
#ejecute el siguiente comando para la prueba 
py manage.py test formulario
