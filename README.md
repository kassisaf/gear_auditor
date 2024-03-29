# gear_auditor

gear_auditor is an inventory management tool for FFXI Windower users.  Currently, all it does is generate a list of equipment you're carrying and not actively using in GearSwap. 

This project is a work in progress and I make no guarantees on its accuracy.  **Please double-check before dropping any items you might still need!**

### Planned Features

- Generate a spreadsheet with full inventory information for all characters
- Highlight items that could be moved to storage slips
- Highlight duplicate Sortie earrings
- Display POL sendable flag (identify mule-able items)
- Calculate number of shards and voids needed based on your current relic upgrade levels
- Generate checklists for Unity, HTMB, etc. (maybe?)

### Getting Started

#### Requirements
- Windower 4 installation with the `GearSwap` and `findall` addons installed
- `findall` must have been loaded at least once to generate the necessary inventory data
- GearSwap must contain one or more lua files applicable to your character (either prefixed with character's name or in the format of JOB.lua) 

#### How to Run

1. Download and install the latest version of [Python](https://www.python.org/downloads/)
2. Download and extract this repo (or git clone it)
3. Run `python main.py` from a terminal
4. Browse to and select your Windower folder when prompted
