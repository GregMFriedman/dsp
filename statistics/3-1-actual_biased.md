[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> Exercise 3.1: Something like the class size paradox appears if you survey
children and ask how many children are in their family. Families with many
children are more likely to appear in your sample, and families with no
children have no chance to be in the sample.

>>Use the NSFG respondent variable NUMKDHH to construct the actual distribution
for the number of children under 18 in the household.

>>The code for this part is:

```
import chap01soln
import thinkstats2
import thinkplot

resp = chap01soln.ReadFemResp()
pmf = thinkstats2.Pmf(resp.numkdhh)

```
>>Printing the pmf, we get a dictionary of values & probablities:

```
Pmf({0: 0.46617820227659301, 1: 0.21405207379301322, 2: 0.19625801386889966, 3: 0.087138558157791451, 4: 0.025644380478869556, 5: 0.010728771424833181})
```

>>Now compute the biased distribution we would see if we surveyed the children
and asked them how many children under 18 (including themselves)
are in their household.

>>The code:

```
def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)
    
    for x, p in pmf.Items(): #multiply each probability by children reporting
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize() #normalize the probability so the total = 1
    return new_pmf

biased = BiasPmf(pmf, label='biased')

```

>>The new probabilities are shown in the following dictionary:

```
({0: 0.0, 1: 0.20899335717935616, 2: 0.38323965252938175, 3: 0.25523760858456823, 4: 0.10015329586101177, 5: 0.052376085845682166})

```

>>Obviously, the households with no kids had no kids to be surveyed.  The 0-child household, which was the mode of the actual data, is now completely unrepresented in the biased data.  That change will account for the large difference between the 2 data sets later on, when the means are calculated.

>>Plot the actual and biased distributions, and compute their means.

>>The code:

```

#Plots
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Show()

#Means
actual_mean = pmf.Mean()
biased_mean = biased.Mean()

```
>>The output of the plots is:

![Biased vs. Plots](/Users/gregoryfriedman/dsp/img/Actual_Biased Plots.png)


>>Finally the means:

```

Actual Mean Number of Children: 1.02420515504
Biased Mean Number of Children: 2.40367910066

```

>>So as mentioned earlier, without counting the vast number of 0-child households, the mean household appears to be more than double the size it actually is.  One other note is that the other reason for the discrepancy is that each household child is counted as many times as the children in the household, not just once as would be accurate (except in the case of the one-child household). 

