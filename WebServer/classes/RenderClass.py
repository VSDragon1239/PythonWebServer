from CodeManager.pathManager import jsFolder, cssFolder


def render_main(page, send_response, send_header, end_headers, wfile, path):
    """Возвращает index.html"""
    send_response(200)
    send_header('Content-type', 'text/html')
    end_headers()
    wfile.write(page[0].render(main_js_file_path=jsFolder, main_css_file_path=cssFolder).encode('utf-8'))


def render_auth(page, send_response, send_header, end_headers, wfile, path):
    """Возвращает auth.html"""
    send_response(200)
    send_header('Content-type', 'text/html')
    end_headers()
    wfile.write(page[0].render(authPath=path, main_js_file_path=jsFolder, main_css_file_path=cssFolder).encode('utf-8'))


def render_other(page, send_response, send_header, end_headers, wfile, path):
    """Возвращает index.html"""
    send_response(200)
    send_header('Content-type', 'text/html')
    end_headers()
    wfile.write(page[0].render(main_js_file_path=jsFolder, main_css_file_path=cssFolder).encode('utf-8'))


class Render:
    def __init__(self):
        pass
