# gear_auditor

### What does it do?

Gear auditor is a script that will extract your FFXI characters' inventory using data from the `findall` addon, compare it to items in your `GearSwap` luas, and identify any items not in use.

### Requirements
- Windower 4 installation with the `GearSwap` and `findall` addons installed
- `findall` must have been loaded at least once to generate the necessary inventory data
- Gear must be present **as strings** in luas within your `GearSwap` data folder.  Currently, item variables are *not* parsed as items.

### How do I run it?

1. Download and install [Python](https://www.python.org/downloads/)
2. Download and extract (or git clone) this repo and run main.py
3. Point it to your Windower folder