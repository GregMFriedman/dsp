[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> Exercise 2.4: Using the variable 'totalwgt_lb' investigate whether first babies
are lighter or heavier than others. 

>>Here is the code I used to investigate:

```
from __future__ import print_function
import first
import thinkstats2

live, firsts, others = first.MakeFrames()

def Weight_Comparison(live, firsts, others):
    mean1 = firsts.totalwgt_lb.mean()
    mean2 = others.totalwgt_lb.mean()
    mean0 = live.totalwgt_lb.mean()
    
    var1 = firsts.totalwgt_lb.var()
    var2 = others.totalwgt_lb.var()
    
    print('Means')
    print('First babies: ', mean1)
    print('Others: ', mean2)

    print('Variance')
    print('First babies: ', var1)
    print('Others: ', var2)
    
    print('Difference in lbs: ', mean1 - mean2)
    print('Difference in oz: ', (mean1 - mean2) * 16)
    
    print('Difference relative to mean (%): ', 
          (mean1 - mean2) / mean0 * 100)
          
    d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
    print("Cohen's d: ", d)

Weight_Comparison(live, firsts, others)

```

>>That returned this output:

```

Means
First babies:  7.20109443044
Others:  7.32585561497
Variance
First babies:  2.01802730092
Others:  1.9437810259
Difference in lbs:  -0.124761184535
Difference in oz:  -1.99617895257
Difference relative to mean (%):  -1.71714236784
Cohen's d:  -0.0886729270726

```

>>Compute Cohen’s d to quantify the difference between the groups. 

>>`Cohen's d` came out to be `-0.0886729270726`, which means first babies were found to be lighter than other babies by less than a tenth of a standard deviation.  Since a d-value of `0.2` or less is conventionally defined to be a "small" difference, it does not seem to be a leap of faith to call this difference a small one.

>>How does it compare to the difference in pregnancy length?

>>The difference of `0.089` standard deviations in weight is practically 3 times the difference of `0.29` in prengancy length.  However, both differences are so small that there would be no practical consequences to these results in either case.


