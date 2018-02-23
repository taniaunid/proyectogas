import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    
    def GET(self, id_productos, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_productos) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/productos') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_productos, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_productos) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/productos') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    

    
        
    

    @staticmethod
    def GET_EDIT(id_productos, **k):
        message = None # Error message
        id_productos = config.check_secure_val(str(id_productos)) # HMAC id_productos validate
        result = config.model.get_productos(int(id_productos)) # search for the id_productos
        result.id_productos = config.make_secure_val(str(result.id_productos)) # apply HMAC for id_productos
        return config.render.edit(result, message) # render productos edit.html

    @staticmethod
    def POST_EDIT(id_productos, **k):
        form = config.web.input()  # get form data
        form['id_productos'] = config.check_secure_val(str(form['id_productos'])) # HMAC id_productos validate
        # edit user with new data
        result = config.model.edit_productos(
            form['id_productos'],form['nombre'],form['litros'],form['precio'],
        )
        if result == None: # Error on udpate data
            id_productos = config.check_secure_val(str(id_productos)) # validate HMAC id_productos
            result = config.model.get_productos(int(id_productos)) # search for id_productos data
            result.id_productos = config.make_secure_val(str(result.id_productos)) # apply HMAC to id_productos
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/productos') # render productos index.html
