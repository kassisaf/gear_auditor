# gear_auditor

### What does it do?

Gear auditor is a script that will extract your FFXI characters' inventory using data generated by the `findall` addon, compare it to items in your `GearSwap` luas, and identify any items not in use.  It is a work in progress.

### Planned Features

- Generate a spreadsheet with full inventory information for all characters
- Identify items that could be moved to storage slips
- Calculate number of shards and voids needed based on your current relic upgrade levels
- Display POL sendable flag (identify mule-able items)
- Generate checklists for Unity, HTMB, etc. (maybe?)

### Requirements
- Windower 4 installation with the `GearSwap` and `findall` addons installed
- `findall` must have been loaded at least once to generate the necessary inventory data
- Gear must be present **as strings** in luas within your `GearSwap` data folder.  **Currently, item variables are *not* parsed as items.**

### How do I run it?

1. Download and install the latest version of [Python](https://www.python.org/downloads/)
2. Download and extract this repo (or git clone it)
3. Run `python main.py` from a terminal
4. Browse to and select your Windower folder when prompted
