# Clean-Architecture-Example-in-Python-Flask

To Run:
source env/bin/activate
python app.py

Add env variable:
source env/bin/activate
export APP_SETTINGS="config.DevelopmentConfig"

Get Env Variable

app.config.from_object(os.environ['APP_SETTINGS'])
print(os.environ['APP_SETTINGS'])

