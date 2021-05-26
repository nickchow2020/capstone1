from newsapi import NewsApiClient
from API_KEY import NewsApi_key,Google_Translate_API
import requests

newsapi = NewsApiClient(api_key=NewsApi_key)
translate_url = "https://google-translate20.p.rapidapi.com/translate"



languages = {
        "auto":"Detect Language",
        "af":"Afrikaans",
        "sq":"Albanian",
        "am":"Amharic",
        "ar":"Arabic",
        "hy":"Armenian",
        "az":"Azerbaijani",
        "eu":"Basque",
        "be":"Belarusian",
        "bn":"Bengali",
        "bs":"Bosnian",
        "bg":"Bulgarian",
        "ca":"Catalan",
        "ceb":"Cebuano",
        "ny":"Chichewa",
        "zh-CN":"Chinese (Simplified)",
        "zh-TW":"Chinese (Traditional)",
        "co":"Corsican",
        "hr":"Croatian",
        "cs":"Czech",
        "da":"Danish",
        "nl":"Dutch",
        "en":"English",
        "eo":"Esperanto",
        "et":"Estonian",
        "tl":"Filipino",
        "fi":"Finnish",
        "fr":"French",
        "fy":"Frisian",
        "gl":"Galician",
        "ka":"Georgian",
        "de":"German",
        "el":"Greek",
        "gu":"Gujarati",
        "ht":"Haitian Creole",
        "ha":"Hausa",
        "haw":"Hawaiian",
        "he":"Hebrew",
        "iw":"Hebrew",
        "hi":"Hindi",
        "hmn":"Hmong",
        "hu":"Hungarian",
        "is":"Icelandic",
        "ig":"Igbo",
        "id":"Indonesian",
        "ga":"Irish",
        "it":"Italian",
        "ja":"Japanese",
        "jw":"Javanese",
        "kn":"Kannada",
        "kk":"Kazakh",
        "km":"Khmer",
        "rw":"Kinyarwanda",
        "ko":"Korean",
        "ku":"Kurdish (Kurmanji)",
        "ky":"Kyrgyz",
        "lo":"Lao",
        "la":"Latin",
        "lv":"Latvian",
        "lt":"Lithuanian",
        "lb":"Luxembourgish",
        "mk":"Macedonian",
        "mg":"Malagasy",
        "ms":"Malay",
        "ml":"Malayalam",
        "mt":"Maltese",
        "mi":"Maori",
        "mr":"Marathi",
        "mn":"Mongolian",
        "my":"Myanmar (Burmese)",
        "ne":"Nepali",
        "no":"Norwegian",
        "or":"Odia (Oriya)",
        "ps":"Pashto",
        "fa":"Persian",
        "pl":"Polish",
        "pt":"Portuguese",
        "pa":"Punjabi",
        "ro":"Romanian",
        "ru":"Russian",
        "sm":"Samoan",
        "gd":"Scots Gaelic",
        "sr":"Serbian",
        "st":"Sesotho",
        "sn":"Shona",
        "sd":"Sindhi",
        "si":"Sinhala",
        "sk":"Slovak",
        "sl":"Slovenian",
        "so":"Somali",
        "es":"Spanish",
        "su":"Sundanese",
        "sw":"Swahili",
        "sv":"Swedish",
        "tg":"Tajik",
        "ta":"Tamil",
        "tt":"Tatar",
        "te":"Telugu",
        "th":"Thai",
        "tr":"Turkish",
        "uk":"Ukrainian",
        "ur":"Urdu",
        "ug":"Uyghur",
        "uz":"Uzbek",
        "vi":"Vietnamese",
        "cy":"Welsh",
        "xh":"Xhosa",
        "yi":"Yiddish",
        "yo":"Yoruba",
        "zu":"Zulu"
    }



def language_tuple_list(obj):
    return list(obj.items())



def get_reading_material(lang,cate=False):
    if cate:
        data = newsapi.get_sources(
            language=lang,
            category=cate)
        return data["sources"]
    else:
        data = newsapi.get_sources(
            language=lang)
        return data["sources"]



def translateEnTo(content,lang,url):
        querystring = {
                "text":content,
                "tl":lang,
                "sl":"en"
                }

        headers = {
                'x-rapidapi-key': Google_Translate_API,
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()["data"]["translation"]



def getEnglishDef(vol):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{vol}/definitions"
    headers = {
        'x-rapidapi-key':Google_Translate_API
    }
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    return data["definitions"][0]



def getChineseDef(vol,url):
    querystring = {"text":f"{vol}","tl":"zh-CN","sl":"en"}
    headers = {
    'x-rapidapi-key': Google_Translate_API,
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    return data["data"]["translation"]