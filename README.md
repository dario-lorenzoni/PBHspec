# PBHspec
## Primordial Black Holes from Inflation with a Spectator Field

This repository contains minimal working code that will allow researchers to reproduce the results detailed in our papers [arXiv:2504.13251](https://arxiv.org/abs/2504.13251) ("Letter" in what follows) and [arXiv:TBD](https://arxiv.org/abs/TBD) ("Companion" in what follows).

As detailed in the papers, we used two independent codes written in Python and Mathematica, respectively, to calculate the evolution of the background and of the perturbations. We found excellent agreement between the two codes. 
In Python, we used the publicly available code `PyTransport` (see [arXiv:1609.00379](https://arxiv.org/pdf/1609.00379) and [arXiv:1609.00381](https://arxiv.org/pdf/1609.00381)), which uses the Transport Method to directly compute the time-evolution of correlation functions. The `PyTransport` code is available at [this repository](https://github.com/jronayne/PyTransport).
In Mathematica, we solve the perturbation equations in the form presented in [arXiv:1010.3693](https://arxiv.org/pdf/1010.3693) and, from this, construct the power spectra. We dub this Mathematica solver `PerturbationExpress`.

We provide minimal and self-contained versions of both the Python and Mathematica codes. 

In both the Python and Mathematica codes, all quantities are calculated using the number of e-folds, $N$, as a time coordinate.
The examples provided in this repository are given for the PBH$A$ potential of [arXiv:1911.00057](https://arxiv.org/pdf/1911.00057); the model parameters are the ones used in the Companion paper (see Table I). We show the evolution of the relevant background quantities and the curvature power spectrum for both the single-field reference model (named "PBH$A$-fid" in the Letter, "SF Reference" in the Companion) and the PBHspec model (named "$\chi$-PBH$A$-var" in the Letter, "PBHspec" in the Companion).


**Python**

We provide a PyTransport model setup file that defines the PBHspec model (with PBHspec-$A$ potential), as well as a Jupyter notebook where all the relevant quantities are defined, calculated, and plotted.

Note that a working installation of `PyTranport` is required. We defer further installation and usage information to the instructions presented in the [`PyTransport` repository](https://github.com/jronayne/PyTransport).

Note that the user should explicitly indicate the path tho their local installation of `PyTransport` in both the setup file (line 25) and notebook (line 11 of the first cell).



**Mathematica**

We provide a `PerturbationExpress` notebook where the calculations of the background and of the perturbations are defined, as well as a plotting notebook that produces the figures provided in the `plots` directory for the relevant quantities of the single-field and PBHspec models.  We note that this code is substantially slower than the `PyTransport` equivalent. 

All observables are found to agree between the Python and Mathematica codes.

The authors, Dario Lorenzoni, Sarah Geller, David Kaiser, Evan McDonough.

For any request of information, kindly contact Dario Lorenzoni at lorenzod@myumanitoba.ca .