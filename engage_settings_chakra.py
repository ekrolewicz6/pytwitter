#!/usr/bin/python

from __future__ import print_function
from time import localtime, strftime
import twitter
import random

CONSUMER_KEY = 'fP7SRcKlEsYYsQosCtkJB7Ktg'
CONSUMER_SECRET = '8mMrZ2AHzP6LUxVPBEaoWknJFdoGkPWDvcd6ge74KGoqD15mnq'
ACCESS_TOKEN = '821692353131839488-3Y4PFI2WjOa5jirQNaz1sVJU6LZQ0KR'
ACCESS_TOKEN_SECRET = '80os3qt0jCzmPM96X0SgLNbtFwyUcfvDzCse1A57mGskY'


# Create an Api instance.
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET,
                  sleep_on_rate_limit=True)


# SEND TIME SETTINGS:
send_every_days = 7
send_on_days = ["Tuesday","Thursday"]
send_at_times = ["1:00pm","2:00pm"]
send_to_groups = ['Current Followers', 'Propsective Followers']

#TODO figure out how to schedule tasks.


# Get bio+title keywords
bio_kws = ['Reiki Master','Reiki Practitioner','Energy worker','Light-touch practitioner','Medium',
'Spiritual Advisor','Psychic Medium','Pranic Healer','Medical Intuitive','Psychic Tarot Reader','Reiki-Sechiem practitioner','Shaman Baphomet',
'Hypnotherapist','Cellular Recall Therapy','Crystal Whisperer','Soul Empowerer','Life Illuminator','Tibetan Reiki',
'Social Worker','Herbalist','LMT CEUs','Body alchemist','Clairvoyant','Auro diagnosis','Lomi Bodywork','Personal Development Coach',
'Cranio-sacral therapy','Holistic birth','Doula','Water birth','Recalibration healing','Shamana','Respiratory Therapist',
]

# Get Post Keywords
post_kws = ['Aesthetic Candles','Earth','healing',	'Oracle cards',	'Spiritual','angels',	'Earth child',	'holistic',	'Owl',	'Spirtual being',
'Astrology',	'EFT',	'Hopi Ear Candling',	'pixies',	'Taoism',
'Awaken',	'Energy Psychology',	'Hot stones',	'Quartz',	'Tuning Forks',
'Ayurveda',	'Energy work',	'Karuna',	'reiki',	'Universal energy',
'Chakra Balancing',	'Essential oils',	'LOA',	'Reiki Vibration',	'Waking up',
'clarity',	'Fairy',	'Meditation',	'Self-healing',	'YL Essential Oils',
'Crunchy',	'Fantasy',	'Melchizedek',	'shamanism',	'Yoga',
'Crystal Singing Bowls',	'Feng shui',	'metaphysical',	'soul',	'Natural healing'
'Earth',	'Granola',	'Mindfulness',	'Soy candles',	
			'Spirit',]

# Set Location
city = 'Portland, OR'

# Get a list of targets
targets = ['PortlandHR','TBoPortland','ProvvistaNW','zupans','newseasons']