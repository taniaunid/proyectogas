import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    
    def GET(self, id_clientes, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_clientes) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/clientes') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_clientes, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_clientes) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/clientes') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    

    
    

    @staticmethod
    def GET_DELETE(id_clientes, **k):
        message = None # Error message
        id_clientes = config.check_secure_val(str(id_clientes)) # HMAC id_clientes validate
        result = config.model.get_clientes(int(id_clientes)) # search  id_clientes
        result.id_clientes = config.make_secure_val(str(result.id_clientes)) # apply HMAC for id_clientes
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(id_clientes, **k):
        form = config.web.input() # get form data
        form['id_clientes'] = config.check_secure_val(str(form['id_clientes'])) # HMAC id_clientes validate
        result = config.model.delete_clientes(form['id_clientes']) # get clientes data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_clientes = config.check_secure_val(str(id_clientes))  # HMAC user validate
            id_clientes = config.check_secure_val(str(id_clientes))  # HMAC user validate
            result = config.model.get_clientes(int(id_clientes)) # get id_clientes data
            result.id_clientes = config.make_secure_val(str(result.id_clientes)) # apply HMAC to id_clientes
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/clientes') # render clientes delete.html 
