# Test Driven Ranges

This exercise extends the [Battery Monitoring] use-case.

The charging current varies during the process of charging.
We need to capture the range of current measurements -
what range of currents are most often encountered while charging.

> **DO NOT** jump into implementation! Read the example and the starting task below.

## Example

### Input

Consider a set of periodic current samples from a charging session to be:
`3, 3, 5, 4, 10, 11, 12`

### Functionality

The continuous ranges in there are: `3,4,5` and `10,11,12`.

The task is to detect the ranges and
output the number of readings in each range.

In this example,

- the `3-5` range has `4` readings
- the `10-12` range has `3` readings.

### Output

The expected output would be:

```
Range, Readings
3-5, 4
10-12, 3
```

## Tasks

Start test-driven development:

1. Establish quality parameters for your project: What is the maximum complexity you would allow? 
   How much duplication would you consider unacceptable? 
   What is the coverage you'll aim for?
   Adapt/adopt/extend the `yml` files from one of your workflow folders.

1. Write the smallest possible failing test.

1. Write the minimum amount of code that'll make it pass.

1. Write the next failing test.

## Task Implementation Details

1. I have set the maximum cyclomatic complexity to be 4 to allow for slightly more convoluted control flows than
   previous assignments.
   I have kept the duplication rules as is from the other assignments since I considered them a fair check for copy
   pasted code.
   100% coverage or nothing :D

1. My smallest possible failing test is to test that the code returns an error code for empty input.

1. Smallest possible passing function returns an error code for empty input.

1. Another failing test is to test that all the inputs are of int type.
