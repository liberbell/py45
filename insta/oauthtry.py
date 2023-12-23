import subprocess
import configparser

config_txt = configparser.ConfigParser()
config_txt_path = "config.txt"

with open(config_txt_path, encoding='utf-8') as fp:
    config_txt.read_file(fp)

    read_default = config_txt['Login']
    oauth = read_default.get('oauth')

two_step_authentication = ['oathtool', '--totp', '--base32', oauth]
print(subprocess.check_output(two_step_authentication))