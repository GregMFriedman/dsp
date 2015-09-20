[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

>> Compute the median, mean, skewness and Pearson’s skewness of the resulting sample. What fraction of households reports a taxable income below the mean? How do the results depend on the assumed upper bound?

>> The code to generate the answers is as follows:

```
import numpy as np

import hinc
import hinc2

import thinkplot
import thinkstats2
import density

df = hinc.ReadData()

def PearsonStats(df, log_upper):
    ls = hinc2.InterpolateSample(df, log_upper)
    log_cdf = thinkstats2.Cdf(ls)
    sample = np.power(10, ls)
    mean, median = density.Summarize(sample)

    cdf = thinkstats2.Cdf(sample)
    print "Percent below Mean: " + str(100*cdf[mean]) + "%"
    
    pdf = thinkstats2.EstimatedPdf(sample)
    thinkplot.Pdf(pdf)
    thinkplot.Show(xlabel='household income',
                   ylabel='PDF')    

#Test different upper bounds
for x in [4, 6, 7, 10]:
    PearsonStats(df, x)

```

>> This generates the following values for upperbounds of 10 to the 4th, 6th, 7th & 10th:

```
mean 63190.3016873
std 50413.2749016
median 49844.7976054
skewness 1.22249363582
pearson skewness 0.794166066853
Percent below Mean: 60.2451452743%
 
mean 74278.7075312
std 93946.9299635
median 51226.4544789
skewness 4.94992024443
pearson skewness 0.736125801914
Percent below Mean: 66.0005879567%
 
mean 124267.397222
std 559608.501374
median 51226.4544789
skewness 11.6036902675
pearson skewness 0.391564509277
Percent below Mean: 85.6563066521%
 
mean 22526983.8667
std 334705384.9
median 51226.4544789
skewness 19.8424289781
pearson skewness 0.201452606617
Percent below Mean: 98.6330007023%

```
>>As one increases the upper bound, the skewness clearly increases.  Since the Pearson Skewness varies inversely as the cube of the standard deviation, increasing the upper bound actually shrinks it.  For that reason, it's most informative to look at the percent below the mean, which is nearly 100% for 10 to the 10th (which is the order of magnitude of the current richest person alive, I believe).  However, of course the generated distributions are much farther from the truth once the upper bound is that high, which is why the author chooses the more reflective 10^6.
