# Clean-Architecture-Example-in-Python-Flask

To Run: <br />
export PORT=5000 <br />
python3 app.py <br />

Running with docker-compose: <br />
docker-compose up <br />

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
