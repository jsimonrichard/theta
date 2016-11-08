import theta as ta

print('##### This is a Demo of cypher #####')

print('Shifting text: "hello world" with key 15436')
print(ta.shift_key('hello world', 15436))

print('Sorting text: "hello world" with key 15436')
print(ta.sort_key('hello world', 15436))

print('Numbering text: "hello world"')
print(ta.str_to_int('hello world'))

input()
