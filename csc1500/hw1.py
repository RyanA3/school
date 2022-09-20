def test(num_conditions, function):
    state = [0] * num_conditions;
    for i in range(2 ** num_conditions):
        for j in range(num_conditions):
            state[j] = int(i / (2 ** j)) % 2;
        print(str(state) + "   " + str(bool(function(state)))[0]);

        

#problem 1
prop1 = lambda v: (v[0] or not v[1]) and (v[1] or not v[2]) and (v[2] or not v[0]) and (v[0] or v[1] or v[2]) and (not v[0] and not v[1] and not v[2]);


test(3, prop1);
