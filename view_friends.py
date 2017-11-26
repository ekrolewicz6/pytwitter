#!/usr/bin/env python

# Copyright 2016 The Python-Twitter Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ------------------------------------------------------------------------
# Change History
# 2010-10-01
#   Initial commit by @jsteiner207
#
# 2014-12-29
#   PEP8 update by @radzhome
#
# 2016-05-07
#   Update for Python3 by @jeremylow
#

from __future__ import print_function
import twitter
import time


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


targets = ['PortlandHR','TBoPortland','ProvvistaNW','zupans','newseasons']
users = []
for target in targets:
	users = users + api.GetFriends(target)

print('Number of found users: ', len(targets))

for user in users:
	print("Befriended: %s" % user.screen_name)
	api.CreateFriendship(user.id)


print("Followed %s: ", len(users) % target)
