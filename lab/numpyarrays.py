# a NumPy array from a list of random numbers
# import numpy as np
# listo=np.array(np.random.randint(1,100,10))
# print(listo)

# # temperature statistics
# import numpy as np
# temperature=[1,2,3,4,5,6,7,8,9,10]
# maximum=np.max(temperature)
# minimum=np.min(temperature)
# average=np.average(temperature)
# #  ? calculating standard deviation
# print(f"the maximum temperature is {maximum} and the minimum temperature is {minimum} and the average is {average}")

# # defining an array with numpy
# import numpy as np 
# a=np.arange(3) ** 2
# b=np.arange(3)** 3
# c=a + b
# print (c)

# calculating the shape of arrays
# import numpy as np
# a=np.arange(5)
# print(np.shape(a))
# b=np.array([np.arange(2),np.arange(2),np.arange(2)])
# print(np.shape(b))

# finding item size
# import numpy as np
# a=np.arange(3,dtype="f8")
# print(a)

# ravel method
# import numpy as np
# a=[[1,2,3,4],[5,6,7,8]]
# print(np.ravel(a))

# shape method
# import numpy as np
# a=[[1,2,3,4],[5,6,7,8]]
# print(np.transpose(a))

# resize method
# import numpy as np
# a=[[1,2,3,4],[5,6,7,8]]
# print(np.resize(a,(2,3)))

# stacking
# import numpy as np
# a=np.arange(9).reshape(3,3)
# b=2*a
# # horizontal stacking
# print(np.hstack((a,b)))
# # vertical stacking
# print(np.vstack((a,b)))
# # concantenating
# print(np.concatenate((a,b)))
# # depth stacking
# print(np.dstack((a,b)))
# # row stacking
# print(np.row_stack((a,b)))

# # splitting arrays
# import numpy as np
# a=np.arange(9).reshape(3,3)
# b=2*a
# horizontal splitting
# print(np.hsplit(a,3))
# # vertical splitting
# print(np.vsplit(a,3))

# # finding number of dimensions
# print(np.ndim(a))

# # finding number of elements
# print(np.size(a))

# finding dtype
# print(np.dtype(str))

# to list method
# import numpy as np
# a=np.arange(5)
# print(a.tolist())

# flat method
# import numpy as np
# a=np.arange(5)
# print(a.flat)
# for value in a.flat:
#     print(value)
    
# flatten method
# print(a.flatten())

# # creating views and copies
# import numpy as np
# a=np.arange(5)
# b=a.view()
# # print(b)
# c=a.copy()
# b[0]=3
# # print(a)
# # print(b)
# # print(c)
# c[3]=5
# print(a)

# # fancy indexing
# import numpy as np
# a=np.array([[1,2,3],[4,5,6]])
# rows=np.array([0,1])
# cols=np.array([2])
# b=a[rows,cols]
# print(b)

import pandas as pd
