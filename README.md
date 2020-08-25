# OpenSAFELY cohort extractor demo

This repo gives an example of how the [OpenSAFELY cohort extractor](https://github.com/opensafely/cohort-extractor/) works.

It contains [a very simple study definition](https://github.com/opensafely/cohort-extractor-demo/blob/master/analysis/study_definition.py).

## Things to read:

* [An introduction to OpenSAFELY platform](https://github.com/opensafely/documentation/blob/master/Introducing%20OpenSAFELY.md)
* [Walkthrough instructions for using the platform for epidemiological research](https://github.com/opensafely/documentation/blob/master/Onboarding%20analysts.md)
* [Instructions for writing a study definition](https://github.com/opensafely/documentation/blob/master/study_definition.md)
* [Cohort extractor source code](https://github.com/opensafely/cohort-extractor/)
* [A more comprehensive study definition](https://github.com/opensafely/flu-vacc-research/blob/master/analysis/study_definition_flu_vaccine.py)

## About the OpenSAFELY framework

The OpenSAFELY framework is a new secure analytics platform for
electronic health records research in the NHS.

Instead of requesting access for slices of patient data and
transporting them elsewhere for analysis, the framework supports
developing analytics against dummy data, and then running against the
real data *within the same infrastructure that the data is stored*.
Read more at [OpenSAFELY.org](https://opensafely.org).

The framework is under fast, active development to support rapid
analytics relating to COVID19; we're currently seeking funding to make
it easier for outside collaborators to work with our system.  You can
read our current roadmap [here](ROADMAP.md).
