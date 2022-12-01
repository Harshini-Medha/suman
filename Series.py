import numpy as np
Series_A=([10,20,30,40,50])
Series_B=([40,50,60,70,80])
intersect=pd.Series(np.intersect1d(Series_A,Series_B))
print("the common items are")
print(intersect)
