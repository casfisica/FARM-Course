# FARM-Course
Python FastAPI, React, and MongoDB (FARM)
```bash
PYTHONVERSION=$(python3 --version)
python3 -m virtualenv venv
source ./venv/bin/activate
pip install fastapi uvicorn pymongo
pip freeze > requirements.txt
```

## To run the app
```bash
uvicorn index:app --reload
```

## To start and stop MongoDB services:
To have launchd start mongod immediately and also restart at login, use:
```bash

brew services start mongodb-community
```

If you manage mongod as a service it will use the default paths listed above. To stop the server instance use:

```bash
brew services stop mongodb-community
```