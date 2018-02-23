import web
import config

db = config.db


def get_all_clientes():
    try:
        return db.select('clientes')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_clientes(id_clientes):
    try:
        return db.select('clientes', where='id_clientes=$id_clientes', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_clientes(id_clientes):
    try:
        return db.delete('clientes', where='id_clientes=$id_clientes', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_clientes(nombre,rfc,direccion,telefono):
    try:
        return db.insert('clientes',nombre=nombre,
rfc=rfc,
direccion=direccion,
telefono=telefono)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_clientes(id_clientes,nombre,rfc,direccion,telefono):
    try:
        return db.update('clientes',id_clientes=id_clientes,
nombre=nombre,
rfc=rfc,
direccion=direccion,
telefono=telefono,
                  where='id_clientes=$id_clientes',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
