import subprocess

two_step_authentication = ['oathtool', '--totp', '--base32', 'アカウント追加用のキー']
print(subprocess.check_output(two_step_authentication))