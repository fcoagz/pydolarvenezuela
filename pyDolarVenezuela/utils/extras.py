from ..models import Image

currencies = {
    "eur": {"name": "Euro", "id": "euro"},
    "cny": {"name": "Yuan chino", "id": "yuan"},
    "try": {"name": "Lira turca", "id": "lira"},
    "rub": {"name": "Rublo ruso", "id": "rublo"},
    "usd": {"name": "Dólar estadounidense", "id": "dolar"}
}

code_currencies = {
    'USD': 'Dólar estadounidense',
    'DKK': 'Corona danesa',
    'COP': 'Peso colombiano',
    'NOK': 'Corona noruega',
    'GBP': 'Libra esterlina',
    'SEK': 'Corona sueca',
    'CLP': 'Peso chileno',
    'CHF': 'Franco suizo',
    'HKD': 'Dólar de Hong Kong',
    'TWD': 'Nuevo dólar taiwanés',
    'BRL': 'Real brasileño',
    'CAD': 'Dólar canadiense',
    'EUR': 'Euro',
    'BOB': 'Boliviano',
    'NIO': 'Córdoba nicaragüense',
    'ARS': 'Peso argentino',
    'CNY': 'Yuan chino',
    'ILS': 'Nuevo séquel israelí',
    'JPY': 'Yen japonés',
    'PEN': 'Sol peruano',
    'DOP': 'Peso dominicano',
    'TTD': 'Dólar de Trinidad y Tobago',
    'UYU': 'Peso uruguayo',
    'ANG': 'Florín antillano neerlandés',
    'AUD': 'Dólar australiano'
}

currencies_list = ['usd', 'dkk', 'cop', 'nok', 'gbp', 'sek', 'clp', 'chf', 'hkd', 'twd', 'brl', 'cad',
                   'eur', 'bob', 'nio', 'ars', 'cny', 'ils', 'jpy', 'pen', 'dop', 'ttd', 'uyu', 'ang', 'aud']

monitors = {'binance': 'Binance', 'dolartoday': 'DolarToday',
            'yadio': 'Yadio', 'airtm': 'Airtm', 'cambiosrya': 'Cambios R&A',
            'mkambio': 'Mkambio', 'bcv': 'BCV', 'promediovip': 'EnParaleloVzlaVip',
            'prom_epv': 'EnParalelovzla'}

monitors_exchange = ["dolar-em", "monitor_dolar_venezuela", "enparalelovzla", "monitor_dolar_vzla", "petro",
"bcv", "remesas_zoom", "italcambio","bancamiga","banco_de_venezuela","banco-exterior",
"banplus","bnc","banesco","bbva_provincial","mercantil","otras_instituciones",
"binance","airtm","reserve","syklo","yadio",
"dolartoday","mkambio" ,"cambios-r&a" ,"paypal" ,"zinli" ,
"skrill" ,"amazon_gift_card"]

time_units = {
    "semana": "weeks", "semanas": "weeks",
    "día": "days", "días": "days",
    "horas": "hours", "hora": "hours",
    "minutos": "minutes", "minuto": "minutes",
    "segundos": "seconds", "segundo": "seconds"
}

# https://github.com/joseaugustosoto/venezuelaBanks thank you <3
bank_dict = {
    "Banco Central de Venezuela": "bcv",
    "Banco de Venezuela": "bdv",
    "Banco Venezolano de Crédito": "bvc",
    "Mercantil Banco": "mercantil",
    "BBVA Provincial": "provincial",
    "Bancaribe": "bancaribe",
    "Banco Exterior": "exterior",
    "Banco Occidental de Descuento": "bod",
    "Banco Caroní": "caroní",
    "Banesco": "banesco",
    "Banco Sofitasa": "sofitasa",
    "Banco Plaza": "plaza",
    "Banco de la Gente Emprendedora": "bangente",
    "Banco Fondo Común": "bfc",
    "100% Banco": "100%_banco",
    "DelSur": "delsur",
    "Banco del Tesoro": "tesoro",
    "Banco Agrícola de Venezuela": "bav",
    "Bancrecer": "bancrecer",
    "Mi Banco": "mi_banco",
    "Banco Activo": "activo",
    "Bancamiga": "bancamiga",
    "Banco Internacional de Desarrollo": "b.i.d",
    "Banplus": "banplus",
    "Banco Bicentenario": "bicentenario",
    "Banco de la Fuerza Armada Nacional Bolivariana": "banfanb",
    "N58 Banco Digital": "n58",
    "Citibank": "citi",
    "Banco Nacional de Crédito": "bnc",
    "Instituto Municipal de Crédito Popular": "imcp",
    "Banco Mercantil": "mercantil_banco",
    "Otras Instituciones": "otras_instituciones",
    "Banco Nacional de Crédito BNC": "bnc",
    "BanCaribe": "bancaribe",
    "Bangente": "bangente",
}

