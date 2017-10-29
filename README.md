# J.A.S.P.R.
#### Alessandro Cartegni, Jasper  Cheung, Jawadul Kadir, Naotaka Kinoshita, Anish Shenoy <br> SoftDev1 Pd 7 <br>P #00 - Da Art of Storytellin'

A collaborative storytelling game/website. 

**Running program** <br>
First, ensure that the dependencies listed below are installed. If you have installed `flask` through `pip` in a virtualenv, make sure that your virtual environment is running when you run the program. After cloning our files from github, the only file you need to run is `app.py`. `app.py` will automatically initialize the needed databases in `data/` using `__init__.py` and `db.py` found in `util/`. <br>
The file structure should be: <br>
```
app.py
data/
util/
 |  db.py
 |  __init.py__
templates/
 |  account.html
 |  base.html
 |  login.html
 |  story.html
 |  create.html
 |  edit.html
 |  home.html
design.pdf
devlog.txt
changes.txt
README.md
```
<br>
After running app.py, you can now go to localhost:5000 in your web browser, and the site should be accessible. 
<br><br>

**Dependencies**
<ul>
  <li>
    
  `from flask: Flask, render_template, redirect, url_for, request, session`
  </li>
  <li>
  
  `python3`
  </li>
  <li>
  
  `sqlite3`
  </li>
  <li>
  
  `os`
  </li>
  <li>
  
  `from os.path: isfile`
  </li>
  <li>
  
  `hashlib`
  </li>
