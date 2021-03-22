# user_id=('user1','user2','user3')
# names=('rajveer','karan','mohit')
# l_name=['rawat','chouchan','singhal']
# print(list(zip(user_id,names,l_name)))
# print(tuple(zip(user_id,names,l_name)))
# print(dict(zip(user_id,names))) #ValueError: dictionary update sequence element #0 has length 3; 2 is required



def func(*l):
    l1,l2=(l)
    print(l1)
    print(l2) 
lists=[(1,2),(3,4),(5,6)]   
func(lists)
