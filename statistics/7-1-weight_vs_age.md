[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

>> Exercise 7.1 Using data from the NSFG, make a scatter plot of birth weight
versus mother’s age. 

>>The following code creates and saves a copy of the Scatterplot shown below:

```
from __future__ import print_function
import sys
import numpy as np
import math

import first
import thinkplot
import thinkstats2

def ScatterPlot(ages, weights, alpha=1.0):
    """Make a scatter plot and save it.

    ages: sequence of float
    weights: sequence of float
    alpha: float
    """
    thinkplot.Scatter(ages, weights, alpha=alpha)
    thinkplot.Config(xlabel='age (years)',
                     ylabel='weight (lbs)',
                     xlim=[10, 45],
                     ylim=[0, 15],
                     legend=False)

live, firsts, others = first.MakeFrames()
live = live.dropna(subset=['agepreg', 'totalwgt_lb'])

ScatterPlot(ages, weights, alpha=0.1)
thinkplot.Save(root='chap07scatter1', 
               legend=False,
               formats=['jpg'])

```

![Birth Weight vs. Mother's Age Scatterplot](https://github.com/GregMoney85/dsp/blob/master/img/chap07scatter1.jpg)

>>One can see by the horizontal cloudlike shape that there is practically no correlation between the age of the mother and the birthweight of the child.  This will be confirmed when we calculate the Pearson & Spearman correlations below.

>>Plot percentiles of birth weight versus mother’s age.

>>The code for plotting and saving this graph is below, follwed by the graph it creates:

```
def BinnedPercentiles(df):
    """Bin the data by age and plot percentiles of weight for each bin.

    df: DataFrame
    """
    bins = np.arange(10, 48, 3)
    indices = np.digitize(df.agepreg, bins)
    groups = df.groupby(indices)

    ages = [group.agepreg.mean() for i, group in groups][1:-1]
    cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups][1:-1]

    thinkplot.PrePlot(3)
    for percent in [75, 50, 25]:
        weights = [cdf.Percentile(percent) for cdf in cdfs]
        label = '%dth' % percent
        thinkplot.Plot(ages, weights, label=label)

    thinkplot.Save(root='chap07scatter3',
                   formats=['jpg'],
                   xlabel="mother's age (years)",
                   ylabel='birth weight (lbs)')

BinnedPercentiles(live)

```
![Birth Weight vs. Mother's Age Percentiles](https://github.com/GregMoney85/dsp/blob/master/img/chap07scatter3.jpg)


>>Compute Pearson’s and Spearman’s correlations. How would you characterize the relationship between these variables?

>>The code:

```
print('thinkstats2 Corr', thinkstats2.Corr(ages, weights))
print('thinkstats2 SpearmanCorr', 
      thinkstats2.SpearmanCorr(ages, weights))
```

>>Yields:

```
thinkstats2 Corr 0.0688339703541
thinkstats2 SpearmanCorr 0.0946100410966

```
>> Pearson's correlation is approximately 0.069 and Spearman's is about 0.095.  Firstly, this confirms that there is a very weak correlation.  Secondly, because there's a disparity between them, then according to the text, the data is affected by the presences of outliers or there may be a non-linear relationship.

>>Looking at the graph of the percentiles, birthweight does seem to increase with the age of the mother at least until her early 20s.  Perhaps because a 15 year-old mother is usually smaller than a mother in her 20s.  However, once past the early 20s, there is practically no correlation between the two variables at all.


