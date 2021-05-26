from werkzeug.utils import send_file
from app import app 
from unittest import TestCase 
from flask import session, sessions 

app.config["TESTING"] = True 
app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]

class FlaskAppTestCase(TestCase):
    
    def test_home(self):
        with app.test_client() as client:
            res = client.get("/",follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code,200)
            self.assertIn("<title>GoGo app</title>",html)

    
