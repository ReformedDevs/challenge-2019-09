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
CORRECT = '433494437'

results = []
wrongs = []
for d in TEST_DIRS:
    if os.path.isfile(os.path.join(d, 'build_test.sh')):
        os.system('cd {} && bash build_test.sh'.format(d))

    if os.path.isfile(os.path.join(d, 'run_test.sh')):
        temps = []
        temps_wrong = []
        for i in range(5):
            result = os.popen('cd {} && bash run_test.sh'.format(d)).read()
            if isinstance(result, string_types) and ',' in result:
                items = result.replace('\n', '').split(',')
                temp = {
                    'user': items[0].strip(),
                    'lang': items[1].strip(),
                    'solution': items[2].strip(),
                    'time': float(items[3].strip()),
                    'notes': items[4]
                }
                if temp['solution'] == CORRECT:
                    temps.append(temp)
                else:
                    temps_wrong.append(temp)
        if temps:
            results.append({
                'user': temps[0]['user'],
                'lang': temps[0]['lang'],
                'solution': temps[0]['solution'],
                'time': sum(x['time'] for x in temps) / len(temps),
                'notes': temps[0]['notes']
            })
        if temps_wrong:
            wrongs.append({
                'user': temps_wrong[0]['user'],
                'lang': temps_wrong[0]['lang'],
                'solutions': ', '.join([t['solution'] for t in temps_wrong])
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

        if wrongs:
            wrongs = '\n'.join([
                '* {}, {}\n  * `{}`'.format(x['user'], x['lang'], x['solutions'])
                for x in wrongs
            ])
            wrongs = ('\n\n# Oops\n\nThe following were submitted but '
                      'contained wrong answers:\n{}'.format(wrongs))
            table += wrongs

        with open(README, 'w') as f:
            f.write(readme + table)
