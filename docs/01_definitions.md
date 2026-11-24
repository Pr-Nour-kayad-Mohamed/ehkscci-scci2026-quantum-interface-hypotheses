# Definitions and Scope

## Purpose

This document defines the mathematical objects, modelling conventions,
assumptions, and limitations used in the exploratory SCCI-2026 quantum
interface hypothesis.

This repository does **not** claim to validate, improve, stabilize, or
solve Google Willow, any 105-qubit processor, or any quantum-hardware
platform.

All quantities introduced here are modelling variables unless they are
explicitly derived, measured, simulated, and independently reproduced.

## Status

| Item | Status |
|---|---|
| SCCI-2026 Layer 1 canonical bridge workflow | Locally validated in the separate archival repository |
| Complete SCCI-2026 revision 1.0 | Not archived in this repository |
| Quantum interface hypothesis | Exploratory hypothesis |
| Willow stabilisation claim | Not validated |
| Delta_Phi = 3.0063 | Modelling convention, not a physical constant |
| Unitarity claim | Not established |
| Gate-fidelity improvement claim | Not established |
| Cohomology-based noise cancellation claim | Not established |

## Notation

Let \(M\) denote a modelling space, \(N \subset M\) an interface
subspace, and \(U(1)\) the abelian gauge group used in the exploratory
model.

Let \(x,y \in M\) denote points in the modelling space. Let
\(\tau_{\mathrm{supra}}\) and \(\tau_{\mathrm{atome}}\) denote
characteristic timescales assigned to two idealised subsystems.

Let \(d\) denote the code distance of an idealised surface-code model.
Let \(N_q\) denote the number of physical qubits in an idealised
hardware model.

## Scalar field Phi

### Definition

\[
\Phi : M \to \mathbb{R}
\]

\(\Phi\) is an effective scalar field used as a modelling degree of
freedom. It is not assumed to be a fundamental field unless a separate
microscopic derivation is supplied.

### Interpretation

In this exploratory model, \(\Phi\) is intended to represent an
effective information-geometric or thermodynamic ordering variable.

### Status

\(\Phi\) is a hypothesis. Its physical interpretation, equation of
motion, coupling constants, and domain of validity are not established.

## Conformal factor Omega

### Definition

\[
\Omega : M \to \mathbb{R}_{>0}
\]

\(\Omega\) is a positive conformal scaling factor.

### Proposed relation

A tentative relation between an effective conformal factor and two
characteristic timescales is:

\[
\Omega
=
\left(
\frac{\tau_{\mathrm{supra}}}{\tau_{\mathrm{atome}}}
\right)^{1/\Delta_\Phi}.
\]

For the illustrative values

\[
\tau_{\mathrm{supra}} = 10^{-9}\,\mathrm{s},
\qquad
\tau_{\mathrm{atome}} = 10^{-3}\,\mathrm{s},
\]

this becomes:

\[
\Omega
=
10^{-6/\Delta_\Phi}.
\]

### Important limitation

This relation is a **modelling convention**, not a derived physical law.
It does not follow from quantum mechanics, conformal field theory,
superconducting-circuit theory, or neutral-atom physics without an
explicit derivation.

## Conformal dimension Delta_Phi

### Definition

In a conformal setting, the scaling dimension \(\Delta_\Phi\) of an
operator \(\Phi\) is defined by the scaling behaviour of its two-point
correlation function:

\[
\langle \Phi(x)\Phi(y)\rangle
\propto
\frac{1}{|x-y|^{2\Delta_\Phi}}.
\]

### Status

\(\Delta_\Phi\) is a property of a specified conformal theory or
effective field theory. It cannot be determined from the number of
qubits, the size of a quantum-error-correcting code, or a ratio of
timescales without a complete model.

### Proposed working value

The value

\[
\Delta_\Phi = 3.0063
\]

is obtained only from the ad hoc convention:

\[
10^{-6/\Delta_\Phi}
=
\frac{1}{\log_{10}\left(105^{49}\right)}.
\]

Therefore:

\[
\Delta_\Phi
=
\frac{6}{\log_{10}\left(49\log_{10}105\right)}
\approx 3.0063.
\]

### Status of the value

This value is a **consequence of an arbitrary modelling convention**.
It is not a physical prediction, a measured constant, or a validated
critical value.

## Effective mass m_Phi_eff

### Definition

\[
m_{\Phi,\mathrm{eff}} : M \to \mathbb{R}_{>0}
\]

\(m_{\Phi,\mathrm{eff}}\) denotes an effective mass-like parameter
associated with the scalar field \(\Phi\).

### Proposed role

In the exploratory model, \(m_{\Phi,\mathrm{eff}}\) is intended to act
as a control parameter that modifies an effective interface impedance.

### Required derivation

