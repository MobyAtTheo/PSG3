#!/usr/bin/env python2.7




dict001={}
def retADict(a,b):
    dict001.update({a:b})
    #dict001.update({a:b},{"see":"dee"}) # broken TypeError: 'update expected at most 1 arguments, got 2' // don't do that with update

    return dict001

arr001=[]
print type(arr001)


x=retADict("ABC", "DEF")
x=retADict("1", "2")
x=retADict("3", "4")
x=retADict("5", "6")

for i in dict001.iteritems():
    arr001.append(i)

print "[+] iteritems on dict001"
for i in dict001.iteritems():
    print "    [*] ",i

print "[+] ### output array"
i=0
while ( i < len(arr001)):
    print "    [arr001[",i,"]] ", arr001[i]
    print "    [arr001[",i,"]] ", arr001[i][0]
    print "    [arr001[",i,"]] ", arr001[i][1]
    i = i + 1

### outputdata
print "[+] ### output dict"
print "    [*] x    ",(x)
print "    [*] dict ",(dict001)


print "[+] ### output dict k,v"
for i,j in dict001.iteritems():
   print "    [+]", i, " ", j

print "[+] ### output keys"
for i in dict001.keys():
    print "    [*]", i


print "[+] ### output array"
x=0
while x < len(arr001):
    print "    [+]", "arr001", arr001[x]
    x = x + 1

print "[+] ### output array length"
print "    arr001 length: ", len(arr001)


