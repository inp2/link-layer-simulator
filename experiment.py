from csma import simmulate
import json

R = [8, 16, 32, 64, 128]
L = 20 
M = 6
T = 500000

# for a, b, c

#with open('exps.out.json', 'wb') as out:
#    results = [simmulate(n, R, L, M, T) for n in xrange(5, 100+1)] 
#    dump = {}
#    for result in results:
#        num_nodes, num_utilized, utilization, idling, var, col_count = result 
#        dump[num_nodes] = {
#            'num_utilized': num_utilized,
#            'utilization': utilization,
#            'var': var,
#            'col_count': col_count ,
#            'idling': idling
#        }
#
#    out.write(json.dumps(dump, indent=4))

Rs = [
[  1 ,  2 ,  4 ,  8 ,  16 ,   ],
[  2 ,  4 ,  8 ,  16 ,  32 ,   ],
[  4 ,  8 ,  16 ,  32 ,  64 ,   ],
[  8 ,  16 ,  32 ,  64 ,  128 ,   ],
[  16 ,  32 ,  64 ,  128 ,  256 ,   ],
]

#with open('exps.out-2.json', 'wb') as out:
#    dump = {}
#    for R in Rs:
#        dump[R[0]] = {}
#        results = [simmulate(n, R, L, M, T) for n in xrange(5, 100+1)] 
#        for result in results:
#            num_nodes, num_utilized, utilization, idling, var, col_count = result 
#            dump[R[0]][num_nodes] = {
#                'num_utilized': num_utilized,
#                'utilization': utilization,
#                'var': var,
#                'col_count': col_count ,
#                'idling': idling
#            }
#
#    out.write(json.dumps(dump, indent=4))

Ls = [20, 40, 60, 80, 100]

with open('exps.out-3.json', 'wb') as out:
    dump = {}
    for L in Ls:
        dump[L] = {}
        results = [simmulate(n, R, L, M, T) for n in xrange(5, 100+1)] 
        for result in results:
            num_nodes, num_utilized, utilization, idling, var, col_count = result 
            dump[L][num_nodes] = {
                'num_utilized': num_utilized,
                'utilization': utilization,
                'var': var,
                'col_count': col_count ,
                'idling': idling
            }

    out.write(json.dumps(dump, indent=4))
