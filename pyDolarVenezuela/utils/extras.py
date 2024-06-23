from ..models.images import Image

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
    "BanCaribe": "bancaribe"
}

path_images = [
    {
        "title": "bcv",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1717042862/alcambio/pff3ahlx2ilvcf48ijne.png",
        "provider": "alcambio"
    },
    {
        "title": "enparalelovzla",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1717042885/alcambio/pzlgnhggdwgkzzg3ndfs.png",
        "provider": "alcambio"
    },
    {
        "title": "usd",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093823/bcv/uppdtt4fzbhnwq5cu9br.png",
        "provider": "bcv"
    },
    {
        "title": "try",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716099345/bcv/zowkdfsqlmiafsksgdwb.png",
        "provider": "bcv"
    },
    {
        "title": "eur",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093824/bcv/epzeuzakymrxe1ygwvvp.png",
        "provider": "bcv"
    },
    {
        "title": "rub",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093824/bcv/nyuavxoe4edpahvuzciv.png",
        "provider": "bcv"
    },
    {
        "title": "cny",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093825/bcv/wqfalezwajdzzj6lqe8g.png",
        "provider": "bcv"
    },
        {
        "title": "bancamiga",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093825/criptodolar/kvey6stefly2tz0iycxb.png",
        "provider": "criptodolar"
    },
    {
        "title": "banco_mercantil",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093826/criptodolar/cv11ywpqffhu5nm9jvnu.png",
        "provider": "criptodolar"
    },
    {
        "title": "banco_provincial",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093827/criptodolar/ucd3xjeni9msgrjlfdtg.png",
        "provider": "criptodolar"
    },
    {
        "title": "banco_venezuela",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093828/criptodolar/yepxycceaprq0feladr9.png",
        "provider": "criptodolar"
    },
    {
        "title": "banesco",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093828/criptodolar/oppovzonizubffeuezwd.png",
        "provider": "criptodolar"
    },
    {
        "title": "banplus",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093830/criptodolar/eyf6tzib8dpvbruueq6h.png",
        "provider": "criptodolar"
    },
    {
        "title": "bnc",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093830/criptodolar/o0x92ehatdf3tvdeojeg.png",
        "provider": "criptodolar"
    },
    {
        "title": "binance",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093832/criptodolar/vfeeir2qfehonclityeb.png",
        "provider": "criptodolar"
    },
    {
        "title": "cripto_dolar",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093832/criptodolar/la54eximbsqbydf9madc.png",
        "provider": "criptodolar"
    },
    {
        "title": "dolar_today",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093833/criptodolar/qqmrcjkh49tjjcfoteip.png",
        "provider": "criptodolar"
    },
    {
        "title": "amazon_gift_card",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093834/criptodolar/i30kozfg2qbicxqclcbu.png",
        "provider": "criptodolar"
    },
    {
        "title": "paypal",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093834/criptodolar/pgyukgc2p2kxg9a1urpl.png",
        "provider": "criptodolar"
    },
    {
        "title": "bcv",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093835/criptodolar/pxef065ha5r6zzpfizxy.png",
        "provider": "criptodolar"
    },
    {
        "title": "skrill",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093836/criptodolar/cyp71axif36rurqulqnr.png",
        "provider": "criptodolar"
    },
    {
        "title": "uphold",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093837/criptodolar/qezqmjzibtor9wr7pv6m.png",
        "provider": "criptodolar"
    },
    {
        "title": "enparalelovzla",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093838/criptodolar/jukudiiabja65ijuu8yo.png",
        "provider": "criptodolar"
    },
        {
        "title": "airtm",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093839/exchangemonitor/bekyy0llre7ypyk25rgo.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "amazon_gift_card",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093840/exchangemonitor/s9eujyaebumcwpblupr0.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "bancamiga",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093842/exchangemonitor/ylqelunizpr6frababbe.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "bancaribe",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1719023856/exchangemonitor/burnekr9pidop4wz3xrx.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "banco_de_venezuela",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1719023820/exchangemonitor/zlz0iuhw3me4ldhu9k1g.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "banco_exterior",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093842/exchangemonitor/eyf90rndgix2ayfirptz.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "banca_plaza",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1719023752/exchangemonitor/aqmehn1enysonjsihed3.webp",
        "provider": "exchangemonitor"
    },
        {
        "title": "banplus",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1719023923/exchangemonitor/vg4gibg5y4ziyloejlrl.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "banesco",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093843/exchangemonitor/wb581lw04tyccpemgvlw.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "bbva_provincial",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093843/exchangemonitor/snwobyspdjueqk3hnmcy.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "bcv",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093844/exchangemonitor/cynwwdlkdcstqxfwxetc.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "binance",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093844/exchangemonitor/uxmug0r4taifpy2tkk77.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "bnc",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093845/exchangemonitor/dvxkxspvbifxnv9iwjfm.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "cambios_r&a",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093846/exchangemonitor/bo152xqyrshncklgcp0b.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "dolartoday_(btc)",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093847/exchangemonitor/samnvo9ml1bjwwbky87h.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "dolartoday",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093847/exchangemonitor/jojtn5gu1g52zq3el3zp.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "el_dorado",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093849/exchangemonitor/klzike64gmwlhnpyuuju.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "dolar_em",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093849/exchangemonitor/mx1tostafvbftdn1ofbe.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "italcambio",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093850/exchangemonitor/ma295gq8ftcasuh3ki8o.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "mercantil",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093850/exchangemonitor/w0xsro1si7laxalu8zgs.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "mkambio",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093851/exchangemonitor/himq41taohdcxbcnlgub.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "monitor_dolar_vzla",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093852/exchangemonitor/qwydse1rhwqyzh4vzmyj.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "monitor_dolar_venezuela",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093852/exchangemonitor/kih3nvrygbratbtzvvew.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "monitor_dolar",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093852/exchangemonitor/kih3nvrygbratbtzvvew.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "enparalelovzla",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093852/exchangemonitor/kih3nvrygbratbtzvvew.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "otras_instituciones",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093853/exchangemonitor/myh2wpnsaruz462fbhqs.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "paypal",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093853/exchangemonitor/hsvaysq1ow3ayaefm5b7.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "petro",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093855/exchangemonitor/vrguo6kaxxa7zmtyp88u.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "remesas_zoom",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093855/exchangemonitor/ki6sg08a1c1yoe2tp7ou.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "skrill",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093856/exchangemonitor/e6i3rygmyjft0mwbfeif.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "syklo",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093856/exchangemonitor/ctpuvtmlxtakuon6e2la.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "yadio",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093857/exchangemonitor/kj25w4xgtz4ztgoljrqz.webp",
        "provider": "exchangemonitor"
    },
    {
        "title": "zinli",
        "image": "https://res.cloudinary.com/dcpyfqx87/image/upload/v1716093857/exchangemonitor/t4ncrzmvldaw1kzqpc0v.webp",
        "provider": "exchangemonitor"
    }
]
list_monitors_images = [Image(**item) for item in path_images]