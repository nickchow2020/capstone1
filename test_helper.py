from logging import getLevelName
from warnings import resetwarnings
from werkzeug.utils import send_file
from app import reading
from requests.models import Response
from helper import language_tuple_list,get_reading_material,translateEnTo,getEnglishDef,getChineseDef
from helper import newsapi,translate_url
from unittest import TestCase


class GoogleTranslateTestCase(TestCase):

    def test_make_object_tuple(self):
        obj = {
            "name":"shumin",
            "age":28
        }

        obj1 = {
            "name":"",
            "age":28
        }

        obj2 = {
            "name":"",
            "age": -28
        }

        self.assertEqual(language_tuple_list(obj),[("name","shumin"),("age",28)])
        self.assertEqual(language_tuple_list(obj2),[("name",""),("age",-28)])
        self.assertEqual(language_tuple_list(obj1),[("name",""),("age",28)])

    def test_translate(self):
        result = translateEnTo("hello","zh-CN",translate_url)
        result1 = translateEnTo("world","zh-CN",translate_url)
        self.assertEqual(result,"你好")
        self.assertEqual(result1,"世界")


    def test_word_translate(self):
        response = getChineseDef("hello",translate_url)
        response1 = getChineseDef("world",translate_url)
        self.assertEqual(response,"你好")
        self.assertEqual(response1,"世界")

class TestingEnglishDefintionTestCase(TestCase):
    def test_definition(self):  
        response = getEnglishDef("hello")
        self.assertEqual(response["definition"],"an expression of greeting")
        self.assertEqual(response["partOfSpeech"],"noun")


class NewApiTestCase(TestCase):
    def test_response_reading(self):
        response1 = get_reading_material("en")
        response2 = get_reading_material("zh")
        self.assertEqual(response1[0]["language"],"en")
        self.assertEqual(response2[0]["language"],"zh")
        self.assertRaises(ValueError,get_reading_material,"ss")






