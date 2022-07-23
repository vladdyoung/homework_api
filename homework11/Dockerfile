FROM python
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD pytest --browser_name=remote --url=http://10.234.28.102:8081/ --browser=chrome --executor=10.234.28.102 --version_browser=102.0