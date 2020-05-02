
# Multi-Armed Bandit
Multi-armed bandit as a service

Epsilon-greedy
=======

## General description
 
This project is an implementation of a number of MAB algorithms such as [epsison-greedy](https://en.wikipedia.org/wiki/Multi-armed_bandit).

## Use cases

There are a number of use cases.  For example, if you have a number of different version of a landing page and you want to automatically find out what version generates the maximun leads, you can use this optimization service.  Essentially, we are running reinforecement learning where we explore and expoit different landing page and quickly find the optimal version. After the algorithm converges, we server with high likelihood the landing page version that makes the maximum lead for your business. 

## Requirements

You should setup the conda environment (i.e. `mab`) using the environment.yml file:

`conda env create -f environment.yml`

## Activate conda environment:

`conda activate mab`

(Run `unset PYTHONPATH` on Mac OS)

## start HTTP server

`python -m src.server -o models`

# To deactivate the conda environment:

`conda deactivate`
