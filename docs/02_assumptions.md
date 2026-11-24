# Assumptions and Modelling Conventions

## Purpose

This document separates the assumptions, conventions, hypotheses, and
open questions used in the exploratory SCCI-2026 quantum-interface
model.

Nothing in this document should be interpreted as an experimentally
validated result, a physical prediction, or a claim about Google Willow,
any 105-qubit processor, or any quantum-hardware platform.

## Modelling principle

The model distinguishes four categories:

| Category | Meaning |
|---|---|
| Definition | A mathematical object is precisely specified |
| Assumption | A condition is imposed for the model to work |
| Convention | A rule or formula is chosen for exploration |
| Hypothesis | A claim is proposed but not established |
| Derivation | A result follows logically from stated assumptions |
| Simulation | A numerical output is produced from a specified model |
| Validation | A result is reproduced independently and compared with a reference |

## Global scope

The exploratory model concerns a hypothetical interface between two
idealised quantum subsystems:

\[
\mathcal{S}_{\mathrm{supra}}
\quad \text{and} \quad
\mathcal{S}_{\mathrm{atome}}.
\]

It does **not** assume that these subsystems correspond to any specific
commercial processor, including Google Willow.

## Subsystem assumptions

### Supraconducting subsystem

The model assumes an idealised superconducting subsystem with a
characteristic control or coherence timescale:

\[
\tau_{\mathrm{supra}} = 10^{-9}\,\mathrm{s}.
\]

This value is a modelling assumption. It is not a measured parameter of
any specific processor.

### Neutral-atom subsystem

The model assumes an idealised neutral-atom subsystem with a
characteristic control or coherence timescale:

\[
\tau_{\mathrm{atome}} = 10^{-3}\,\mathrm{s}.
\]

This value is also a modelling assumption. It is not a measured
parameter of any specific processor.

### Interface assumption

The model assumes that an interface between the two subsystems could be
described by an effective coupling mechanism.

This assumption is not established. No physical implementation,
experimental protocol, or hardware architecture is specified.

## Scalar-field assumption

### Hypothesis H-1

An effective scalar field \(\Phi\) may be used as a modelling degree of
freedom for an interface.

\[
\Phi : M \to \mathbb{R}.
\]

### Status

This is a hypothesis. It is not derived from a microscopic theory, and
its physical interpretation is not established.

### Required clarification

A rigorous version of this hypothesis must specify:

- Whether \(\Phi\) is classical, quantum, stochastic, or effective.
- Its equation of motion.
- Its coupling to matter, radiation, or qubits.
- Its boundary conditions.
- Its units.
- Its domain of validity.

## Conformal assumption

### Hypothesis H-2

An effective conformal scaling factor \(\Omega\) may relate the
timescales of the two idealised subsystems.

\[
\Omega
=
\left(
\frac{\tau_{\mathrm{supra}}}{\tau_{\mathrm{atome}}}
\right)^{1/\Delta_\Phi}.
\]

### Status

This is a modelling convention, not a derived physical law.

### Required clarification

A rigorous version must specify:

- The conformal transformation group.
- The metric or effective metric.
- The operator \(\Phi\).
- Its conformal dimension.
- The physical observable being scaled.
- The reason why the timescale ratio enters the relation.

## Dimension assumption

### Hypothesis H-3

A dimension \(\Delta_\Phi\) may be used to parameterise the scaling
behaviour of the effective field \(\Phi\).

\[
\langle \Phi(x)\Phi(y)\rangle
\propto
\frac{1}{|x-y|^{2\Delta_\Phi}}.
\]

### Status

This is a standard form of scaling in conformal field theory, but it
does not determine \(\Delta_\Phi\) in the present model.

### Required clarification

To determine \(\Delta_\Phi\), one must specify a complete conformal
model, including its action, symmetry group, operator content, and
boundary conditions.

## Critical-value convention

### Convention C-1

The following relation is adopted as an exploratory modelling
convention:

\[
10^{-6/\Delta_\Phi}
=
\frac{1}{\log_{10}\left(105^{49}\right)}.
\]

### Consequence

Solving this convention gives:

\[
\Delta_\Phi
=
\frac{6}{\log_{10}\left(49\log_{10}105\right)}
\approx 3.0063.
\]

### Status

This is **not** a validated critical value.

It is a numerical consequence of an ad hoc convention. It must not be
described as a physical constant, a universal threshold, or a property
of Willow.

## Topological assumption

### Hypothesis H-4

The topology of an idealised quantum-error-correcting code may influence
the stability of an interface.

### Status

This is a broad and unproven hypothesis.

### Required clarification

A rigorous version must specify:

- The code family.
- The code distance.
- The qubit connectivity graph.
- The noise model.
- The decoder.
- The logical operators.
- The error metric.
- The relation between topology and interface dynamics.

## Qubit-count assumption

### Assumption A-1

The idealised hardware model contains:

\[
N_q = 105
\]

physical qubits.

### Status

This is only a parameter of an idealised model. It does not establish
any connection with a real processor.

## Surface-code assumption

### Assumption A-2

An idealised surface-code model has code distance:

\[
d = 7.
\]

### Important correction

A \(7 \times 7\) surface-code patch generally contains 49 data qubits,
not 97 physical qubits per logical qubit.

