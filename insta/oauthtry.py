import subprocess
import configparser
import re

config_txt = configparser.ConfigParser()
config_txt_path = "config.txt"

with open(config_txt_path, encoding='utf-8') as fp:
    config_txt.read_file(fp)

    read_default = config_txt['Login']
    oauth = read_default.get('oauth')

two_step_authentication = ['oathtool', '--totp', '--base32', oauth]
SecondLoginPass = re.findall(r'\d+', subprocess.check_output(two_step_authentication).decode('utf-8'))
print(subprocess.check_output(two_step_authentication))
print(SecondLoginPass[0])

