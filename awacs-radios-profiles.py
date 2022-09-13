import json
import os
from tkinter import filedialog

awacs_radios_template_raw = '''
[
  {
    "enc": false,
    "encKey": 0,
    "encMode": 0,
    "freqMax": 100.0,
    "freqMin": 100.0,
    "freq": 100.0,
    "modulation": 2,
    "name": "SATCOM",
    "secFreq": 0.0,
    "volume": 1.0,
    "freqMode": 0,
    "volMode": 1,
    "expansion": false,
    "channel": -1,
    "simul": false,
    "rtMode": 2
  },
  {
    "enc": false,
    "encKey": 1,
    "encMode": 1,
    "freqMax": 400000000.0,
    "freqMin": 1000000.0,
    "freq": 251000000.0,
    "modulation": 0,
    "name": "UHF Guard",
    "secFreq": 243000000.0,
    "volume": 1.0,
    "freqMode": 1,
    "volMode": 1,
    "expansion": false,
    "channel": -1,
    "simul": false,
    "rtMode": 1
  },
  {
    "enc": false,
    "encKey": 1,
    "encMode": 1,
    "freqMax": 400000000.0,
    "freqMin": 1000000.0,
    "freq": 251000000.0,
    "modulation": 0,
    "name": "UHF Guard",
    "secFreq": 243000000.0,
    "volume": 1.0,
    "freqMode": 1,
    "volMode": 1,
    "expansion": false,
    "channel": -1,
    "simul": false,
    "rtMode": 1
  },
  {
    "enc": false,
    "encKey": 1,
    "encMode": 1,
    "freqMax": 76000000.0,
    "freqMin": 1000000.0,
    "freq": 30000000.0,
    "modulation": 1,
    "name": "VHF FM",
    "secFreq": 1.0,
    "volume": 1.0,
    "freqMode": 1,
    "volMode": 1,
    "expansion": false,
    "channel": -1,
    "simul": false,
    "rtMode": 1
  },
  {
    "enc": false,
    "encKey": 1,
    "encMode": 1,
    "freqMax": 400000000.0,
    "freqMin": 1000000.0,
    "freq": 251000000.0,
    "modulation": 0,
    "name": "UHF Guard",
    "secFreq": 243000000.0,
    "volume": 1.0,
    "freqMode": 1,
    "volMode": 1,
    "expansion": false,
    "channel": -1,
    "simul": false,
    "rtMode": 1
  },
  {
    "enc": false,
    "encKey": 1,
    "encMode": 1,
    "freqMax": 400000000.0,
    "freqMin": 1000000.0,
    "freq": 251000000.0,
    "modulation": 0,
    "name": "UHF Guard",
    "secFreq": 243000000.0,
    "volume": 1.0,
    "freqMode": 1,
    "volMode": 1,
    "expansion": false,
    "channel": -1,
    "simul": false,
    "rtMode": 1
  },
  {
    "enc": false,
    "encKey": 0,
    "encMode": 0,
    "freqMax": 400000000.0,
    "freqMin": 1000000.0,
    "freq": 124800000.0,
    "modulation": 0,
    "name": "VHF Guard",
    "secFreq": 121500000.0,
    "volume": 1.0,
    "freqMode": 1,
    "volMode": 1,
    "expansion": false,
    "channel": -1,
    "simul": false,
    "rtMode": 1
  },
  {
    "enc": false,
    "encKey": 0,
    "encMode": 0,
    "freqMax": 400000000.0,
    "freqMin": 1000000.0,
    "freq": 124800000.0,
    "modulation": 0,
    "name": "VHF Guard",
    "secFreq": 121500000.0,
    "volume": 1.0,
    "freqMode": 1,
    "volMode": 1,
    "expansion": false,
    "channel": -1,
    "simul": false,
    "rtMode": 1
  },
  {
    "enc": false,
    "encKey": 1,
    "encMode": 1,
    "freqMax": 76000000.0,
    "freqMin": 1000000.0,
    "freq": 30000000.0,
    "modulation": 1,
    "name": "VHF FM",
    "secFreq": 1.0,
    "volume": 1.0,
    "freqMode": 1,
    "volMode": 1,
    "expansion": false,
    "channel": -1,
    "simul": false,
    "rtMode": 1
  },
  {
    "enc": false,
    "encKey": 0,
    "encMode": 0,
    "freqMax": 400000000.0,
    "freqMin": 1000000.0,
    "freq": 124800000.0,
    "modulation": 0,
    "name": "VHF Guard",
    "secFreq": 121500000.0,
    "volume": 1.0,
    "freqMode": 1,
    "volMode": 1,
    "expansion": false,
    "channel": -1,
    "simul": false,
    "rtMode": 1
  },
  {
    "enc": false,
    "encKey": 0,
    "encMode": 0,
    "freqMax": 400000000.0,
    "freqMin": 1000000.0,
    "freq": 124800000.0,
    "modulation": 0,
    "name": "VHF Guard",
    "secFreq": 121500000.0,
    "volume": 1.0,
    "freqMode": 1,
    "volMode": 1,
    "expansion": false,
    "channel": -1,
    "simul": false,
    "rtMode": 1
  }]
'''

