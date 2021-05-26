# capstone1
## Before Start 
this capstone project need two API,WordsAPI and Google Translate
you can get free API_KEY by register on the following webside 
* https://rapidapi.com/datascraper/api/google-translate20 or [Click Here](https://rapidapi.com/datascraper/api/google-translate20)
* https://rapidapi.com/dpventures/api/wordsapi or [Click Here](https://rapidapi.com/dpventures/api/wordsapi)

after you have you API_KEYs ready at root directery create a file call API_KEY.py 
inside the API_KEY.py create two variable,"NewsApi_key" and "Google_Translate_API"
file should looks similar to this:
```python
NewsApi_key='API_KEY'
Google_Translate_API = 'API_KEY'
```

## Update for Heroku 
because this app is been polishing on the heroku there some step need to be consider 
* I comment out the code on file helper.py line 4 
* add new variables on helper.py line 6-7
```python
4 # from API_KEY import NewsApi_key,Google_Translate_API

6 NewsApi_key = os.environ.get("NewsAPI")
7 Google_Translate_API=os.environ.get("GoogleAPI")
```
if you run in the local machine you need to commend it back and commend out 
the code on line 6-7
```python
4 from API_KEY import NewsApi_key,Google_Translate_API

6 # NewsApi_key = os.environ.get("NewsAPI")
7 # Google_Translate_API=os.environ.get("GoogleAPI")
```

### Create Database 
on you machine create a database call "gogo_app_db" with SQLALCHEMY 
and the app database configuaretion is like this:
```python
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///gogo_app_db'
```
you dont have do anything with it,it just a reference that i already did
you just need to create a database call "gogo_app_db"

### Run requirements.text file 
create a virtual environment folder,you can create whatever folder name you want 
```python
python -m venv venv
```
run the following command to install all the dependencies in virtual environment
```python
pip install -r requirements.txt
```
making sure FLASK_ENV is set to development by set up the configuration
```python
export FLASK_ENV=development
```

## Start APP 
### Start app 
to start the app,inside you terminal virtual enviroment,runs the command "flask run"
```python
flask run
```
and copy the paste the url on termial to you bowser 
```python
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 000-000-000
```

## Polishing on Heroku 
I'm already polishing my capstone app on heroku 
click here to view:
[gogo_app](https://capstoneshumin.herokuapp.com)


### About GoGo App(Capstone1)
Build this app to help to improve English Level,you will able to add and practice vocabulary,study grammar you have learns
making daily,weekly and monthly plan.

## Section of the app
### Vocabulary
Allow to add any Vocabulary,store its definition in both English and Chinese into database

### Reading
Allow to read any articles online to improve reading level 
           
### Grammar
Allow to add any Grammar skill have learned

### Review Vol
Allow to practice Vocabulary 
      
### Translate
Allow to translate any sentence into any language

### Study Plan
Allow add daily,weekly,or monthly plan
