from personal_admon_backend.crud.crud_util import execute_sql


def create_categoria(nombre_categoria: str):
    sql_script = f"INSERT INTO categorias (nombre_categoria) values ('{nombre_categoria}')"
    execute_sql(sql_script=sql_script, guardar_cambios=True)


def read_categoria(categoria_id: int):
    sql_script = "SELECT * FROM platziblog.categorias where id = " + str(categoria_id)
    respuesta: dict = execute_sql(sql_script=sql_script, guardar_cambios=False)
    return respuesta


def update_categoria(nombre_categoria: str, categoria_id: int):
    sql_script = f"UPDATE categorias set nombre_categoria = '{nombre_categoria}' where id = {categoria_id}"
    execute_sql(sql_script=sql_script, guardar_cambios=True)


def delete_categoria(categoria_id: int):
    sql_script = f"DELETE from categorias where id = {categoria_id}"
    print(sql_script)
    execute_sql(sql_script=sql_script, guardar_cambios=True)


def duplicate_categoria(categoria_id: int):
    """
    Ejemplo para duplicar categorias
    :param categoria_id:
    :return:
    """
    my_categoria = read_categoria(categoria_id=categoria_id)
    texto_categoria = my_categoria[1] + " duplicated"

    create_categoria(nombre_categoria=texto_categoria)


if __name__ == '__main__':
    delete_categoria(categoria_id=22)
