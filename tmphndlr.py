from flask import request,make_response,render_template
class Template_Handler:
  def __init__(self,app):
    @app.route("/u/<name>")
    def index(name):
      return render_template("index2.html",user=name)
    @app.route("/")
    def main():
      return render_template("main.html")
    @app.route("/<article>")
    def evrelse(article):
      return render_template("main.html",content=article)