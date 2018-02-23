import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    
    def GET(self, id_productos, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_productos) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/productos') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_productos, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_productos) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/productos') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    

    
    

    @staticmethod
    def GET_DELETE(id_productos, **k):
        message = None # Error message
        id_productos = config.check_secure_val(str(id_productos)) # HMAC id_productos validate
        result = config.model.get_productos(int(id_productos)) # search  id_productos
        result.id_productos = config.make_secure_val(str(result.id_productos)) # apply HMAC for id_productos
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(id_productos, **k):
        form = config.web.input() # get form data
        form['id_productos'] = config.check_secure_val(str(form['id_productos'])) # HMAC id_productos validate
        result = config.model.delete_productos(form['id_productos']) # get productos data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_productos = config.check_secure_val(str(id_productos))  # HMAC user validate
            id_productos = config.check_secure_val(str(id_productos))  # HMAC user validate
            result = config.model.get_productos(int(id_productos)) # get id_productos data
            result.id_productos = config.make_secure_val(str(result.id_productos)) # apply HMAC to id_productos
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/productos') # render productos delete.html 
