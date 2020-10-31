import unittest
import inspect
from main import *

class UnitTests(unittest.TestCase) :
    def test_sampleMean(self) :
        self.assertTrue( np.abs( sum(data)/len(data) - sampleMean(data) ) <1e-7, "the sample mean function is not working" )
        
    def test_criticalRange(self) : 
        l = scipy.stats.norm.ppf(0.025,loc=20,scale=2/np.sqrt(200) )
        u = scipy.stats.norm.ppf(0.975,loc=20,scale=2/np.sqrt(200) )
        lll, uuu = criticalRange( 20, 2, len(data) )
        self.assertTrue( np.abs(l-lll)<1e-4, "you have calculated the lower bound of the critical range incorrectly" )
        self.assertTrue( np.abs(u-uuu)<1e-4, "you have calculated the upper bound of the critical range incorrectly" )
        
    def test_hypothesisTest(self) :
        hhh = hypothesisTest( data, 20, 4 ) 
        self.assertTrue( hhh=="there is insufficient evidence to reject the null hypothesis", "your hypothesis test function returns the wrong statement" )
        self.assertTrue( inspect.getsource(hypothesisTest).find("if")>0, "your hypothesis test function does not contain an if statement" )
