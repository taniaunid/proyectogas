import web
import config

db = config.db


def get_all_productos():
    try:
        return db.select('productos')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_productos(id_productos):
    try:
        return db.select('productos', where='id_productos=$id_productos', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_productos(id_productos):
    try:
        return db.delete('productos', where='id_productos=$id_productos', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_productos(nombre,litros,precio):
    try:
        return db.insert('productos',nombre=nombre,
litros=litros,
precio=precio)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_productos(id_productos,nombre,litros,precio):
    try:
        return db.update('productos',id_productos=id_productos,
nombre=nombre,
litros=litros,
precio=precio,
                  where='id_productos=$id_productos',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