To use this quantity rigorously, one must specify:

- Its units.
- Its equation of motion.
- Its dependence on material or environmental variables.
- Its coupling to the quantum subsystems.
- Its relation to measurable observables.
- Its stability and boundedness conditions.

### Status

No derivation or experimental identification is provided. Therefore,
\(m_{\Phi,\mathrm{eff}}\) remains an undefined modelling parameter.

## Information capacity K_Q

### Definition

\[
\mathcal{K}_{\mathcal{Q}}
\]

\(\mathcal{K}_{\mathcal{Q}}\) is proposed as a measure of preserved
quantum information.

### Required definition

A rigorous definition must specify whether it is:

- A quantum capacity.
- A private capacity.
- A coherent information.
- A channel capacity.
- A logical-qubit fidelity measure.
- A code-specific error-correction metric.

### Status

Without such a definition, \(\mathcal{K}_{\mathcal{Q}}\) is not a
well-defined physical or information-theoretic quantity.

## Dissipation D_Q

### Definition

\[
\mathcal{D}_{\mathcal{Q}}
\]

\(\mathcal{D}_{\mathcal{Q}}\) is proposed as a dissipation-like
quantity.

### Required definition

A rigorous definition must specify whether it denotes:

- Energy dissipation rate.
- Entropy production rate.
- Decoherence rate.
- Depolarising error rate.
- Thermal relaxation rate.
- Dephasing rate.
- A combination of several Lindblad rates.

### Status

No units, equation of motion, or physical identification is provided.
Therefore, \(\mathcal{D}_{\mathcal{Q}}\) remains undefined.

## Operational control cost O_Q

### Definition

\[
\mathcal{O}_{\mathcal{Q}}
\]

\(\mathcal{O}_{\mathcal{Q}}\) is proposed as an operational control
cost.

### Required definition

A rigorous definition must specify whether it measures:

- Control pulse energy.
- Control time.
- Gate error.
- Calibration overhead.
- Readout error.
- Crosstalk.
- Computational cost.
- A monetary or energetic cost.

### Status

Without a definition, \(\mathcal{O}_{\mathcal{Q}}\) is not a measurable
or optimisable quantity.

## Entropy constraint Sigma_Phi

### Proposed inequality

\[
\Sigma_\Phi
=
\Delta S_{\mathrm{interface}}
+
\int_{t_0}^{t_1}
\frac{J_E(t)}{T(t)}
\,dt
\ge 0.
\]

### Intended interpretation

\(\Sigma_\Phi\) is intended to represent a non-negative entropy-like
constraint.

### Required definitions

For this expression to be meaningful, one must define:

- The system boundary.
- The entropy \(S_{\mathrm{interface}}\).
- The heat current \(J_E(t)\).
- The temperature \(T(t)\).
- The time interval \([t_0,t_1]\).
- Whether the process is closed, open, isothermal, adiabatic, or none
  of these.
- The thermodynamic framework used.

### Status

The inequality is plausible as a broad thermodynamic principle, but it
does not by itself imply stability, unitarity, noise suppression, or
quantum-error-correction improvement.

## Interface impedance Z_interface

### Proposed relation

A tentative relation is:

\[
Z_{\mathrm{interface}}(\Phi)
\propto
\frac{
\mathcal{D}_{\mathcal{Q}}+\mathcal{O}_{\mathcal{Q}}
}{
m_{\Phi,\mathrm{eff}}\sigma_p^2
}.
\]

### Problems

This! relation is not dimensionally consistent unless the units,
normalisation, and physical meaning of every variable are specified.

It also does not define whether \(Z_{\mathrm{interface}}\) is:

- An electrical impedance.
- A mechanical impedance.
- A quantum scattering impedance.
- A control-channel impedance.
- A dimensionless coupling parameter.

### Status

\(Z_{\mathrm{interface}}\) is an undefined modelling quantity.

## Density fluctuation sigma_p

### Definition

\[
\sigma_p^2
\]

\(\sigma_p^2\) is proposed as a variance of a density-like fluctuation.

### Required definition

One must specify:

- The random variable \(p\).
- Its probability distribution.
- Its spatial support.
- Its time dependence.
- Its units.
- Its relation to physical density, charge density, mass density, or
  another observable.

### Status

\(\sigma_p^2\) is undefined without these specifications.

## Hybrid interface Hamiltonian

### Proposed form

A tentative interaction Hamiltonian is:

\[
H_{\mathrm{hybrid}}
=
\hbar
\sum_k
\left(
g_k a_k^\dagger \sigma_k^-
+
g_k^* a_k \sigma_k^+
\right)
+
\int_M
\Phi(x)J_{U(1)}(x)
\,d^3x.
\]

### Required definitions

To make this Hamiltonian meaningful, one must define:

