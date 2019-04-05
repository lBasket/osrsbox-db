"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Description:
This is a quick script to check the contents of the items-ammo-requirements.json
file by comparing it to the item database: item.equipment.slot property.

Copyright (c) 2019, PH01L

###############################################################################
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################
"""

import json
from pathlib import Path

import config
from osrsbox import items_api


# These bad IDs are prayer scrolls that are also equiped in the ammo slot
BAD_IDS = [20220, 20223, 20226, 20229, 20232, 20235, 22941, 22943, 22945, 22947]


if __name__ == "__main__":
    # Load all items
    all_db_items = items_api.load()

    ammo_items = dict()

    # Loop through all items in the database and print the item name for each item
    for item in all_db_items:
        # Check if item is equipable, and is not memebers (aka f2p item)
        if item.equipable_by_player:
            if item.equipment.slot == "ammo":
                # print(f"{item.id:<6} {item.name}")  # New, f-strings printing method
                ammo_items[item.id] = item.name

    loc = Path(config.DATA_PATH / "item-ammo-requirements.json")
    with open(loc) as f:
        data = json.load(f)

    for k, v in ammo_items.items():
        if k in BAD_IDS:
            continue
        print(f"{k}, {v}, {data[str(k)]}")

    print("DONE")
