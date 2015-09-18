[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

>>Exercise 8.2 Suppose you draw a sample with size n = 10 from an exponential distribution with λ = 2. Simulate this experiment 1000 times and plot the sampling distribution of the estimate L.Compute the standard error of the estimate and the 90% confidence interval.

>> Below is the code that simulates the above experiment 1000 times first for a sample size of 10, but then after for sample sizes of 25, 50, 100, 500 & 1000.  For each of those simulations, the standard error and the 90% confidence interval are recorded.

```
from __future__ import print_function

import thinkstats2
import thinkplot

import math
import random
import numpy as np
import matplotlib.pyplot as pyplot

from scipy import stats
from estimation import RMSE, MeanError

def SimulateSample(lam=2, n=10, m=1000):
    """Sampling distribution of L as an estimator of exponential parameter.

    lam: parameter of an exponential distribution
    n: sample size
    m: number of iterations
    """
    def VertLine(x, y=1):
        thinkplot.Plot([x, x], [0, y], color='0.8', linewidth=3)

    estimates = []
    for j in range(m):
        xs = np.random.exponential(1.0/lam, n)
        lamhat = 1.0 / np.mean(xs)
        estimates.append(lamhat)

    stderr = RMSE(estimates, lam)
    print('standard error', stderr)

    cdf = thinkstats2.Cdf(estimates)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    print('confidence interval', ci)
    VertLine(ci[0])
    VertLine(ci[1])

    # plot the CDF
    thinkplot.Cdf(cdf)
    thinkplot.Save(root='estimation2',
                   xlabel='estimate',
                   ylabel='CDF',
                   title='Sampling distribution')  
    return stderr
    
x = []
y = []

print('Experiment 3')
for n in [10, 25, 50, 100, 500, 1000]:
    stderr = SimulateSample(n=n)
    x.append(n)
    y.append(stderr)
    print(n, stderr)

```

>>This returns:

```
Experiment 3
standard error 0.829760765922
confidence interval (1.2676575635779865, 3.7082382969504137)
Writing estimation2.pdf
Writing estimation2.eps
10 0.829760765922
standard error 0.427188472956
confidence interval (1.4832534288771413, 2.8452347030168337)
Writing estimation2.pdf
Writing estimation2.eps
25 0.427188472956
standard error 0.292813371758
confidence interval (1.5940412801485089, 2.5722863327606955)
Writing estimation2.pdf
Writing estimation2.eps
50 0.292813371758
standard error 0.199557650527
confidence interval (1.7126792243275946, 2.364068835320615)
Writing estimation2.pdf
Writing estimation2.eps
100 0.199557650527
standard error 0.0906526303433
confidence interval (1.8673409688005425, 2.1690205453490403)
Writing estimation2.pdf
Writing estimation2.eps
500 0.0906526303433
standard error 0.0614173300018
confidence interval (1.8958614987775091, 2.1030759642829122)

```

>> As the sample size goes up, standard error decreases and the confidence interval converges on both sides towards the value of lambda, in this case 2.


>> Repeat the experiment with a few different values of n and make a plot of
standard error versus n. 

>>The code above already repeats the experiment for samples of 10, 25, 50, 100, 500 and 1000.  Below is a code that produces a scatterplot of Standard Error as a function of n:

```
pyplot.scatter(x,y, label="n vs. std. error")
pyplot.show()

```
>>The plot is shown below:

![Standard Error as a Function of n](https://github.com/GregMoney85/dsp/blob/master/img/Standard_Error_N.png)

>>It seems that as the sample size increases, the standard error decays exponentially.
