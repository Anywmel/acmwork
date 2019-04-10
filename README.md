#### acmwork
```
cd acmwork
pip install -r requirements.txt
python manage.py runserver

cd acmwork
celery -A acmwork worker -l info -P eventlet
```
#### acmwork-front
```
cd acmwork-front
npm install
npm run dev
```