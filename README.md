# WebFolder
Web interface by Django for file managing

This project developed as test task, you can read description in description.txt

# Setup
1. Clone git content
2. intall libs from requirements.txt
3. edit [settings.py](https://github.com/Nikakto/WebFolder/blob/master/WebFolder/settings.py):
  <br>ROOT_DIR is uppest allowed level of directory. 
  <br>Example: if you want allow to users look only "C:/Games" and subfolders of this, then set ROOT_DIR=”C:/Games”
4. run manage.py
5. open localhost:8000

Console commands:
<br>$ git clone https://github.com/Nikakto/WebFolder/
<br>$ cd WebFodler
<br>$ mkvirtualenv --python=/python3.5folder/python3.5 WebFolder
<br>$ workon WebFodler
<br>$ pip install -r requirements.txt
<br>$ python manage.py runserver
<br>$ xdg-open localhost:8000/

# How use:
Head always contain buttons for choose file and upload at current directory.
Second line is path from root to current place
Left panel is list of folder files and directories
When file choose, riwght pannrl will be visible. This panel allow you remove or download this file.
When you click remove, started dialog for removing this file (yes - remove, no - do nothing. Each answer will return in active directory)

# Note:
You can use direct link for file managing with out web page.
<br>/file/download/path="C:/Games/game.exe" - to start download game.exe
<br>/file/delete/path="C:/Games/game.exe"&confirm=yes - to remove game.exe (with out confirm=yes - return dialog for remove file)
<br>/file/upload/path="C:/Games" - to upload file to "C:/Games". (name of file field should be "file_upload". But it will not work, because need crf token that generate only in web page)
