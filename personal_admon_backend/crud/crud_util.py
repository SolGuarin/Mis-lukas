import pymysql


def execute_sql(sql_script: str, guardar_cambios: bool):
    ############### CONFIGURAR ESTO ###################
    # Abre conexion con la base de datos
    connection = pymysql.connect(
        host="localhost",
        user="postgres",
        password="soleny",
        db="personal_finance",
        cursorclass=pymysql.cursors.DictCursor
    )
    ##################################################

    # prepare a cursor object using cursor() method
    cursor = connection.cursor()

    # ejecuta el SQL query usando el metodo execute().
    cursor.execute(sql_script)

    # procesa una unica linea usando el metodo fetchone().
    data = cursor.fetchone()

    if guardar_cambios == True:
        # Vamos a guardar los cambios hechos por el cursor
        connection.commit()

    # desconecta del servidor
    connection.close()

    return data