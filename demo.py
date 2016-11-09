import theta as ta

print('##### This is a Demo of cypher #####')

shift = ta.shift_key.encode('hello world', 15436)
sort = ta.sort_key.encode('hello world', 15436)

print('Shifting text: "hello world" with key 15436')
print(shift)
print('Decode')
print(ta.shift_key.decode(shift, 15436))
print()

print('Sorting text: "hello world" with key 15436')
print(sort)
print('Decode')
print(ta.sort_key.decode(sort, 15436))
print()

print('Numbering text: "hello world"')
print(ta.str_to_int('hello world'))

input()
