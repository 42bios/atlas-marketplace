import json,re
from urllib.parse import urlsplit
from pathlib import PurePosixPath
x=json.load(open('catalog.json'));assert x['schemaVersion']==1;assert len(x['packages'])<=200
ids=set()
for p in x['packages']:
 assert re.fullmatch(r'[a-z0-9][a-z0-9-]*',p['id']) and p['id'] not in ids;ids.add(p['id'])
 assert p['type'] in ('connector','device-catalog','icon-pack')
 assert re.fullmatch(r'[a-f0-9]{40}',p['ref'])
 u=urlsplit(p['repository']);assert u.scheme=='https' and u.hostname=='github.com' and not u.username and not u.password and not u.query and len(u.path.strip('/').split('/'))==2
 for key in ('name','description','version','license'):assert isinstance(p[key],str) and p[key]
 for key in ('manifest','preview','documentation'):
  if key in p:assert not PurePosixPath(p[key]).is_absolute() and all(s not in ('','.','..') for s in p[key].split('/'))
print('Validated',len(ids),'commit-pinned extensions.')
