import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    
    def GET(self, id_clientes, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_clientes) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/clientes') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_clientes, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_clientes) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/clientes') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    

    
        
    

    @staticmethod
    def GET_EDIT(id_clientes, **k):
        message = None # Error message
        id_clientes = config.check_secure_val(str(id_clientes)) # HMAC id_clientes validate
        result = config.model.get_clientes(int(id_clientes)) # search for the id_clientes
        result.id_clientes = config.make_secure_val(str(result.id_clientes)) # apply HMAC for id_clientes
        return config.render.edit(result, message) # render clientes edit.html

    @staticmethod
    def POST_EDIT(id_clientes, **k):
        form = config.web.input()  # get form data
        form['id_clientes'] = config.check_secure_val(str(form['id_clientes'])) # HMAC id_clientes validate
        # edit user with new data
        result = config.model.edit_clientes(
            form['id_clientes'],form['nombre'],form['rfc'],form['direccion'],form['telefono'],
        )
        if result == None: # Error on udpate data
            id_clientes = config.check_secure_val(str(id_clientes)) # validate HMAC id_clientes
            result = config.model.get_clientes(int(id_clientes)) # search for id_clientes data
            result.id_clientes = config.make_secure_val(str(result.id_clientes)) # apply HMAC to id_clientes
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/clientes') # render clientes index.html
