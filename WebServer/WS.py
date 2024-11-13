from http.server import SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from CodeManager.env import env
from CodeManager.funcsManager import getPage, ConditionPath
from WebServer.classes.RenderClass import Render as Rr, render_main, render_other, render_auth


class WebServerClass(SimpleHTTPRequestHandler):

    def do_GET(self):
        """Получение и обработка данных, сайтов, путей, стилей, и другого что получает запрос GET"""

        # Парсинг URL и извлечение параметров
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)
        self.dataArray = []
        # Например, получение параметра 'user'
        testData = query_params.get('user', [''])[0]
        self.dataArray.append(testData)

        if ConditionPath(self.path, 'main'):
            self.mainPage = render_main(getPage(env, 1), self.send_response, self.send_header, self.end_headers, self.wfile, self.path)

        elif ConditionPath(self.path, 'about'):
            self.aboutPage = render_other(getPage(env, 2), self.send_response, self.send_header, self.end_headers, self.wfile, self.path)

        elif ConditionPath(self.path, 'auth'):
            self.authPage = render_auth(getPage(env, 3), self.send_response, self.send_header, self.end_headers, self.wfile, self.path)

        elif ConditionPath(self.path, 'new_template'):
            self.NewTemplatePage = render_other(getPage(env, 4), self.send_response, self.send_header, self.end_headers, self.wfile, self.dataArray)

        else:
            super().do_GET()
