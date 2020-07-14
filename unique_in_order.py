# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

def unique_in_order(iterable):
  list = []
  if iterable == "" or iterable == []:
    return list
  else:
    x = iterable[0]
    list.append(iterable[0])
    for i in iterable:
      if i != x:
        list.append(i)
        x = i
    return list

print(unique_in_order([1,2,2,3,3])) #returns [1, 2, 3]