The claim that “97 physical qubits are required per logical qubit” is
not established by the present model and must not be used without a
specific code construction and noise model.

### Status

The code model is idealised and incomplete.

## Entropy assumption

### Hypothesis H-5

An entropy-like constraint may be expressed as:

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

### Status

This is a generic thermodynamic form, but it is not sufficient to define
a physical model.

### Required clarification

The following must be defined:

- The thermodynamic system boundary.
- The entropy \(S_{\mathrm{interface}}\).
- The heat current \(J_E(t)\).
- The temperature \(T(t)\).
- The time interval.
- The process class: closed, open, isothermal, adiabatic, or other.
- The relation to quantum entropy, classical entropy, or both.

## Impedance assumption

### Hypothesis H-6

An effective interface impedance may depend on an effective mass,
dissipation, control cost, and density fluctuation:

\[
Z_{\mathrm{interface}}(\Phi)
\propto
\frac{
\mathcal{D}_{\mathcal{Q}}+\mathcal{O}_{\mathcal{Q}}
}{
m_{\Phi,\mathrm{eff}}\sigma_p^2
}.
\]

### Status

This is an unproven modelling convention.

### Required clarification

The relation is not dimensionally consistent until the units and
definitions of all variables are specified.

It must also be clarified whether \(Z_{\mathrm{interface}}\) denotes:

- Electrical impedance.
- Mechanical impedance.
- Quantum scattering impedance.
- Control-channel impedance.
- A dimensionless coupling parameter.

## Noise-filtering hypothesis

### Hypothesis H-7

A large effective mass \(m_{\Phi,\mathrm{eff}}\) could increase the
interface impedance and reduce transmission of unwanted modes.

### Proposed limiting behaviour

\[
\lim_{m_{\Phi,\mathrm{eff}}\to\infty}
|R_{\mathrm{supra}}|^2
=
1,
\qquad
\lim_{m_{\Phi,\mathrm{eff}}\to\infty}
|T_{\mathrm{hyb}}|^2
=
0.
\]

### Status

This behaviour is assumed, not derived.

### Required clarification

A rigorous derivation must specify:

- The scattering matrix.
- The input and output channels.
- The frequency dependence.
- The Hamiltonian.
- The boundary conditions.
- The loss channels.
- The relation between impedance and reflection/transmission.

## Unitarity hypothesis

### Hypothesis H-8

The interface may preserve unitarity if an appropriate cohomological
condition cancels uncontrolled geometric phases.

\[
\int_{\partial N}A_\Phi
=
0
\pmod{2\pi}.
\]

### Status

This is not established.

### Required clarification

Unitarity requires:

\[
S^\dagger S = I.
\]

This condition depends on the full Hamiltonian, the loss channels, the
boundary conditions, and the normalisation of input and output modes.

A cohomological condition alone does not establish unitarity.

## Cohomology assumption

### Hypothesis H-9

A relative cohomology group denoted
\(H^1_{\mathrm{Kayad}}(M,N;U(1))\) may describe obstructions associated
with an interface.

### Status

This is not currently a well-defined mathematical object.

### Required clarification

Before using this notation, one must define:

- The topological space \(M\).
- The subspace \(N\).
- The coefficient system.
- The chain complex.
- The coboundary operator.
- The connection or gauge field.
- The relation to standard relative cohomology.

## Gate-fidelity hypothesis

### Hypothesis H-10

A reduction in physical error rate may improve logical gate fidelity in
a surface-code model.

### Proposed scaling form

\[
P_{\mathrm{logical}}
\sim
C
\left(
\frac{p_{\mathrm{physical}}}{p_{\mathrm{threshold}}}
\right)^{(d+1)/2}.
\]

### Status

This is only a rough asymptotic approximation.

### Required clarification

A meaningful comparison requires:

- The same code family.
- The same code distance.
- The same noise model.
- The same decoder.
- The same logical operator.
- The same error metric.
- The same circuit-level noise model.
- The same threshold.
- The same evaluation protocol.

## Willow limitation

### Explicit non-claim

This model does **not** claim that:

- Willow is improved.
- Willow is stabilised.
- Willow is solved.
- A 105-qubit processor is stabilised.
- A \(7 \times 7\) surface code is improved.
- Logical gate fidelity is improved.
- Thermal noise is eliminated.
- Decoherence is eliminated.
- A hybrid superconducting-neutral-atom interface is realised.

## Falsification criteria

A hypothesis may be rejected if any of the following occurs:

1. The mathematical model is internally inconsistent.
2. The units or dimensions are incompatible.
3. The predicted observable cannot be defined.
4. The simulation is not reproducible.
5. The result depends on an arbitrary convention without justification.
6. The baseline and proposed models use different assumptions.
7. The claimed improvement disappears under a fair comparison.
8. The predicted effect is not distinguishable from noise or systematic
   error.
9. The model contradicts an established conservation law without a
   documented extension or exception.

## Required controls

Any simulation must include:

- A baseline model.
- A proposed model.
- Identical initial conditions.
- Identical noise model.
- Identical decoder or evaluation method.
- Fixed random seeds.
- Confidence intervals or uncertainty estimates.
- Input and output files.
- A documented failure condition.

## Version

This document is version 0.1.0 of the exploratory quantum-interface
hypothesis.

It is subject to revision whenever a definition, assumption, derivation,
simulation, or experimental result changes.
