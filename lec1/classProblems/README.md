# Class Programs for Lecture 1

Lecture 1 was mainly focused on **“Peak finding”** problem.
Which had two parts : 
- 1D Peak Finder Problem
- 2D Peak Finder Problem

## PEAK FINDER PROBLEM

Find a peak in given set of input if exists where an element is a peak if it is greater then or equal to it's neighbour elements


### Solutions for 1D Peak Finder Problem

- 1 Solution
  - This is a straight forward approach where we are moving from left to right and checking if an element is peak or not.
    
```text
Algorithmic Complexity  
    Θ(n)
```
Input Size 1000000 :

![Alt text](img/peak1D-Time.png?raw=true "Peak 1D Solution")


- 2 Solution
  - This is a more efficient solution using Divide and Conquer Approach.

```text
Algorithmic Complexity  
    Θ(log2(n))
```

Input Size 1000000 :

![Alt text](img/peak1D-DAC-Time.png?raw=true "Peak1D DNC")

