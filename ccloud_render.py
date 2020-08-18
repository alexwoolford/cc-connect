#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader
import configparser

config = configparser.RawConfigParser()
config.read('ccloud.properties')

with open("connect-distributed.j2") as f:
    template_str = f.read()
template = Environment().from_string(template_str)
output = template.render(bootstrap_servers=config.get('ccloud', 'bootstrap_servers'),
                         api_key=config.get('ccloud', 'api_key'),
                         api_secret=config.get('ccloud', 'api_secret'),
                         sr_url=config.get('ccloud', 'sr_url'),
                         sr_key=config.get('ccloud', 'sr_key'),
                         sr_secret=config.get('ccloud', 'sr_secret'))

print(output)
