# Sets in python
# A set is an unordered collection of unique elements.
s={}
s1=set()
s2={10,10,20,20}
print(type(s))
print(type(s1))
print(s2)
s3={2,4,6,10,16,20}
print(f"Union is {s2.union(s3)}")
print(s2,s3)
s2.update(s3)
print(s2,s3)
print(f"Intersection is {s2.intersection(s3)}")
print(s2,s3)
s3.intersection_update(s2)
s2.symmetric_difference_update(s3)
print(s2)
s3.difference_update(s2)
print(s3)

