import pymysql

from personal_admon_backend.crud.crud_util import execute_sql


def create_usuario(usuario: dict):

    sql_script = """
        INSERT INTO usuarios (login, password, nickname, email) 
        VALUES ('{login}','{password}','{nickname}','{email}')
    """.format(
        login=usuario["login"],
        password=usuario["password"],
        nickname=usuario["nickname"],
        email=usuario["email"]
    )

    execute_sql(sql_script=sql_script, guardar_cambios=True)


def read_usuario(usuario_id: int) -> dict:
    sql_script = "SELECT * FROM platziblog.usuarios WHERE id=" + str(usuario_id)
    respuesta: dict = execute_sql(sql_script=sql_script, guardar_cambios=False)
    return respuesta


def update_usuario(usuario: dict):
    sql_script = """
    UPDATE usuarios
    SET login= '{login}', password= '{password}', nickname='{nickname}', email='{email}' 
    WHERE id={id}
    """.format(
        id=usuario["id"],
        login=usuario["login"],
        password=usuario["password"],
        nickname=usuario["nickname"],
        email=usuario["email"]
    )
    execute_sql(sql_script=sql_script, guardar_cambios=True)


def delete_usuario(usuario_id: int):
    sql_script = f"DELETE from usuarios where id = {usuario_id}"
    execute_sql(sql_script=sql_script, guardar_cambios=True)


if __name__ == '__main__':
    my_dict = {
        "id": 7,
        "login": "Doña Marina",
        "password": "fabio",
        "nickname": "Marinita",
        "email": "marina@gmail.com"
    }
    update_usuario(usuario=my_dict)