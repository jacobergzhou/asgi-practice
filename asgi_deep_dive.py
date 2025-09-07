import json
async def app(scope, receive, send): 
    assert scope['type'] == 'http'

    ### Extract request info
    method = scope['method']
    path = scope['path']
    query_string = scope['query_string'].decode('utf-8')

    params = parse_query_params(query_string)

    body = await read_body(receive)

    ### Route handling
    if path == '/' and method == 'GET':
        await send_response(send, 200, "GET Request Succeed!")
    elif path == '/users' and method == 'GET':
        page = params.get('page', '1')
        limit = params.get('limit', '10')
        await send_json(send, 200, {
            'users': ['Saka', 'Rice', 'Saliba'],
            'page': page,
            'limit': limit
        })
    elif path == '/echo' and method == 'POST':
        await send_response(send, 200, f'You sent: {body.decode()}')
    else:
        await send_response(send, 404, f'Path {path} not found!')

def parse_query_params(query_string): 
    if not query_string:
        return {}
    
    params = {}
    pairs = query_string.split('&')
    for pair in pairs:
        if '=' in pair:
            key, value = pair.split('=')
            params[key] = value
        else:
            # when key have no value: ?debug&verbose
            params[pair] = ''
    return params

async def read_body(receive):
    body = b''
    while True:
        message = await receive()
        if message['type'] == 'http.request':
            body += message.get('body', b'')
            if not message.get('more_body', False): 
                break
        elif message['type'] == 'http.disconnect':
            break
    return body

async def send_response(send, status, text):
    byte_text = text.encode('utf-8')

    await send({
        'type': 'http.response.start',
        'status': status,
        'headers': [[b'content-type', b'text/plain']]
    })

    await send({
        'type': 'http.response.body',
        'body': byte_text
    })

async def send_json(send, status, data):
   json_string = json.dumps(data)
   json_bytes = json_string.encode('utf-8')

   await send({
       'type': 'http.response.start',
       'status': status,
       'headers': [
           [b'content-type', b'application/json'],
           [b'content-length', str(len(json_bytes)).encode()]
        ]
   })

   await send({
       'type': 'http.response.body',
       'body': json_bytes
   })