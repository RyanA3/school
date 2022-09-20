def test(num_conditions, functions):
    print(("-" * (3 * num_conditions)) + ("-" * (4 * len(functions))));
    state = [0] * num_conditions;
    for i in range(2 ** num_conditions):
        for j in range(num_conditions):
            state[j] = int(i / (2 ** j)) % 2;
        out = str(state);
        for function in functions:
            out += "   " + str(bool(function(state)))[0];
        print(out);

        

#problem 1
prop1 = lambda v: (v[0] or not v[1]) and (v[1] or not v[2]) and (v[2] or not v[0]) and (v[0] or v[1] or v[2]) and (not v[0] and not v[1] and not v[2]);
test(3, [prop1]);

#problem 2
prop2 = lambda v: v[0] or (v[1] and v[2]);
prop3 = lambda v: (v[0] or v[1]) and (v[0] or v[2]);
test(3, [prop2, prop3])
