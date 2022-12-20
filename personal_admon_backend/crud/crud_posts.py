
from personal_admon_backend.crud.crud_util import execute_sql


def create_post(post: dict):
    sql_script = """
        INSERT INTO posts (titulo, fecha_publicacion, contenido, estatus, usuario_id, categoria_id) 
        VALUES ('{titulo}','{fecha_publicacion}','{contenido}','{estatus}', '{usuario_id}', '{categoria_id}')
    """.format(
        titulo=post["titulo"],
        fecha_publicacion=post["fecha_publicacion"],
        contenido=post["contenido"],
        estatus=post["estatus"],
        usuario_id=post["usuario_id"],
        categoria_id=post["categoria_id"],
    )

    execute_sql(sql_script=sql_script, guardar_cambios=True)


def read_post(post_id: int) -> dict:
    sql_script = "SELECT * FROM platziblog.posts WHERE id=" + str(post_id)
    respuesta: dict = execute_sql(sql_script=sql_script, guardar_cambios=False)
    return respuesta


def update_post(post: dict):
    sql_script = """
    UPDATE posts  
    SET titulo= '{titulo}', fecha_publicacion= '{fecha_publicacion}', contenido= '{contenido}', estatus= '{estatus}', usuario_id= '{usuario_id}', categoria_id= '{categoria_id}'  
    WHERE id={id}
    """.format(
        **post
    )
    execute_sql(sql_script=sql_script, guardar_cambios=True)


def delete_post(post_id: str):
    sql_script = f"DELETE from posts where id = {post_id}"
    execute_sql(sql_script=sql_script, guardar_cambios=True)


if __name__ == '__main__':
    my_dict={
        "id": "28",
        "titulo": "Epa colombia",
        "fecha_publicacion": "22-09-10",
        "contenido": "epacolomniaggsnjdjduifhrbfhsfjkfhbdhfgerugu",
        "estatus": "activo",
        "usuario_id": "1",
        "categoria_id": "1"
    }
    update_post(post=my_dict)
