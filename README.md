# Bayesian Sports Models

A Python implementation of the concepts and models from Andrew Mack's book "Bayesian Sports Models in R".

## Overview

This repository contains Python implementations of the Bayesian sports modeling techniques presented in Andrew Mack's book "Bayesian Sports Models in R". While the original book uses R, these projects demonstrate the same statistical concepts and modeling approaches using Python.

## About the Book

"Bayesian Sports Models in R" by Andrew Mack provides a comprehensive introduction to applying Bayesian statistics to sports analytics and betting. This repository serves as a Python companion to the book's concepts.

## Key Differences from the Book

- **Language**: Python instead of R
- **Libraries**: Uses Python equivalents (pymc, arviz, pandas, numpy, scipy)
- **Implementation**: Modern Python workflows and best practices

## Project Structure

- **Chapter 3**: Probability Rules and Fundamentals
- **Chapter 4**: Basic Probability Applications
- **Chapter 5**: Probability Distributions
- **Chapter 6**: Conjugate Prior Models
- **Chapter 7**: Beta-Binomial and Gamma-Poisson Models
- **Chapter 8**: Interval Estimation and Comparison

## Getting Started

1. Clone this repository
2. Install required Python packages: `pip install pymc arviz pandas numpy scipy matplotlib seaborn`
3. Navigate to specific chapter folders for detailed documentation

## Recent Updates

### Chapter 8: Interval Estimation and Comparison
- **beta-binomial-intervals.py**: Compares Bayesian credible intervals, frequentist confidence intervals, and true ranges for win rate estimation
- **gamma-poisson-intervals.py**: Compares Bayesian credible intervals and frequentist confidence intervals for goal scoring rate estimation
- Both files include custom visualization with black interval bars, blue dots for minimums, and red dots for maximums

## Technologies Used

- **Bayesian Inference**: PyMC, ArviZ
- **Data Manipulation**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Statistical Analysis**: scipy, statsmodels

## Reference

Mack, Andrew. "Bayesian Sports Models in R." [Book reference details]
