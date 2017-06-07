# sinxcosy
# Bayesian Neural Network Example (Regression)
A simple demo of regression with Radford Neal's fbm package

Introduction
------------
The file doc/BNN.pdf gives a terse introduction to the package by Radford 
Neal. The package can be found at:

	http://www.cs.toronto.edu/~radford/software-online.html

Note, this was the package used in one of the three analyses that yielded the 
first evidence of single top production and subsequent discovery by Dzero.

Simple 2-D regression example
-----------------------------
In this example, we generate data (x, y, z) from the function

	z = f(x, y) = sin(x)*cos(y)

using the function gendata.py (in bin) and fit a Bayesian neural network (BNN)
to these data. A BNN is simply an average over an ensemble of networks. Here
we average over the last 100 networks sampled from a posterior probability
defined over the neural network (NN) parameter space. In this example, we have
2 inputs x, y and one output z. The NN is defined by 2 inputs, 10 hidden nodes,
and 1 output node. 

In principle, a BNN can model any d-dimensional function

	y = f(x1, x2, ...xd)

though his may take a few hours for large d (~10) since the training is done
using MCMC.

The program plot.py compares the true function with its BNN approximation. 


I. 	COMPILING Neal's package

	cd fbm.2004-11-10
	chmod +x make-clean make-all
	./make-clean
	./make-all

II. 	SETUP (assuming a Bash shell)

	Edit setup.sh to include ROOT in your path, if not already present

	source setup.sh

	This makes the executables in Neal's package and the Python scripts
	in the bin directory available.

III.	PREPARING training data

	gendata.py	(creates sinxcosy.dat and sinxcosy.var)

	The do

	       mktrain.py -mr -H10 -N2000 -I200 sinxcosy

	       to create sinxcosy.sh

VI.	TRAINING (using MCMC based on Hamiltonian dynamics)

		source sinxcosy.sh&


	Test training periodically using

		net-display -h sinxcosy.bin


	This will give the index number (training cycle). In this example, we
	train for 200 cycles, where each cycle consists of 20 steps each comprising
	100 deterministic steps (through the NN parameter space) followed by a 
	random change of direction; that is, each cycle comprises 2000 steps,
	punctuated with 20 random changes of direction in the NN parameter space.

 	The results of the training are contained in the binary file
	sinxcosy.bin.

V.	TESTING

	Create a self-contained C++ function using

		netwrite.py -n 100 sinxcosy.bin


	This creates the function 

		sinxcosy.cpp

	that computes

		z = (1/100) sum_i=1^100 NN(x, y, w_i)

	where w_i denotes the 41 parameters of the ith NN in the ensemble of 50.

	Then plot result using

		python plot.py


	Try to guess which plot is the true function and which is the 
	approximation! 


	Have fun!

