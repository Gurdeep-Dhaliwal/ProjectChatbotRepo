keywordsList = list()
globalInput = ""

"""
currenciesList = ["dollar", "krona", "peso", "krone", "forint", "koruna", "pound", "leu", "krona",
                   "rupiah", "rupee", "real", "ruble", "kuna", "yen", "baht", "franc", "euro", "ringgit", "lev",
                   "lira", "yuan", "rand", "shekel", "won", "zloty", "dollars", "kronas", "pesos", "krones", "forints", "korunas", "pounds", "leus", "kronas",
                   "rupiahs", "rupees", "reals", "rubles", "kunas", "yens", "bahts", "francs", "euros", "ringgits", "levs",
                   "liras", "yuans", "rands", "shekels", "wons", "zlotys", "CAD", "HKD", "ISK", "PHP", "DKK", "HUF", "CZK", "GBP", "RON", "SEK", "IDR", "INR", "BRL", "RUB", "HRK", "JPY", "THB", "CHF",
                    "EUR", "MYR", "BGN", "TRY", "CNY", "NOK", "NZD", "ZAR", "USD", "MXN", "SGD", "AUD", "ILS", "KRW", "PLN", "canadian dollar",
                    "hong kong dollar", "icelandic krona", "philipine peso", "danish krone", "hungarian froint", "czech republic koruna", "british pound", "romanian leu", "swedish krona", "indonesian rupiah",
                  "indian rupee", "brazilian real", "russian ruble", "croatian kuna", "japanese yen", "thai baht", "swiss franc", "malaysian ringgit", "bulgarian lev", "turkish lyra", "chinese yuan",
                  "norwegian krone", "new zealand dollar", "south african rand", "united states dollar", "mexican peso", "singapore dollar", "australian dollar", "israeli new shekel", "south korean won", "poland zloty",
                  "canadian dollars", "hong kong dollars", "icelandic kronas", "philipine pesos", "danish krones", "hungarian froints", "czech republic korunas", "british pounds", "romanian leus", "swedish kronas", "indonesian rupiahs",
                  "indian rupees", "brazilian reals", "russian rubles", "croatian kunas", "japanese yens", "thai bahts", "swiss francs", "malaysian ringgits", "bulgarian levs", "turkish lyras", "chinese yuans",
                  "norwegian krones", "new zealand dollars", "south african rands", "united states dollars", "mexican pesos", "singapore dollars", "australian dollars", "israeli new shekels", "south korean wons", "poland zloty"]
"""


currencyCodes = ["CAD", "HKD", "ISK", "PHP", "DKK", "HUF", "CZK", "GBP", "RON", "SEK", "IDR", "INR", "BRL", "RUB", "HRK", "JPY", "THB", "CHF",
                    "EUR", "MYR", "BGN", "TRY", "CNY", "NOK", "NZD", "ZAR", "USD", "MXN", "SGD", "AUD", "ILS", "KRW", "PLN"]


currenciesList = ["CAD", "canadian", "canada", "canadian dollar",
                  "HKD", "hong", "kong", "hong kong dollar",
                  "ISK", "icelandic", "iceland", "icelandic krona",
                  "PHP", "philippines", "philippine", "philippine peso",
                  "DKK", "denmark", "danish", "dansih krone",
                  "HUF", "hungarian", "hungary", "forint", "forints", "hungarian forint",
                  "CZK", "czech", "koruna", "korunas", "czech koruna",
                  "GBP", "british", "britain", "uk", "england", "scotland", "wales", "pound", "pounds", "great british pound",
                  "RON", "romanian", "romania", "leu", "leus", "romanian leu",]


currencyCodesDict = {
    "CAD": ("canadian", "canada", "canadian dollar"),
    "HKD": ("hong", "kong", "hong kong dollar"),
    "ISK": ("icelandic", "iceland", "icelandic krona"),
    "PHP": ("philippines", "philippine", "philippine peso"),
    "DKK": ("denmark", "danish", "dansih krone"),
    "HUF": ("hungarian", "hungary", "forint", "forints", "hungarian forint"),
    "CZK": ("czech", "koruna", "korunas", "czech koruna"),
    "GBP": ("british", "britain", "uk", "england", "scotland", "wales", "pound", "pounds", "great british pound"),
    "RON": ("romanian", "romania", "leu", "leus", "romanian leu"),
    "SEK": ("swedish", "sweden", "krona", "kronas", "swedish krona"),
    "IDR": ("indonesia", "indonesian", "rupiah", "rupiahs", "indonesian rupiah"),
    "INR": ("india", "indian", "rupee", "rupees", "indian rupee"),
    "BRL": ("brazil", "brazilian", "real", "reals", "reais", "brazilian real"),
    "RUB": ("russia", "russian", "ruble", "rubles", "russian ruble"),
    "HRK": ("croatian", "croatia", "kuna", "kunas", "croatian kuna"),
    "JPY": ("japan", "japanese", "yen", "yens", "japanese yen"),
    "THB": ("thai", "thailand", "baht", "bahts", "thai baht"),
    "CHF": ("swiss", "switzerland", "franc", "francs", "swiss franc"),
    "EUR": ("europe", "eu", "euros", "euro"),
    "MYR": ("malaysia", "malaysia", "ringgit", "ringgits", "malasian ringgit"),
    "BGN": ("bulgaria", "bulgarian", "lev", "levs", "bulgarian lev"),
    "TRY": ("turkey", "turkish", "lira", "liras", "turkish lira"),
    "CNY": ("china", "chinese", "yuan", "yuans", "chinese yuan"),
    "NOK": ("norway", "norwegian", "krone", "krones", "norwegian krone"),
    "NZD": ("zealand", "new zealand dollar"),
    "ZAR": ("africa", "african", "rand", "south african rand"),
    "USD": ("states", "america", "american", "dollar", "dollars", "united states dollar"),
    "MXN": ("mexico", "mexican", "peso", "pesos", "mexican peso"),
    "SGD": ("singapore", "singapore dollar"),
    "AUD": ("australia", "australian", "australian dollar"),
    "ILS": ("israel", "israeli", "shekel", "shekels", "israeli shekel"),
    "KRW": ("south", "korean", "won", "wons", "korean won"),
    "PLN": ("poland", "polish", "zloty", "zlotys", "polish zloty")
}