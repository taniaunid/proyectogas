import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    
    def GET(self, id_clientes):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(id_clientes) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/clientes') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(id_clientes):
        id_clientes = config.check_secure_val(str(id_clientes)) # HMAC id_clientes validate
        result = config.model.get_clientes(id_clientes) # search for the id_clientes data
        return config.render.view(result) # render view.html with id_clientes data
