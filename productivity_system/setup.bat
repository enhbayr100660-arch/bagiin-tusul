@echo off
echo === Productivity System setup ===
if not exist .env copy .env.example .env
echo.
echo .env file dotor DB_PASSWORD-oo bichij hadgalaad, daraa n ENTER darna uu.
notepad .env
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations core
python manage.py migrate
python manage.py seed
python manage.py report
echo.
echo Duuslaa. Dashboard: streamlit run dashboard/app.py
pause
