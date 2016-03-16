def application(environ, start_response):
    lines = []
    qs = environ['QUERY_STRING']
    get_params = qs.split('&')
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    return  ["\n".join(get_params)]
