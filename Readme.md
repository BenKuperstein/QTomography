# Quantum Tomography and Bell's Inequality Simulation

This repository contains the supplementary code and documentation for our experiment on simulating quantum tomography and testing Bell's inequality using a classical optical analog system.

## Overview

Experiments in quantum communication and cryptography often require sophisticated and costly experimental setups. To address this challenge, we present an inexpensive and accessible classical optical analog system to demonstrate quantum tomography and test Bell's inequality. Our approach uses a pseudo-random number generator to simulate the quantum randomness of photons, proving sufficient for mimicking quantum phenomena.

## Key Findings

- The density matrices of the measured ensemble align with the results of previous research.
- The Bell parameter \( S \) obtained in this experiment is \( -2.71 \pm 0.18 \), consistent with quantum mechanical predictions and contradicting local hidden variable theories.
- While the results do not represent the true behavior of photons and do not constitute a genuine violation of Bell’s inequality, they serve as an excellent introductory experiment for undergraduate students interested in quantum mechanics.

## Abstract

Experiments in quantum communication and cryptography often require sophisticated and costly experimental setups. In this paper, we present an inexpensive and accessible classical optical analog system to demonstrate quantum tomography and test Bell's inequality. A pseudo-random number generator was used to simulate the quantum randomness of photons. This method has proven sufficient for mimicking quantum phenomena. The density matrices of the ensemble measured are in agreement with results published before, and the Bell parameter \( S \) value obtained in this experiment is \( -2.71 \pm 0.18 \), which aligns with the predictions of quantum mechanics and contradicts local hidden variable theories.

However, it is important to note that the results do not represent the true behavior of photons and thus cannot be treated as a true violation of Bell's inequality. Instead, the experiment provides an excellent first step for undergraduate students to gain a practical understanding of how experiments in quantum mechanics are conducted.

## Code Overview
  
  ### Generating random sets for simulating a quantum state
  - **Output**: Random number to be used as qubit values for the tomography part of the experiment
  - **Output**: Random number to be used as qubit values for the Bell test part of the experiment
  
  ### Processing red light from recorded videos
  - **Input**: Recording of experiment
  - **Output**: Mapping between red light intensity to frame number for each video
  
  ### Finding peaks - Tomography
  - **Input**: Red light intensity for each of the first part videos
  - **Output**: Generate graphs and find peaks that are above a preconfigured threshold
  
  ### Reconstructing density matrix from experiment
  - **Input**: Peaks found previously
  - **Output**: Reconstructed density matrix
  
  ### Finding peaks - Bell
  - **Input**: Red light intensity for each of the second part videos
  - **Output**: Generate graphs and find peaks that are above a preconfigured threshold
  
  ### Calculating Bell's inequality
  - **Input**: Peaks of Bell test measurements
  - **Output**: S parameter of the Bell test
  - 
  ### Density Matrix Tomography Simulation
  - **Output**: Density matrices calculated using a virtual experiment for the first and third Bell states