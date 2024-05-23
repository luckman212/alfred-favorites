#!/usr/bin/env python3

import os
import sys
import json

cfg = os.environ.get('cfg', 'apps.json')
items = []

try:
	with open(cfg, 'r') as f:
		data = json.load(f)
except:
	pass

for a in data:
	items.append({
		'title': a.get('name'),
		'arg': a.get('path'),
		'match': ' '.join(a.get('keywords', [])),
		'icon': { 'type': 'fileicon', 'path': a.get('path') }
	})

items.append({
	'title': 'Edit configuration file',
	'arg': cfg,
	'icon': { 'path': 'cfg.png' }
})

sys.stdout.write(json.dumps(dict(items=items)))