awacs_radios_template = json.loads(awacs_radios_template_raw)

def main():
    # file explorer open dialog to select the profile to load
    print('Getting configuration file... ', end = '')
    with filedialog.askopenfile(mode='r', title='Select AWACS profile', initialdir='.', filetypes=(('JSON Files', "*.json"), ('All files', "*.*"))) as new_config_file:
        filepath = os.path.realpath(new_config_file.name)
    with open(filepath, 'r', encoding='utf-8-sig') as new_config_file:
        try:
            new_config = json.loads(new_config_file.read())
        except json.JSONDecodeError:
            print('Could not parse JSON. Check that the file is valid JSON and try again.')
            input('Press Enter to exit... ')
            exit()
    print('Done')

    # TODO verify the profile

    print('Generating new awacs-radios json... ', end = '')
    try:
        modify_awacs_radios(awacs_radios_template, new_config)
    except Exception as exception:
        print('Something went wrong! All JSON is valid, but there may be improper keyword usage, improper application of quotation marks, or some other issue.\nCheck your file and try again.\n')
        print(f"The problem (for debugging purposes): {exception}")
        input('Press Enter to exit... ')
        exit()
    print('Done')

    # show a preview of the profile and ask for write permission
    print_overlay("Selected profile:", new_config)

    proceed = input('Write this profile? (y/N): ').lower()
    print()

    # write the profile
    if proceed == 'y':
        print('Reading awacs-radios.json... ', end = '')

        with filedialog.askopenfile(mode='r', title='Select awacs-radios.json', initialdir="C:\Program Files\DCS-SimpleRadio-Standalone", filetypes=(('JSON Files', "*.json"), ('All files', "*.*"))) as awacs_radios_file:
            filepath = os.path.realpath(awacs_radios_file.name)
            folderpath = os.path.dirname(awacs_radios_file.name)
        with open(filepath, 'r', encoding='utf-8-sig') as awacs_radios_file:
            try:
                old_radionames = read_awacs_json_settings(awacs_radios_file.read())
                print('Done')

                print('Cleaning old channel texts... ')
                for radioname in set(old_radionames):
                    try:
                        os.remove(os.path.join(folderpath, radioname + '.txt'))
                    except:
                        pass
            except Exception as exception:
                print('Failed')
                print(exception)

        print(f"Writing new json to {filepath}... ", end = '')
        with open(filepath, 'w') as awacs_radios_file:
            awacs_radios_file.write(json.dumps(awacs_radios_template, indent='\t'))
        print('Done')

        print('Creating new channel texts... ', end = '')
        try:
            for radio in new_config['radios']:
                channel_text = generate_channel_text(radio, new_config)

                with open(os.path.join(folderpath, radio['name'] + '.txt'), 'w') as channel_file:
                    channel_file.write(channel_text)
            
            print('Done')
        except FinishedWithWarning as warning:
            print('Completed with warning')
            print(warning)
        except Exception as exception:
            print('Failed')
            print(exception)

        input('Press Enter to exit...')
        exit()
    else:
        input('Press Enter to exit... ')
        exit()

def read_awacs_json_settings(awacs_json):
    try:
        awacs_radios = json.loads(awacs_json)
    except:
        raise Exception('Invalid JSON. Continuing without removing old channel texts...')
    
    radionames = []

    for radio in awacs_radios:
        if radio['name'] != 'SATCOM':
            radionames.append(radio['name'])
        
    return radionames

