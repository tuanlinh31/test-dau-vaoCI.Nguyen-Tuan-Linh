n = 181
n2 = n//2
numbers = [80, 98, 83, 92, 1, 38, 37, 54, 58, 89,89,92,92,98]
goodnums = {n-x for x in numbers if x<=n2} & {x for x in numbers if x>n2}
pairs = {(n-x, x) for x in goodnums}

# if not n%2 and (n2, n2) in pairs and numbers.count(n2) == 1:
#    pairs.remove((n2, n2))

print(goodnums)

