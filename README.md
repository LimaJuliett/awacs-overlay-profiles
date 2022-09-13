# installation
[Install Python 3](https://www.python.org/downloads/) if you do not already have it. No libraries should be required (depends on json and os).

Download awacs-radios-profiles.py to a folder of your choosing. You may also choose to download the example profile as reference.

You can run the Python program to select a profile, then a .json to apply it to. By default, it searches for profiles in the same folder as itself, and a .json to write to in C:\Program Files\DCS-SimpleRadio-Standalone (the default install location for SRS).

# profile syntax
Profiles are .json files with three sections:
- Comments: soley for the user's information. The program completey ignores this section
- radios: radio settings (things like name, default frequency, modulation, and tuneable range)
- channels: channels (name, frequency, and modulation)

## radios
The radios section contains a list of 10 items, with each item being a radio. The first item is for Radio 1, the next Radio 2, and so on (radios are numbered left to right, top to bottom, same as in SRS). Each radio has:
- `name`: can be any string. Names that are too long will be truncated to fit in the overlay by SRS.
- `modulation`: string. Can be either AM or FM.
- `band`: string. Controls the tuneable frequency range.
  - `HF`: 1 to 100 MHz (inclusive)
  - `VHF`: 100 to 200 MHz (inclusive)
  - `UHF`: 200 to 400 MHz (inclusive)
  - `all`: 1 to 400 MHz (inclusive)
- `default-freq`: int, float, or string. Defines the frequency the radio is tuned to when the overlay is first opened.
- `channels`: list of strings. Assigns channels to radio.
  - arbitrary string: assignes the channel of that name to the radio.
  - all: stands in for a list of every channel, in the order of the channels section
  - HF, VHF, and UHF stand in for a list of all channels that have a frequency in that range (frequency ranges are same as band settings, see above)

### default-freq
Can be a number (int or float) or a channel name (string). If it is a number, the radio's default frequency will be that number (MHz). If it is a string, the radio's default frequency will be the frequency of the channel with that name. For example: `251` or `251.0` will set the radio's default frequency to 251 MHz. `"Channel 1"` will set the radio's default frequency to the frequency of Channel 1.

### channels
The program goes through this list item by item, adding each item to the list of channels for that radio. You can create a list of channels for a radio by putting each channel's name as an item in the list. For example: `"Channel 1", "Channel 2", "Channel 3"` will cause the radio to have those channels in that order.

Some shortcut strings to make life easier:
| keyword | function |
|----------|------------|
| `all` | all channels |
| `HF` | all channels with frequency between 1 and 100 MHz  |
|`VHF` | all channels with frequency between 100 and 200 MHz |
|  `UHF` | all channels with frequency between 200 and 400 MHz |

Keywords add channels in the order they're listed in the channels section.

Multiple keywords can also be used. For example, the list `["UHF", "VHF", "HF"]` will cause the radio to have all UHF channels, then all VHF channels, then all HF channels, listed in that order.

The program **will only add channels with the same modulation as the radio.** You cannot hear or talk to someone using a different modulation than you.

# how it works
SRS stores settings for the AWACS overlay in awacs-radios.json, located in the SRS installation location (C:\Program Files\DCS-SimpleRadio-Standalone is the default). Channels are stored as .txt files in the same directory.

This program edits awacs-radios.json and replaces .txt files in the SRS folder to match a selected profile. Profiles dictate radio names, default frequencies, tuneable frequency range, radio modulation (AM or FM), and radio channels.
