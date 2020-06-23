'''
Test different yaml loading
'''
import yaml

config = 'config.yaml'

with open(config,'rt') as yin:
    configyaml = yin.read()

config = yaml.safe_load(configyaml)
