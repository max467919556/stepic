def app(environ, start_response):
    status = "200 OK"
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    body = ""
    query_list = environ["QUERY_STRING"].split("&")
    for item in query_list:
        body += "{}\n".format(item)
    return [ body.encode() ]
