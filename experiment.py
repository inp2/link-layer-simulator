from csma import simmulate
from multiprocessing import Pool, cpu_count
import json

R = [8, 16, 32, 64, 128]
L = 20 
M = 6
T = 500000

with open('exps.out.json', 'wb') as out:
    results = [simmulate(n, R, L, M, T) for n in xrange(5, 100+1)] 
    dump = {}
    for result in results:
        num_nodes, num_utilized, utilization, var, col_count = result 
        dump[num_nodes] = {
            'num_utilized': num_utilized,
            'utilization': utilization,
            'var': var,
            'col_count': col_count 
        }

    out.write(json.dumps(dump, indent=4))

