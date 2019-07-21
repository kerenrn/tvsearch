import os
from bottle import (get, post, redirect, request, route, run, static_file,
                    template)
import json                    
from utils import getVersion, getShowsData, search

# Static Routes

@get("/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="./js")

@get("/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="./css")

@get("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="./images")

@route('/')
def index():
    sectionTemplate = "./templates/home.tpl"
    return template("./pages/index.html", version=getVersion(), sectionTemplate=sectionTemplate, sectionData = {})

@route('/browse')
def browse():
    sectionTemplate = "./templates/browse.tpl"
    return template("./pages/index.html", version=getVersion(), sectionTemplate=sectionTemplate, sectionData = getShowsData())

@route('/search')
def search():
    sectionTemplate = "./templates/search.tpl"
    return template("./pages/index.html", version=getVersion(), sectionTemplate=sectionTemplate, sectionData = {})

@post('/search')
def search():
    sectionTemplate = "./templates/seaerch_result.tpl"
    query = request.forms.get('q')
    return template("./pages/index.html", version=getVersion(), sectionData={}, sectionTemplate=sectionTemplate, query=query, results=search(query))

if __name__ == "__main__":
    run(host='localhost', port=os.environ.get('PORT', 5000), reloader=True, debuger=True)
