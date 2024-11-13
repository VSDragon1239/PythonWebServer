import webbrowser
from http.server import HTTPServer

from CodeManager.pathManager import ArrayPages, dataFolder, typeData, ArrayPaths


def run_server(WebServerClass):
    httpd = HTTPServer(('', 8000), WebServerClass)
    httpd.serve_forever()  # Бесконечная обработка (цикл работы)
    print('= = Server started = =')


def open_browser():
    # Открывает браузер с URL 'http://localhost:8000'
    webbrowser.open('http://localhost:8000')


def getPage(env, idPage):
    page = env.get_template(ArrayPages[idPage])
    return [page, ArrayPages[idPage]]


def getData(file_name):
    return dataFolder + file_name + typeData


def ConditionPath(path, type):
    """Отвечает за условие, при котором путь = страница"""
    if type == 'main':
        if path == ArrayPaths[1]:
            return True
        else:
            return False
    elif type == 'about':
        if path == ArrayPaths[2][1] or path == ArrayPaths[2][2]:
            return True
        else:
            return False
    elif type == 'auth':
        if path == ArrayPaths[3][1] or path == ArrayPaths[3][2] or path == ArrayPaths[3][3]:
            return True
        else:
            return False
    elif type == 'new_template':
        if path == ArrayPaths[4][1] or path == ArrayPaths[4][2]:
            return True
        else:
            return False

    else:
        return False
