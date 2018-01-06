#!/usr/bin/python

from __future__ import print_function
from time import localtime, strftime
import twitter
import random

CONSUMER_KEY = 'ISQPrRJ3UvtNl17hdURE95XYd'
CONSUMER_SECRET = 'C1BUGhoi00iZkW0WlGZyzloIFtuHvvd60Rp6Ysq1QQhgTk2dYv'
ACCESS_TOKEN = '910266067213180928-LIRuvdeYl2X1XRXCRA12Gk3cUSLyoXd'
ACCESS_TOKEN_SECRET = 'WwQ2xo67CnEJGeTVbcmLwyaY5Dx3f2SMnhHY40mc8dKVy'


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
bio_kws = ['foodie','food blogger', 'Buyer','CEO','CFO','COO','Employee Relations Director',
'Employee Relations Manager','Facilities Manager','Food Blogger','Food Journalist','Food Photographer','Foodie','HR','HR Assistant','HR Director','HR Manager',
'HR Supervisor','Human Resources','Human Resources Assistant','Human Resources Director','Human Resources Manager',
'Human Resources Supervisor','Inventory Manager','MRO Buyer','Office Manager','Operations Manager','PHR','Procurement Specialist','Professional in HR','Professional in Human Resources',
'Purchaser','Purchasing Director','Purchasing Manager','Purchasing Manager','Recruiter','Recruiting',
'Senior Buyer','SPHR','staffing','Staffing Associate','Talent','Talent Acquisition','Vendor Relations','Chef']

# Get Post Keywords
post_kws = ['food','eatpdx','pdxeats','portland food', 'eat portland','delicious', 'yummy', 'fish', 'brunch', 'roasted', 'Avanti', 
			'Avanti','micro-market','Canteen','R Squared','Evergreen Vending','Avenue C','Honor Box','Blue Tiger','Agora',
			'Portland Pedal Power','Royal Vending NW','Farmer Brothers','Belmont Coffee Services','Percasso Coffee Services','First Choice Coffee',
			'World Cup Roasters', 'work','micro-market','foodie','vending machine','Kombucha','office','New Seasons','food','market','Foodie',
			'Crave','kombucha','eatpdx','SHRM','LWHRA','benefits','NWFE','fitness','vending','instagood','Honor Box',
			'foodporn','Sandwiches','healthy','Sandwich','sweet','Salad','officelife','Wrap','officework','organic food',
			'ceo','organicfood','portland','bevi','workfood','marketfood','freshfood','locallysourced','localsource','employeebenefits',
			'employeefeedback','cold brew','fresh juice','Jerky','pro bar','rx bar','yogurt','Costco Business','Aramark',
			'employeeengagement','workexperience','foodtech','Fair Trade', 'Non-GMO', 'Gluten-Free', 'glutenfree','lactosefree','Lactose-Free','gluten', 'lactose','water', 'coffee', 'tea',
			'organic','PortlandBeer','Keg','Growler','cider','mead','brews','wine','chef','ingredients', 'chocolate', 'paleo']

exception_kws = ['police','pdx911']

# Set Location
city = 'Portland, OR'

# Get a list of targets
targets = ['PortlandHR','TBoPortland','ProvvistaNW','zupans','newseasons']
