# Hypothesis testing

Making the connection that you needed to make to solve that problem is momentously important.  If you understand what the central limit theorem tells us about the distribution the sample mean is sampled from it will help you to understand many of the hypothesis testing methods that you are going to learn in this course as they use variants on this idea.  When they are first introduced, you should thus try to understand how the central limit theorem is being used within them.

With all that in mind, I am thus going to start the lying that was promised.  The file data.dat here may or may not contain a set of 200  normal variables with expectation 20 and variance 4.  Your task is to determine if the evidence from the file supports the rejection of this hypothesis.  The method you will use to test this hypothesis is as follows:

1. Your __null hypothesis__ for this test is that the data points are all normal random variables with expectation 20 and variance 4
2. Your __alternative hypothesis__ for the test is that the data points are not all normal random variables with expectation 20 and variance 4.
3. You will calculate the sample mean from the data points.  If the __null hypothesis__ is true you know that this random variable is a sample from a normal random variable and from the central limit theorem you know what distribution this is sampled from.
4. As, under the __null hypothesis__, you know what distribution the sample mean is calculated from you can determine a __critical region__.  In doing this you use the identified probability density function to set up the __critical region__ for a 5% __significance level__.  With the critical range setup in this way, the probability of the sample mean falling within it is 5% if the null hypothesis is true.  

To complete step 4 you will need to calculate percentiles from a normal distribution.  If you were doing this by hand you would look up these percentiles for the standard normal distribution from table 4 in the new Cambridge Statistical Tables.  Python will do look these values up for you.  For example, if you want the 95th percentile (which is not the percentile you will need for this task) you would write:

````
percentile95 = scipy.stats.norm.ppf(0.95)
````

Once you call this function you then need to transform what is output to the percentile for the distribution with the correct expectation and variance.    

5. The final step of the hypothesis test involves determining whether or not the sample mean for the data that you calculated is within this __critical region__ or not.  If it is you then write: _"the null hypothesis is rejected in favour of the alternative."_  If the sample mean is not in the critical region you write _"there is insufficient evidence to reject the null hypothesis."_ 

Your task is to perform the hypothesis test in the manner described above.  I have written some code to read in the data set, to write out the null and alternative hypotheses and to perform the test.  To complete the exercise, however, you will need to write the code in the three functions:

1. `sampleMean` - this function takes a numpy array called `data` as input. It should return the sample mean for the data contained in the array. 
2. `criticalRange` - this function takes three arguments in input.  `mu` is the expecation of a normal random variable, `sigma` is the standard deviation and `N` is the number of samples that have been added together to compute a sample mean.  The function should return two variables `lower` and `upper`.  The variable `lower` should be set so that the probability that a sample mean computed from `N` normal random variables with expectation `mu` and variance `sigma*sigma`  is less than or equal to this value is 2.5%.  The variable `upper`  should be set so that the probability that a sample mean computed from `N` normal random variables with expectation `mu` and variance `sigma*sigma`  is less than or equal to this value is 97.5%. 
3. `hypothesisTest` - this function takes three arguments.  `data` is the list of datapoints from the input file, `mu` is the expectation of the normal random variable that the null hypothesis states we are sampling from,   `sigma` is the standard deviation of the normal random variable that the null hypothesis states we are sampling from.  The `criticalRange` function is called within this function.  To complete the task you must use the values returned from this function as well as the value of the `sampleMea`n to write an if statement that determines whether the statement "_the null hypothesis is rejected in favour of the alternative_" should be returned or whether the statement "_there is insufficient evidence to reject the null hypothesis_" should be returned.  
 
