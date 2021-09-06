s3 = set('wow thats cool')
print(s3)

s1 = set('abcde')
s1.add('hello')
print(s1)

s1 = set('abcde')
s1.remove('d')
print(s1)

s1 = set('abcdef')
s1.discard('f')
print(s1)

s1 = set('abcdef')
s1.remove('f')
print(s1)

alpha_set = set('abcde')
name = set('bad boy')
print(alpha_set.union(name))

num_set = {0,1,2,3,4,5,6,7,8,9,10}
date_num = set([1,9,4,8])
print(num_set.union(date_num))

alpha_set = set('abcde')
name = set('bad boy')
print(alpha_set.intersection(name))

num_set = {0,1,2,3,4,5,6,7,8,9,10}
date_num = set([1,9,4,8])
print(num_set.intersection(date_num))

alpha_set = set('abcde')
name = set('bad boy')
print(alpha_set.difference(name))

num_set = {0,1,2,3,4,5,6,7,8,9,10}
date_num = set([1,9,4,8])
print(num_set.difference(date_num))