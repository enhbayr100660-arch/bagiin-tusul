@echo off
echo === GitHub push ===
echo Umnu n GitHub deer HOOSON repo uusgesen baih heregtei.
set /p URL=GitHub repo URL (jishee https://github.com/name/repo.git): 
if not exist .git git init
git add .
git commit -m "Week 1: database, models, seed, collector, dashboard"
git branch -M main
git remote remove origin 2>nul
git remote add origin %URL%
git push -u origin main
pause