- The Hilbert space.
- The bosonic operators \(a_k\).
- The qubit or atomic operators \(\sigma_k^\pm\).
- The coupling constants \(g_k\).
- The current operator \(J_{U(1)}\).
- The integration domain.
- The boundary conditions.
- The dissipative channels.
- The Lindblad operators, if open-system dynamics are intended.

### Status

This is an exploratory ansatz, not a validated physical model.

## Scattering matrix S_hyb

### Proposed form

A tentative factorised form is:

\[
S_{\mathrm{hyb}}
=
\begin{pmatrix}
R_{\mathrm{supra}} & T_{\mathrm{hyb}} \\
T_{\mathrm{hyb}} & R_{\mathrm{atome}}
\end{pmatrix}
\exp\left(
i\int_{\partial N}A_\Phi
\right).
\]

### Required conditions

For \(S_{\mathrm{hyb}}\) to be a valid scattering matrix, one must
define:

- Input and output channels.
- Their normalisation.
- Their frequency dependence.
- The Hamiltonian generating the scattering.
- The boundary conditions.
- The absorption and loss channels.
- The relation between \(R\), \(T\), and the full scattering matrix.

### Unitarity condition

For a closed, lossless two-port system, unitarity requires:

\[
S_{\mathrm{hyb}}^\dagger S_{\mathrm{hyb}} = I.
\]

This condition cannot be established merely by assuming that
\(|R|^2+|T|^2=1\) for selected frequency ranges.

### Status

\(S_{\mathrm{hyb}}\) is an exploratory ansatz, not a validated
scattering model.

## Relative cohomology group

### Proposed object

\[
H^1_{\mathrm{Kayad}}(M,N;U(1)).
\]

### Required definitions

To define this object rigorously, one must specify:

- The topological space \(M\).
- The subspace \(N\).
- The coefficient system or local system.
- The chain complex.
- The coboundary operator.
- The connection or gauge field.
- The gauge transformation group.
- The relation to standard relative cohomology.

### Status

Until these objects are defined, the notation
\(H^1_{\mathrm{Kayad}}\) is not a well-defined mathematical object.

## Cohomological cancellation claim

### Proposed condition

\[
\int_{\partial N}A_\Phi
=
\int_{\partial N}d\chi
=
0
\pmod{2\pi}.
\]

### Interpretation

This condition would mean that the integrated phase is gauge-pure.

### Limitation

Even if this condition holds, it does not by itself imply:

- Unitarity.
- Absence of decoherence.
- Absence of thermal noise.
- Stability of a quantum processor.
- Improvement of logical gate fidelity.
- Correction of quantum errors.

## Surface-code claims

### Code distance

Let \(d\) denote the code distance of an idealised surface code.

### Logical error rate

A common asymptotic scaling form is:

\[
P_{\mathrm{logical}}
\sim
C
\left(
\frac{p_{\mathrm{physical}}}{p_{\mathrm{threshold}}}
\right)^{(d+1)/2}.
\]

### Required conditions

This approximation requires:

- A specified noise model.
- A specified decoder.
- A specified code family.
- A specified circuit-level noise model.
- A specified threshold.
- A specified logical operator.
- A specified error metric.

### Status

The formula cannot be used to compare a baseline system with a
hypothetical optimised system unless both systems use the same noise
model, decoder, code geometry, and evaluation protocol.

## Willow claims

### Explicit limitation

This repository does **not** claim that:

- Willow is improved.
- Willow is stabilised.
- Willow is solved.
- A 105-qubit processor is stabilised.
- A 7-by-7 surface code is improved.
- Logical gate fidelity is improved.
- Thermal noise is eliminated.
- Decoherence is eliminated.
- A hybrid supraconducting-neutral-atom interface is realised.

## Falsifiability criteria

A hypothesis in this repository may be considered supported only if it
produces a reproducible prediction that can be compared with an
independent reference model or experiment.

Minimum requirements:

1. A complete mathematical model.
2. Explicit assumptions and units.
3. A deterministic simulation or analytical derivation.
4. Fixed random seeds, where applicable.
5. Input and output files.
6. A baseline model using the same assumptions except for the proposed
   mechanism.
7. A statistical comparison.
8. A documented failure condition.
9. Independent reproduction from a clean repository clone.

## Non-goals

This repository does not aim to:

- Replace quantum error correction.
- Replace established quantum-hardware engineering.
- Claim priority over existing conformal field theory.
- Claim priority over existing surface-code theory.
- Claim experimental validation.
- Claim industrial deployment.
- Claim a solution to decoherence.
- Claim a solution to quantum error correction.

## Version

This document is version 0.1.0 of the exploratory quantum-interface
hypothesis.

It is subject to revision whenever a definition, assumption, derivation,
simulation, or experimental result changes.
