import os
mem=str(os.popen('free -t -m').readlines())
"""
Get a whole line of memory output, it will be something like below
['             total       used       free     shared    buffers     cached\n', 
'Mem:           925        591        334         14         30        355\n', 
'-/+ buffers/cache:        205        719\n', 
'Swap:           99          0         99\n', 
'Total:        1025        591        434\n']
 So, we need total memory, usage and free memory.
 We should find the index of capital T which is unique at this string
"""
T_ind=mem.index('T')
"""
Than, we can recreate the string with this information. After T we have,
"Total:        " which has 14 characters, so we can start from index of T +14
and last 4 characters are also not necessary.
We can create a new sub-string using this information
"""
mem_G=mem[T_ind+14:-4]
"""
The result will be like
1025        603        422
we need to find first index of the first space, and we can start our substring
from from 0 to this index number, this will give us the string of total memory
"""
S1_ind=mem_G.index(' ')
mem_T=mem_G[0:S1_ind]
"""
Similarly we will create a new sub-string, which will start at the second value. 
The resulting string will be like
603        422
Again, we should find the index of first space and than the 
take the Used Memory and Free memory.
"""
mem_G1=mem_G[S1_ind+8:]
S2_ind=mem_G1.index(' ')
mem_U=mem_G1[0:S2_ind]

mem_F=mem_G1[S2_ind+8:]
print 'Summary = ' + mem_G
print 'Total Memory = ' + mem_T +' MB'
print 'Used Memory = ' + mem_U +' MB'
print 'Free Memory = ' + mem_F +' MB'
