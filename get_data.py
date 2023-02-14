from pyngrok import ngrok

ngrok.set_auth_token("AUTH-TOKEN HERE")
api = ngrok.get_ngrok_process().api_url #get api_url
response = ngrok.api_request("{}/api/tunnels".format(str(api).replace("4041", "4040") if "4041" in api else str(api)),  #replace to fix error if ngrok is running
                             params={"tunnel_name": "foo"})
try:
    data = response['tunnels'][0] #get data from response
    host, port = str(data['public_url'][6:]).split(":") #get server ip and server port
except:
    pass
