[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> Exercise 5.1 In the BRFSS (see Section 5.4), the distribution of heights is
roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men,
and µ = 163 cm and σ = 7.3 cm for women.

>>First create a normal distribution with a `mean` of 178 and a `sigma` of 7.7:

```
import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale = sigma)
#print dist.mean(), dist.std()

```

>>In order to join Blue Man Group, you have to be male between 5’10” and
6’1” . What percentage of the U.S. male population is in this range?  

>>Having created our distribution above, there are essentially 2 things left to do.  We must first deal with the fact that our inputs are in inches:

```
def to_cm(inches):
    return 2.54*inches

#print to_cm(70), to_cm(73)

```

>>Finally, since the cdf returns the probability of getting a value below the input value, so in order to get the probability of being between two inputs, one just needs to take the difference:

```
tallest = dist.cdf(to_cm(73))
shortest = dist.cdf(to_cm(70))

print tallest, shortest

blue_men = tallest - shortest
print blue_men

```

>>Since 83% of men are below 6'1, but only 49% of men are below 5'10, the remaining 34% must be between 5'10 and 6'1.
