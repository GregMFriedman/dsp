# Statistics

Read Allen Downey's [Think Stats (second edition)](http://greenteapress.com/thinkstats2/) and [Think Bayes](http://greenteapress.com/thinkbayes/) for getting up to speed with core ideas in statistics and how to approach them programmatically. Both books are completely available online, or you can buy physical copies if you would like.

[<img src="img/think_stats.jpg" title="Think Stats"/>](http://greenteapress.com/thinkstats2/)
[<img src="img/think_bayes.png" title="Think Bayes" style="float: left"; />](http://greenteapress.com/thinkbayes/)  

## Instructions

The ThinkStats book is approximately 200 pages in length.  It is recommended you read the entire book, particularly if you are less familiar with introductory statistical concepts.

The stats exercises have been chosen to introduce/solidify some relevant statistical concepts related to data science.  The solutions for these exercises are available in the ThinkStats repository on GitHub.  You should focus on understanding the statistical concepts, python programming and interpreting the results.  If you are stuck, review the solutions and recode the python in a way that is more understandable to you. 

For example, in the first exercise, the author has already written a function to compute Cohen's D.  You could import it, or you could write your own to practice python and develop a deeper understanding of the concept. 

Complete the following exercises along with the questions in this file. They come from Think Stats, and some can be solved using code provided with the book. The preface of Think Stats [explains](http://greenteapress.com/thinkstats2/html/thinkstats2001.html#toc2) how to use the code.  
*See FAQ at the end of this page for more detailed instructions on cloning the repo.*

Communicate the problem, how you solved it, and the solution, within each of the following [markdown](https://guides.github.com/features/mastering-markdown/) files. (You can include code blocks and images within markdown.)

---

###Required Exercises

###Q1. [Think Stats Chapter 2 Exercise 4](statistics/2-4-cohens_d.md) (Cohen's d)  
Cohen's D is an example of effect size.  Other examples of effect size are:  correlation between two variables, mean difference, regression coefficients and standardized test statistics such as: t, Z, F, etc. In this example, you will compute Cohen's D to quantify (or measure) the difference between two groups of data.   

You will see effect size again and again in results of algorithms that are run in data science.  For instance, in the bootcamp, when you run a regression analysis, you will recognize the t-statistic as an example of effect size.

###Q2. [Think Stats Chapter 3 Exercise 1](statistics/3-1-actual_biased.md) (actual vs. biased)
This problem presents a robust example of actual vs biased data.  As a data scientist, it will be important to examine not only the data that is available, but also the data that may be missing but highly relevant.  You will see how the absence of this relevant data will bias a dataset, its distribution, and ultimately, its statistical interpretation.

###Q3. [Think Stats Chapter 4 Exercise 2](statistics/4-2-random_dist.md) (a random distribution)  
This questions asks you to examine the function that produces random numbers.  Is it really random?  A good way to test that is to examine the pmf and cdf of the list of random numbers and visualize the distribution.  If you're not sure what pmf is, read more about it in Chapter 3.  

###Q4. [Think Stats Chapter 5 Exercise 1](statistics/5-1-blue_men.md) (blue men)
This is a classic example of hypothesis testing using the normal distribution.  The effect size used here is the Z-statistic. 

As a bonus (optional) step, write out the null hypothesis, alternative hypothesis, critical value for testing, and the associated p-value.  You will see p-values in virtually every algorithm output during the bootcamp.  And from this exercise, you will know how the p-value has been computed and its relationship to a distribution.

###Q5. [Think Stats Chapter 7 Exercise 1](statistics/7-1-weight_vs_age.md) (weight vs. age)
In this exercise, you will compute the effect size of correlation.  Correlation measures the relationship of two variables, and data science is about exploring relationships in data.    

###Q6. [Think Stats Chapter 8 Exercise 2](statistics/8-2-sampling_dist.md) (sampling distribution)
In the theoretical world, all data related to an experiment or a scientific problem would be available.  In the real world, some subset of that data is available.  This exercise asks you to take samples from an exponential distribution and examine how the standard error and confidence intervals vary with the sample size.

###Q7. Bayesian (Elvis Presley twin) 

Bayes' Theorem is an important tool in understanding what we really know, given evidence of other information we have, in a quantitative way.  It helps incorporate conditional probabilities into our conclusions.

Elvis Presley had a twin brother who died at birth.  What is the probability that Elvis was an identical twin? Assume we observe the following probabilities in the population: fraternal twin is 1/125 and identical twin is 1/300.  

>> Using Bayes Theorem, we can restate the question as "What is the probability that Elvis was an identical twin **given** we know that he's a twin?"  That yields the following probabilities:

```
pFrat = float(1.0/125.0)
pID = float(1.0/300.0)
pNorm = float(pFrat + pID)
pTwin_Given_ID = float(1)

```
>>With those probabilities defined, we can plug them into the formula:

```
pID_Given_Twin = float((pID * pTwin_Given_ID) / pNorm)
print pID_Given_Twin

```

>>This yields a probability of `0.294117647059`, a little under **30%**.

---

###Q8. Bayesian &amp; Frequentist Comparison  
How do frequentist and Bayesian statistics compare?

>> **Frequentist statistics** is one of a number of possible techniques of formulating generally applicable schemes for making statistical inference: drawing conclusions from sample data by the emphasis on the frequency or proportion of the data. This is the inference framework in which the well-established methodologies of **statistical hypothesis testing** and **confidence intervals** are based.

>>**Bayesian inference** is a method of statistical inference in which Bayes' theorem is used to update the probability for a hypothesis as evidence is acquired.  The critical point about Bayesian inference, then, is that it provides a principled way of **combining new evidence with prior beliefs**, through the application of **Bayes' rule**. This is in **contrast to frequentist inference**, which relies only on the evidence as a whole, with **no reference to prior beliefs**.

>>While "probabilities" are involved in both approaches to inference, the probabilities are associated with different types of things. The result of a **Bayesian approach** can be a probability distribution for what is known about the parameters given the results of the experiment or study. The result of a **frequentist approach** is either a "true or false" conclusion from a significance test or a conclusion in the form that a given sample-derived confidence interval covers the true value: either of these conclusions has a given probability of being correct, where this probability has either a frequency probability interpretation or a pre-experiment interpretation.

>>A real-world example from someone on a forum:

>>Here is how I would explain the basic difference to my grandma:

>>I have misplaced my phone somewhere in the home. I can use the phone locator on the base of the instrument to locate the phone and when I press the phone locator the phone starts beeping.

>>Problem: Which area of my home should I search?

>>Frequentist Reasoning:

>>I can hear the phone beeping. I also have a mental model which helps me identify the area from which the sound is coming from. Therefore, upon hearing the beep, I infer the area of my home I must search to locate the phone.

>>Bayesian Reasoning:

>>I can hear the phone beeping. Now, apart from a mental model which helps me identify the area from which the sound is coming from, I also know the locations where I have misplaced the phone in the past. So, I combine my inferences using the beeps and my prior information about the locations I have misplaced the phone in the past to identify an area I must search to locate the phone.

>>My takeaway is that the frequentist tries to approach results of an experiment as if they were in a vacuum and those results are the only things from which it is OK to draw conclusions.  The Baynesian seeks to quantitatively apply assumptions, that may be updated based on the results, in order to make conclusions.

---

###Optional Exercises

The following exercises are optional, but we highly encourage you to complete them if you have the time.

###Q9. [Think Stats Chapter 6 Exercise 1](statistics/6-1-household_income.md) (household income)
###Q10. [Think Stats Chapter 8 Exercise 3](statistics/8-3-scoring.md) (scoring)
###Q11. [Think Stats Chapter 9 Exercise 2](statistics/9-2-resampling.md) (resampling)

## More Resources

Some people enjoy video content such as Khan Academy's [Probability and Statistics](https://www.khanacademy.org/math/probability) or the much longer and more in-depth Harvard [Statistics 110](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo). You might also be interested in the book [Statistics Done Wrong](http://www.statisticsdonewrong.com/) or a very short [overview](http://schoolofdata.org/handbook/courses/the-math-you-need-to-start/) from School of Data.


## FAQ  

###**Q:  How do I use the code referenced in the book?**  
A:  See step-by-step instructions below.  

**Step 1. Create a directory on your computer where you will do the prework.  Below is an example:**

```
(Mac):      /Users/yourname/ds/metis/prework  
(Windows):  C:/ds/metis/prework
```

**Step 2. cd into the prework directory.  Use GitHub to pull this repo to your computer.**

```
$ git clone https://github.com/AllenDowney/ThinkStats2.git
```

**Step 3.  Put your ipython notebook or python code files in this directory (that way, it can pull the needed dependencies):**

```
(Mac):     /Users/yourname/ds/metis/prework/ThinkStats2/code  
(Windows):  C:/ds/metis/prework/ThinkStats2/code
```




