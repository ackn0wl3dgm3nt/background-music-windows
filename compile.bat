@echo off

if "%1" == "main" (
pyinstaller main.py --onefile --noconsole --name background_music
del background_music.spec
)

if "%1" == "control" (
pyinstaller control.py --onefile --noconsole  --name control
del control.spec
)

rmdir /s /q build
rmdir /s /q __pycache__
