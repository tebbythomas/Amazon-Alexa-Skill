# -*- coding: utf-8 -*-

# Resolving gettext as _ for module loading.
from gettext import gettext as _

SKILL_NAME = "Bangalore Guide"

WELCOME = _("Welcome to Bangalore Guide!")
HELP = _("Say about, to hear more about the city, or say coffee, breakfast, lunch, or dinner, to hear local restaurant suggestions, or say recommend an attraction, or say, go outside. ")
ABOUT = _("Bangalore, Karnataka is a city in South India. A popular city for anything tech related, Bangalore is known for its tech scene and diverse urban population.")
STOP = _("Okay, see you next time!")
FALLBACK = _("The {} can't help you with that. It can help you learn about Bangalore if you say tell me about this place. What can I help you with?")
GENERIC_REPROMPT = _("What can I help you with?")

CITY_DATA = {
    "city": "Bangalore",
    "state": "Karnataka",
    "postcode": "560025",
    "restaurants": [
        {
            "name": "A Whole Lotta Love",
            "address": 'Koramangala',
            "phone": '978-283-0474',
            "meals": 'Breakfast',
            "description": 'A cozy and popular spot for breakfast.  Try the omlettes!',
        },
        {
            "name": 'Cafe Coffee Day',
            "address": 'Richmond Road',
            "phone": '978-281-1851',
            "meals": 'coffee, snacks',
            "description": 'A cafe part of the famous CCD chain that serves reasonably good coffee and snacks like sandwiches',
        },
        {
            "name": 'Corner House',
            "address": 'Residency Road, Ashoknagar',
            "phone": '978-281-5310',
            "meals": 'Desserts',
            "description": 'A favorite hangout spot for people wanting to grab a yummy dessert',
        },
    ],
    "attractions": [
        {
            "name": 'Lalbagh',
            "description": 'The Lalbagh botanical garden is a 250 acre breathing space near Wilson Garden.',
            "distance": '5',
        },
        {
            "name": 'Vidhana Soudha',
            "description": 'It is the seat of the state legislature of Karnataka. It is constructed in a style sometimes described as Mysore Neo-Dravidian',
            "distance": '2',
        },
    ],
}

MY_API = {
    "host": "https://query.yahooapis.com",
    "port": 443,
    "path": "/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22{city}%2C%20{state}%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys",
}
