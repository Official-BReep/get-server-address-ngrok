import ngrok

# construct the api client
client = ngrok.Client("API-KEY")

# list all online tunnels
for t in client.tunnels.list():
    host, port = t.public_url[6:]
