#
# Dario Lorenzoni [2024-12-06]
# single-field PBH + spectator
#

# this setup file defines the single-field PBH model of [1911.00057],
# with the addition of a spectator fields chi, minimally-coupled to gravity
# shorthand: PBHAspec (model PBH-A in [2504.13251])

######################################################################################################################

import sympy as sym
from sympy import cos, sin
import math  # not used here, but has useful constants such math.pi which might be needed in other cases
import sys
from pylab import *
from gravipy import *

######################################################################################################################

# if using an integrated environment we recommend restarting the python console
# after running this script to make sure updates are found

# this path must point to the location of the user's installation of PyTransport:
location = "path/to/PyTransport/PyTransport"

sys.path.append(location)  # we add this location to the python path

import PyTransSetup  # the above commands allows python to find the PyTransSetup module and import it

######################################################################################################################

# define the number of fields and number of parameters, and symbolic arrays for both
nF=2 # 2 fields: phi=f[0], chi=f[1]
nP=7 # 7 parameters:  Mp=p[0],
#                     V0=p[1], M=p[2], A=p[3], sigma=p[4], phid=p[5],
#                     mchi=p[6]

f=sym.symarray('f',nF)
p=sym.symarray('p',nP)

# define shorthands for the fields and the parameters
phi,chi = f
Mp,V0,M,A,sigma,phid,mchi = p

# define the nonminimal couplings of the fields to gravity (and their derivatives)
fphi = 0.5*(Mp**2)

# define the field-space metric (in the Einstein frame)
G= (Mp**2/(2*fphi)) * Matrix( [[ 1 , 0 ],\
                               [ 0 , 1 ]] )

# define the PBH and spectator potentials (in the Jordan frame) and convert them to Einstein frame
VpbhJ = V0 * (phi**2/(phi**2+M**2)) * (1 + A*sym.exp(-(phi-phid)**2/(2*sigma**2)))
VsJ = 0.5*mchi**2*chi**2
V = (Mp**4/(4*fphi**2)) * (VpbhJ + VsJ)

######################################################################################################################

# write this model (potential + metric) into a c file when the script is run
PyTransSetup.potential(V, nF, nP, False, G)
PyTransSetup.compileName3("_PBHAspec", True) # name the model for later use

#EoF