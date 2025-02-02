#!/usr/bin/env python3
#-*- coding: utf-8 -*-
'''gbadges.py: Calculates which players will get the Global Map Legend badge

The MIT License (MIT)

Copyright (c) 2021-present Buster

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
'''

import json
from pathlib import Path

from tabulate import tabulate

__author__ = 'Buster#5741'
__license__ = 'MIT'

EVENT = input('Event name > ').lower().replace(' ', '_')
REGION = input('Region > ').lower()
FILENAME = input('Post ban data filename > ')
CLAN_AMOUNT = int(input('Clan amount > '))
PLAYER_AMOUNT = int(input('Player amount > '))

def main(file_path: Path) -> dict:
    gbadge_gamers = {}
    with open(file_path, encoding='utf-8') as file:
        data = json.load(file)

    for player_id, player_data in data.items():
        if all([player_data['player_rank'], player_data['clan_rank']]):
            if (player_data['player_rank'] <= (PLAYER_AMOUNT / 100)) \
            and (player_data['clan_rank'] <= (CLAN_AMOUNT / 100)):
                gbadge_gamers[player_id] = player_data

    return gbadge_gamers

if __name__ == '__main__':
    gbadges = main(Path(f'globalmap_data/{REGION}/{EVENT}/{FILENAME}.json'))
    formatted = []

    for i, (player_id, player_data) in enumerate(gbadges.items(), 1):
        formatted.append([str(i).zfill(3), player_data['player_name'], player_data['player_rank'], player_data['clan_tag'], player_data['clan_rank']])

    with open(f'globalmap_data/{REGION}/{EVENT}/gbadges.txt', 'w', encoding='utf-8') as file:
        file.write(tabulate(
            tabular_data=formatted,
            headers=['Index', 'Name', 'Rank', 'Clan', 'Rank'],
            tablefmt='presto',
            numalign='left'
        ))
