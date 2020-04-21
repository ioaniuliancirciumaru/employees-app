import connection

def data():
    query = 'SELECT * FROM data ORDER BY id'
    return connection.execute_select(query)

def insert(name, email, phone):
    try:
        query = "INSERT INTO data (name, email, phone) VALUES ('{name}','{email}','{phone}')".format(name=name,email=email,phone=phone)
        connection.execute_select(query)
    except:
        return True

def get_by_id(id):
    query = "SELECT * FROM data WHERE id = '{id}'".format(id=id)
    return connection.execute_select(query)

def edit(id, name, email, phone):
    try:
        query = "UPDATE data SET name='{name}',email='{email}',phone='{phone}' WHERE id='{id}'".format(name=name,email=email,phone=phone,id=id)
        connection.execute_select(query)
    except:
        return True

def delete_user(id):
    query = "DELETE FROM data WHERE id = '{id}'".format(id=id)
    connection.execute_dml_statement(query)