import scipy.stats as st
import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_geometric(self) : 
       for i in range(1,9) : 
           p, mean = i*0.1, 0
           for j in range(100) : 
               myvar = geometric(p) 
               self.assertTrue( myvar>0, "the geometric random variable should always be greater than zero" )
               mean = mean + myvar
           mean = mean / 100
           var = ( 1 - p) / (p*p)
           bar = np.sqrt(var/100)*st.norm.ppf( (0.99 + 1) / 2 )
           self.assertTrue( np.fabs( mean - 1/p )<bar, "your random variable appears to be sampling from the wrong distribution" )
