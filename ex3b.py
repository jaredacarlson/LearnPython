#Calculate the value of exp
#import numpy as np
#np.exp(1)

#Calculate Markdown Elasticity
print "Markdown Elasticity"
Beta = 0.3
MarkdownLift = 2
PriceReg = 6
PriceMD = 3
print (Beta + MarkdownLift/PriceReg)*PriceMD
