import mysql

# Conexión a la base de datos (si no existe, se creará)
conexion = mysql.connect('pruebas.db')

# Creación de un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Creación de una tabla
cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                    id_clientes int auto_increment primary key,
                    nombre varchar,
                    email varchar
                )''')

# Insertar datos de ejemplo
cursor.execute("INSERT INTO clientes (nombre, email) VALUES (?, ?)", ('Juan', 30))
cursor.execute("INSERT INTO clientes (nombre, email) VALUES (?, ?)", ('María', 25))

# Guardar los cambios y cerrar la conexión
conexion.commit()
conexion.close()
