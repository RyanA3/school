#Propositional Logic
#Ryan A
#9-13-2022
#CSC1500

#problem 1
"""
#Truth table printer
header3 = "p,q,r   p,q,r"
header2 = "p,q        p,q"
def p3(p, q, r):
    print(str(p) + ',' + str(q) + ',' + str(r) + '   ' + str(bool(p))[0] + ',' + str(bool(q))[0] + ',' + str(bool(r))[0]);
def p2(p, q):
    print(str(bin(p)) + ',' + str(bin(q)) + '   ' + str(bool(p))[0] + ',' + str(bool(p))[0]);


#Tests two-variable lambda functions
def test3(function):
    print(header3);
    for p in range(2):
        for q in range(2):
            p3(p, q, function(p, q));
            
#Tests single-variable lambda functions
def test2(function):
    print(header2);
    for p in range(2):
        p2(p, function(p));

#bit-wise AND
band = lambda p, q: p & q;

#bit-wise OR
bor = lambda p, q: p | q;

#bit-wise XOR
bxor = lambda p, q: p ^ q;

#bit-wise NOT inversion
bnot = lambda p: ~p;

print('AND');
test3(band);
print('\n\nOR');
test3(bor);
print('\n\nXOR');
test3(bxor);
print('\n\ninversion');
test2(bnot);
"""

#problem 2
"""
print(header3);
for i in range(8):
    p = int(i / 4) % 2;
    q = int(i / 2) % 2;
    r = int(i / 1) % 2;
    print(p, q, r, " ", str(not p)[0], str(not q)[0], str(not r)[0]);
"""

#problem 3
"""
file = open("results2.txt", "r");
results = [];
for i in file:
    results.append(int(i));
print(results);

for x in results:
    for y in [1111]:
        print(x, y, "Result: ", x|y);
file.close();
"""

#problem 4
func = lambda p, q, r: (p or not q) and (q or not r) and (r or not p);
print('p,q,r, (p ∨ ¬q) ∧ (q ∨ ¬r) ∧(r ∨ ¬p)');
for i in range(8):
    p = int(i / 4) % 2;
    q = int(i / 2) % 2;
    r = int(i / 1) % 2;
    print(p, q, r, str(bool(func(p,q,r)))[0]);
