import json
import os
from six import string_types

DIR = os.path.abspath(os.path.dirname(__file__))
TEST_DIRS = [
    os.path.join(DIR, d) for d in os.listdir(DIR)
    if os.path.isdir(os.path.join(DIR, d))
    and '-' in d
    and len(d.split('-')) == 2
]
README = '/tmp/repo/README.md'

results = []
for d in TEST_DIRS:
    if os.path.isfile(os.path.join(d, 'build_test.sh')):
        os.system('cd {} && bash build_test.sh'.format(d))

    if os.path.isfile(os.path.join(d, 'run_test.sh')):
        result = os.popen('cd {} && bash run_test.sh'.format(d)).read()
        if isinstance(result, string_types) and ',' in result:
            items = result.replace('\n', '').split(',')
            results.append({
                'user': items[0],
                'lang': items[1],
                'solution': items[2].replace(' ', ''),
                'time': float(items[3]),
                'notes': items[4]
            })

results = sorted(results, key=lambda k: k['time'])
print(json.dumps(results, indent=2))

if os.path.isfile(README):
    with open(README) as f:
        readme = f.read()

    if readme:
        heading = readme.find('# Leaderboard')
        line = readme.find('\n\n', heading)
        readme = readme[:line + 2]
        table = ('Author | Language | Results | Time | Notes\n'
                 '--- | --- | --- | --- | ---')
        for result in results:
            table += '\n{} | {} | {} | {} | {}'.format(
                result['user'], result['lang'],
                result['solution'], result['time'], result['notes'])

        with open(README, 'w') as f:
            f.write(readme + table)
