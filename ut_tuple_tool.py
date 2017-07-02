import tuple_tool as tt

# Convert string to a tuple
my_str= "bell"
tuple1 = tt.make(my_str)

#Merge to two tupples into one
tuple2 = ('apple' , 'cell') # Make a tubple
new_tuple = tt.merge(tuple1 , tuple2)
print "tuple1 is" , tuple1
print "tuple2 is" , tuple2
print "merged tuple1 + tuple2 ::" , new_tuple
print "pick new_tuple[0] :: " , new_tuple[0]

#Sort the taple
sorted_tuple = tt.sort(new_tuple)
print "sorted tuple ::" , sorted_tuple , "  <= basically, can not sort the taple because of taple is imutable."


#Split taple
splited = tt.split(sorted_tuple , 1)
print "split by index (1) : First: " , splited[0]
print "split by index (1) : After: " , splited[1]

# Get top item as object
top = tt.get_top(sorted_tuple)
print "top index: " , top
