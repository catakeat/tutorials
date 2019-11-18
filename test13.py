L1 = ['a','b','c']
L2 = ['1','2','3','4','5']

res_list = [
    {'grade': 'ok', 'rc': 0},
    {'grade': 'warning', 'rc': 1}
]

sub_dict = {
    'count': 0,
    'results': res_list
}
my_dict={}

for l1 in L1:
    my_dict[l1]={}
    for l2 in L2:
        my_dict[l1][l2]=sub_dict

print(my_dict)