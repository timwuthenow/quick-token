# Quick Service Setup

```sh
pip3 install pyjwt
pip3 install jwt
python service.py
```

After installing the service, run the following command to generate a Bearer Token:

```sh
curl -X POST -H "Content-Type: application/json" -d '{"username": "your_username", "password": "your_password"}' http://127.0.0.1:5020/get_token
```

After running this you should receive a token, e.g. the result below:

```json
{
  "token": "c6d87cfc-9048-40cb-8f7d-9b6bd721de04"
}
```

After this you can validate if the token works by accessing the following endpoint via `curl`:

```sh
curl -H "Authorization: Bearer c6d87cfc-9048-40cb-8f7d-9b6bd721de04" http://localhost:5020/protected
```

```json
{
  "message": "Hello, your_username! This is a protected resource."
}```
