# -*- coding: utf-8 -*-
"""resumidor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/jss-or/resumidor_pruebas/blob/main/resumidor.ipynb
"""

!pip install Flask

!pip install Summa

!pip install flask-restful

from flask import Flask, request, render_template

from flask_restful import Resource, Api

from summa.summarizer import summarize

app = Flask(__name__)
api = Api(app)
@app.route("/")
def ny_form():
  return render_template("summarizer.html")

@app.route("/", methods = ["POST"])
def my_form_post():
  text = request.form["text"]
  text = summarize(text, language = "spanish", ratio = 0.2)
  return(text)

class Return_summary(Resource):
  def get(self, content):
    resumen = summarize(content, language = "spanish", ratio = 0.2)
    return resumen

api.add_resource(Return_summary, "/return_summary/<string:content>")
if __name__ == "__main__":
  app.run(debug = True)