def  application  ( environ ,  start_response ):

    QUERY_STRING = '/?a=1&a=2&b=3'

    response_body = [(i + '\n') for i in environ['QUERY_STRING'].split('&')]
	
   
    status  =  '200 OK'

    # Теперь тип содержимого - text / html 
    response_headers  =  [ 
        ( 'Content-Type' ,  'text / html' ), 
        ( 'Content-Length' ,  str ( len ( response_body ))) 
    ]

    start_response ( status ,  response_headers ) 
    return  [response_body]
