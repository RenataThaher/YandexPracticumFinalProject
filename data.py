import datetime

CREATE_ORDER_DATA = {
    'firstName': 'Naruto',
    'lastName': 'Uzumaki',
    'address': 'Kanoha, st 6',
    'metroStation': '5',
    'phone': '+78005553535',
    'rentTime': 2,
    'deliveryDate': (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%dT00:00:00.000Z'),
    'comment': 'Bla bla bla',
    'color': ['BLACK'],
}