def modify_awacs_radios(awacs_radios, new_profile):
    for i in range(10):
        awacs_radios[i + 1]['name'] = new_profile['radios'][i]['name']
        
        if type(new_profile['radios'][i]['default-freq']) == str:
            channel_name = new_profile['radios'][i]['default-freq']
            try:
                awacs_radios[i + 1]['freq'] = new_profile['channels'][channel_name]['freq'] * 1000000
            except KeyError:
                error = f"Radio {new_profile['radios'][i]['name']}: Channel {channel_name} does not exist."
                print(error)
                raise Exception(error)
        elif type(new_profile['radios'][i]['default-freq']) == float or type(new_profile['radios'][i]['default-freq']) == int:
            awacs_radios[i + 1]['freq'] = new_profile['radios'][i]['default-freq'] * 1000000
        
        if new_profile['radios'][i]['band'] == 'all':
            awacs_radios[i + 1]['freqMin'] = 1 * 1000000
            awacs_radios[i + 1]['freqMax'] = 400 * 1000000
        elif new_profile['radios'][i]['band'] == 'HF':
            awacs_radios[i + 1]['freqMin'] = 1 * 1000000
            awacs_radios[i + 1]['freqMax'] = 100 * 1000000
        elif new_profile['radios'][i]['band'] == 'VHF':
            awacs_radios[i + 1]['freqMin'] = 100 * 1000000
            awacs_radios[i + 1]['freqMax'] = 200 * 1000000
        elif new_profile['radios'][i]['band'] == 'UHF':
            awacs_radios[i + 1]['freqMin'] = 200 * 1000000
            awacs_radios[i + 1]['freqMax'] = 400 * 1000000

        if new_profile['radios'][i]['modulation'] == 'AM':
            awacs_radios[i+1]['modulation'] = 0
        elif new_profile['radios'][i]['modulation'] == 'FM':
            awacs_radios[i+1]['modulation'] = 1

def generate_channel_text(radio, new_profile):
    channel_text = ''
    for channel_item in radio['channels']:
        if channel_item.lower() == 'all':
            for channel in new_profile['channels']:
                if radio['modulation'] == new_profile['channels'][channel]['modulation']:
                    channel_text += (channel + '|' + str(new_profile['channels'][channel]['freq']) + '\n')
        
        elif channel_item.upper() == 'HF':
            for channel in new_profile['channels']:
                if 1 <= new_profile['channels'][channel]['freq'] <= 100 and radio['modulation'] == new_profile['channels'][channel]['modulation']:
                    channel_text += (channel + '|' + str(new_profile['channels'][channel]['freq']) + '\n')
        
        elif channel_item.upper() == 'VHF':
            for channel in new_profile['channels']:
                if 100 <= new_profile['channels'][channel]['freq'] <= 200 and radio['modulation'] == new_profile['channels'][channel]['modulation']:
                    channel_text += (channel + '|' + str(new_profile['channels'][channel]['freq']) + '\n')
        
        elif channel_item.upper() == 'UHF':
            for channel in new_profile['channels']:
                if 200 <= new_profile['channels'][channel]['freq'] <= 400 and radio['modulation'] == new_profile['channels'][channel]['modulation']:
                    channel_text += (channel + '|' + str(new_profile['channels'][channel]['freq']) + '\n')

        else:
            try:
                channel_text += channel_item + '|' + str(new_profile['channels'][channel_item]['freq']) + '\n'
            except:
                raise FinishedWithWarning(f"Radio '{radio['name']}': Channel '{channel_item}' was not found. {channel_item} will not be an available channel.")
    
    return(channel_text)
    

def print_overlay(title, config):
    radionames = []
    for radio in config['radios']:
        radionames.append(radio['name'])
    
    max_length = len(max(radionames, key = len))
    horizontal_divider = '-' * (5 * (len(max(radionames, key = len))) + 6)
    
    print(title)

    print(horizontal_divider)
    print('|', end = '')
    for i in range(5):
        print(radionames[i].center(max_length) + '|', end = '')
    print('\n' + horizontal_divider)
    print('|', end = '')
    for i in range(5):
        print(radionames[i+5].center(max_length) + '|', end = '')
    print('\n' + horizontal_divider + '\n')

class FinishedWithWarning(Exception):
    '''function finished, but something unexpected happened'''

if __name__ == '__main__':
    main()
