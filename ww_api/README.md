This project is made with python Python 3.10.12 (fastApi 0.115.6)
### Start project in your local
- 1- Create your venv (inside configure_product):
<code>python3 -m venv .env_ww</code>
- 2- Enable your .env_ww:
<code>source .env_ww/bin/activate</code>
- 3- Install requiered package:
<code>pip install --no-cache-dir -r requirements.txt</code>
- 4- Start uvicorn server:
<code>uvicorn main:app --port PORT  --reload</code>
- 5- Run unit pytest:
<code>python -m pytest</code>
- 6- Swagger docs is available in your local : http://127.0.0.1:8000/docs (replace 8000 with uvicorn port)

### Start project in docker containter
- 1- Need to have docker already installed
- 2- Build your docker image:
<code>docker build -t ww_api .</code>
- 3- Run your docker container:
<code>docker run -d --name ww_api -p 8000:8000 ww_api</code>