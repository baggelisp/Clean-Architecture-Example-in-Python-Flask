# Clean-Architecture-Example-in-Python-Flask

## Running:
export PORT=5000 <br />
python3 app.py <br />

## Running on docker-compose:
docker-compose up

## Entities:

- User
- Post
- Comment

## Example Requests

GET http://0.0.0.0:5000/users <br />
GET http://0.0.0.0:5000/user/2 <br />
GET http://0.0.0.0:5000/post/2 <br />
GET http://0.0.0.0:5000/post-comments/2 <br />

## Image

![](clean.png)
