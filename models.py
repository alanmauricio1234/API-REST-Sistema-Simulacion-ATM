from datetime import date
cards = [
    {
        'n_tarjeta': '1111',
        'nip': 1234,
        'f_vencimiento': date(2023,12,1),
        'saldo': 4000.0,
        'limite': 1500.0,
        'es_bloqueada': False,
        'es_verificada': False,
        'intento': 3
    },
    {
        'n_tarjeta': '2222',
        'nip': 1234,
        'f_vencimiento': date(2020,11,18),
        'saldo': 5500.0,
        'limite': 5500.0,
        'es_bloqueada': False,
        'es_verificada': True,
        'intento': 0
    },
    {
        'n_tarjeta': '3333',
        'nip': 2345,
        'f_vencimiento': date(2024,1,1),
        'saldo': 0.0,
        'limite': 2000.0,
        'es_bloqueada': False,
        'es_verificada': True,
        'intento': 0
    },
    {
        'n_tarjeta': '4444',
        'nip': 2345,
        'f_vencimiento': date(2020,11,18),
        'saldo': 10000.0,
        'limite': 5000.0,
        'es_bloqueada': True,
        'es_verificada': True,
        'intento': 0
    },
    {
        'n_tarjeta': '5555',
        'nip': 2345,
        'f_vencimiento': date(2018,5,1),
        'saldo': 50000.0,
        'limite': 3000.0,
        'es_bloqueada': True,
        'es_verificada': True,
        'intento': 0
    },
    {
        'n_tarjeta': '6666',
        'nip': 1234,
        'f_vencimiento': date(2023,1,18),
        'saldo': 5000.0,
        'limite': 2500.0,
        'es_bloqueada': False,
        'es_verificada': True,
        'intento': 0
    },
    {
        'n_tarjeta': '7777',
        'nip': 5678,
        'f_vencimiento': date(2023,2,10),
        'saldo': 50000.0,
        'limite': 10000.0,
        'es_bloqueada': False,
        'es_verificada': True,
        'intento': 0
    }
]

def find_card(n_tarjeta):
    for card in cards:
        if (card['n_tarjeta'] == n_tarjeta):
            return card
    return None