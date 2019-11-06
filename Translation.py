import requests,json
def TranslateText(Text,Language):
    try:
        LanguageCodes={"azerbaijan":"az","albanian":"sq","amharic":"am","english":"en",
                       "arabic":"ar","armenian":"hy","afrikaans":"af","basque":"eu",
                       "bashkir":"ba","belarusian":"be","bengali":"bn","burmese":"my",
                       "bulgarian":"bg","bosnian":"bs","welsh":"cy","hungarian":"hu",
                       "vietnamese":"vi","haitian":"ht","creole":"ht","galician":"gl",
                       "dutch":"nl","hill mari":"mrj","greek":"el","georgian":"ka",
                       "gujarati":"gu","danish":"da","hebrew":"he","yiddish":"yi",
                       "indonesian":"id","irish":"ga","italian":"it","icelandic":"is",
                       "spanish":"es","kazakh":"kk","kannada":"kn","catalan":"ca",
                       "kyrgyz":"ky","chinese":"zh","korean":"ko","xhosa":"xh",
                       "Khmer":"km","laotian":"lo","latin":"la","latvian":"lv",
                       "lithuanian":"lt","luxembourgish":"lb","malagasy":"mg",
                       "malay":"ms","malayalam":"ml","maltese":"mt","macedonian":"mk",
                       "maori":"mi","marathi":"mr","mari":"mhr","mongolian":"mn",
                       "german":"de","nepali":"ne","norwegian":"no","punjabi":"pa",
                       "papiamento":"pap","persian":"fa","polish":"pl","portuguese":"pt",
                       "romanian":"ro","russian":"ru","cebuano":"ceb","serbian":"sr",
                       "sinhala":"si","slovakian":"sk","slovenian":"sl","swahili":"sw",
                       "sundanese":"su","tajik":"tg","thai":"th","tagalog":"tl",
                       "tamil":"ta","tatar":"tt","telugu":"te","turkish":"tr",
                       "udmurt":"udm","uzbek":"uz","ukrainian":"uk","urdu":"ur",
                       "finnish":"fi","french":"fr","hindi":"hi","croatian":"hr",
                       "czech":"cs","swedish":"sv","scottish":"gd","estonian":"et",
                       "esperanto":"eo","javanese":"jv","japanese":"ja"}
        Key="trnsl.1.1.20191105T220926Z.e747b96073e3c078.eaa300fca7f8ec15dbe6b87c84bc08925108275c"
        Parameters={"lang":LanguageCodes[Language.lower()],"key":Key,"text":Text,"format":"plain"}
        Request=requests.get("https://translate.yandex.net/api/v1.5/tr.json/translate",params=Parameters)
        JsonData=Request.json()
        return JsonData["text"][0]
    except:
        return "Unknown Error Translating. Please check formatting of inputs."