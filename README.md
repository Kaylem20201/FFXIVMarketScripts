# FFXIVMarketScripts
Python scripts for analyzing FFXIV Market

These are python scripts meant to analyze good items for focusing on in the FFXIV market, primarily by using the Universalis and FFXIV APIs.
This is mostly a personal project to help myself acclimate to some new coding environments. In particular, I want to teach myself Python, Git, and Bash scripting using these, so I'm sorry if the code isn't very standard right now, I want to learn by doing. My hope is to create a collection of modular functions that work well together to make it easy to analyze various aspects of the market, and be adaptable to changes.

FFXIV's market is not quite comparable to a real life economy due to several factors like botting. Gathering, for example, is known to be very inefficent to make money off of despite being needed for almost anything. On top of this, I've never been very good at understanding the market, and despite having played this game a very long time, I struggle to jump on good money makers most of the time. So these tools are meant to examine the markets from a few different angles and find efficent items to focus on.

## gilVolume.py:
The intention of this script is to find items that both sell for a decent amount, and sell quickly relative to that amount. We do this by calculating a "Gil Velocity", which is simply the Sale Velocity ("The average number of sales per day, over the past seven days (or the entirety of the shown sales, whichever comes first)") multiplied by the median price of the item over a given time period. This should be particularly helpful for crafted items, since it is difficult to tell at a glance which items will consistently sell well.
Prints a json dictionary of {item_id: gil_velocity}, sorted by descended gil velocity.
Note: Universalis has a "Trade Velocity" request that sounds ideal by it's description, but it appears to be bugged at the moment, returning nothing.

## itemIDToName.py
Takes a json dictionary where the keys are item_ids (like the one returned by gilVolume). Should help make the result of any script human-readable.

## To-do:
- Right now gilVolume uses the most recently updated items request, which maxes out at 200 items. This is okay, but we should make getting item lists it's own script, and pass them into gilVelocity. Ideally, we want to be able to filter items by useful categories (like "Craftable", for example).
- The json format I return from gilVelocity is terrible, and would be even worse if other scripts follow this format. This needs to be restructured with human readable keys.
- Maybe add flags for cleaning up input/output. Right now I was using a command like "python3 gilVolume.py | python3 itemIdToName.py > dump.txt; cat dump.txt", which works but might not be very expandable.
- Create a script for finding niche, underserved markets (High Value, Low Supply, Okay-Great Sale Velocity)
- Create a script for retrieving lists of items of a certain useful category (i.e. "Craftable", "Materia", "Treasure Maps", etc.)
- Create a script for analyzing profit margins of final craftable products to raw or intermediate materials
- Create a script for analyzing worst and best times to buy/sell over the week or day. (Day trading, essentially).
- Maybe: create a script to analyze value of an item compared to the subjective effort/time required to get it. ("Is it more valuable to farm Titania or Rubicante?" type questions).
