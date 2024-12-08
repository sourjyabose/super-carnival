from flask import request,make_response
class Initial:
    def __init__(self,app):
        @app.route('/<int:id>')
        def hello(id):    
            return make_response("",302,{"Location":f"/user/{id}"})
        @app.route("/user/<user>")
        def disp(user):
            prni=request.get_data();
            return f"hello user {request.url} {user}";
        @app.errorhandler(404)
        def err(e):
            return "<center><h1>Page not Found !</h1></center>"
                
        