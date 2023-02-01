import pandas as pd

path = 'prun_output.txt' # <----- paste your MESSY prun output in this file

string = open(path, 'r').read()

string = string.replace('internal time', 'internal time\r')
string = string.replace('}', '}\r')
string = string.replace(')', ')\r')

ls = string.split('\r')

ls_for_pd = []

for i in range(3, len(ls)):
    try:
        sub = ls[i].split(' ')[1:]
        sub[5] = ' '.join(sub[5:])
        sub = sub[:6]
        ls_for_pd.append(sub)
    except:
        pass
    
df = pd.DataFrame(ls_for_pd, columns=['ncalls', 'tottime', 'percall', 'cumtime', 'percall', 'filename:lineno(function)'])

df.to_csv('prun_output.csv', index=False)