path_images = [
    {
        "provider": "bcv",
        "title": "activo",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921460/monitors/public_id:bank-activo.webp"
    },
    {
        "provider": "bcv",
        "title": "bancamiga",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921461/monitors/public_id:bank-bancamiga.webp"
    },
    {
        "provider": "bcv",
        "title": "banesco",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921462/monitors/public_id:bank-banesco.webp"
    },
    {
        "provider": "bcv",
        "title": "banplus",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921464/monitors/public_id:bank-banplus.webp"
    },
    {
        "provider": "bcv",
        "title": "bnc",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921465/monitors/public_id:bank-bnc.webp"
    },
    {
        "provider": "bcv",
        "title": "bvc",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921466/monitors/public_id:bank-bvc.webp"
    },
    {
        "provider": "bcv",
        "title": "exterior",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921467/monitors/public_id:bank-exterior.webp"
    },
    {
        "provider": "bcv",
        "title": "otras_instituciones",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921468/monitors/public_id:bank-instituciones.webp"
    },
    {
        "provider": "bcv",
        "title": "mercantil_banco",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921469/monitors/public_id:bank-mercantil.webp"
    },
    {
        "provider": "bcv",
        "title": "plaza",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921470/monitors/public_id:bank-plaza.webp"
    },
    {
        "provider": "bcv",
        "title": "provincial",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921471/monitors/public_id:bank-provincial.webp"
    },
    {
        "provider": "bcv",
        "title": "sofitasa",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921472/monitors/public_id:sofitasa.webp"
    },
    {
        "provider": "bcv",
        "title": "mi_banco",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921472/monitors/public_id:mi_banco.webp"
    },
    {
        "provider": "bcv",
        "title": "cny",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921473/monitors/public_id:china.webp"
    },
    {
        "provider": "bcv",
        "title": "eur",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921474/monitors/public_id:european-union.webp"
    },
    {
        "provider": "bcv",
        "title": "rub",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921475/monitors/public_id:russia.webp"
    },
    {
        "provider": "bcv",
        "title": "try",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921476/monitors/public_id:turkey.webp"
    },
    {
        "provider": "bcv",
        "title": "usd",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921477/monitors/public_id:united-states.webp"
    },
    {
        "provider": "alcambio",
        "title": "bcv",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921478/monitors/public_id:bcv.webp"
    },
    {
        "provider": "alcambio",
        "title": "enparalelovzla",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921479/monitors/public_id:epv.webp"
    },
    {
        "provider": "enparalelovzla",
        "title": "enparalelovzla",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921479/monitors/public_id:epv.webp"
    },
    {
        "provider": "criptodolar",
        "title": "amazon_gift_card",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921480/monitors/public_id:amazon.webp"
    },
    {
        "provider": "criptodolar",
        "title": "dolar_today",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921481/monitors/public_id:dolartoday.webp"
    },
    {
        "provider": "criptodolar",
        "title": "bcv",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921478/monitors/public_id:bcv.webp"
    },
    {
        "provider": "criptodolar",
        "title": "airtm",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921483/monitors/public_id:airtm.webp"
    },
    {
        "provider": "criptodolar",
        "title": "binance",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921484/monitors/public_id:binance.webp"
    },
    {
        "provider": "criptodolar",
        "title": "cripto_dolar",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921484/monitors/public_id:cripto_dolar.webp"
    },
    {
        "provider": "criptodolar",
        "title": "enparalelovzla",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921479/monitors/public_id:epv.webp"
    },
    {
        "provider": "criptodolar",
        "title": "paypal",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921486/monitors/public_id:paypal.webp"
    },
    {
        "provider": "criptodolar",
        "title": "skrill",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921487/monitors/public_id:skrill.webp"
    },
    {
        "provider": "criptodolar",
        "title": "uphold",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921488/monitors/public_id:uphold.webp"
    },
    {
        "provider": "dolartoday",
        "title": "dolartoday",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921481/monitors/public_id:dolartoday.webp"
    },
    {
        "provider": "dolartoday",
        "title": "bcv",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921478/monitors/public_id:bcv.webp"
    },
    {
        "provider": "dolartoday",
        "title": "bitcoin",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921491/monitors/public_id:bitcoin.webp"
    },
    {
        "provider": "dolartoday",
        "title": "petro",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921492/monitors/public_id:petro.webp"
    },
    {
        "provider": "exchangemonitor",
        "title": "em",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921493/monitors/public_id:em.webp"
    },
    {
        "provider": "exchangemonitor",
        "title": "promedio",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1730348774/monitors/public_id:average.webp"
    },
    {
        "provider": "exchangemonitor",
        "title": "airtm",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921483/monitors/public_id:airtm.webp"
    },
    {
        "provider": "exchangemonitor",
        "title": "monitor_dolar",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921479/monitors/public_id:epv.webp"
    },
    {
        "provider": "exchangemonitor",
        "title": "enparalelovzla",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921479/monitors/public_id:epv.webp"
    },
    {
        "provider": "exchangemonitor",
        "title": "bcv",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921478/monitors/public_id:bcv.webp"
    },
    {
        "provider": "exchangemonitor",
        "title": "banco_activo",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921460/monitors/public_id:bank-activo.webp"
    },
    {
        "provider": "exchangemonitor",
        "title": "banco_bancamiga",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921461/monitors/public_id:bank-bancamiga.webp"
    },
    {
        "provider": "exchangemonitor",
        "title": "banesco",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921462/monitors/public_id:bank-banesco.webp"
    },
    {
        "provider": "exchangemonitor",
        "title": "banplus",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921464/monitors/public_id:bank-banplus.webp"
    },
    {
        "provider": "exchangemonitor",
        "title": "bnc",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921465/monitors/public_id:bank-bnc.webp"
    },
    {
        "provider": "exchangemonitor",
        "title": "bvc",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921466/monitors/public_id:bank-bvc.webp"
    },
    {
        "provider": "exchangemonitor",
        "title": "banco_exterior",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921467/monitors/public_id:bank-exterior.webp"
    },
    {
        "provider": "exchangemonitor",
        "title": "otras_instituciones",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921468/monitors/public_id:bank-instituciones.webp"
    },
    {
        "provider": "exchangemonitor",
        "title": "banco_mercantil",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921469/monitors/public_id:bank-mercantil.webp"
    },
    {
        "provider": "exchangemonitor",
        "title": "banco_plaza",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921470/monitors/public_id:bank-plaza.webp"
    },
    {
        "provider": "exchangemonitor",
        "title": "banco_provincial",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921471/monitors/public_id:bank-provincial.webp"
    },
    {
        "provider": "exchangemonitor",
        "title": "el_dorado",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921508/monitors/public_id:el-dorado.webp"
    },
    {
        "provider": "exchangemonitor",
        "title": "syklo",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921509/monitors/public_id:syklo.webp"
    },
    {
        "provider": "exchangemonitor",
        "title": "dolartoday",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921481/monitors/public_id:dolartoday.webp"
    },
    {
        "provider": "exchangemonitor",
        "title": "yadio",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921510/monitors/public_id:yadio.webp"
    },
    {
        "provider": "exchangemonitor",
        "title": "cambios_r&a",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921606/monitors/public_id:cambios-rya.webp"
    },
    {
        "provider": "exchangemonitor",
        "title": "mkfrontera",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1729921607/monitors/public_id:mk-frontera.webp"
    }
]
list_monitors_images = [Image(**item) for item in path_images]