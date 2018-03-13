#!/usr/bin/python

from __future__ import print_function
from time import localtime, strftime
import twitter
import random
import os

CONSUMER_KEY = os.environ($CONSUMER_KEY)
CONSUMER_SECRET = os.environ($CONSUMER_SECRET)
ACCESS_TOKEN = os.environ($ACCESS_TOKEN)
ACCESS_TOKEN_SECRET = os.environ($ACCESS_TOKEN_SECRET)


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
