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
        temps = []
        for i in range(5):
            result = os.popen('cd {} && bash run_test.sh'.format(d)).read()
            if isinstance(result, string_types) and ',' in result:
                items = result.replace('\n', '').split(',')
                temps.append({
                    'user': items[0].strip(),
                    'lang': items[1].strip(),
                    'solution': items[2].strip(),
                    'time': float(items[3].strip()),
                    'notes': items[4]
                })
        results.append({
            'user': temps[0]['user'],
            'lang': temps[0]['lang'],
            'solution': temps[0]['solution'],
            'time': sum(x['time'] for x in temps) / 5.0,
            'notes': temps[0]['notes']
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
