# Limitations, Rejection Criteria, and Validation Requirements

## Purpose

This document defines the limits of the exploratory SCCI-2026 quantum
interface hypothesis.

It prevents confusion between:

- A mathematical convention.
- A numerical calculation.
- A physical hypothesis.
- A reproducible simulation.
- An experimentally validated result.
- A claim about a real quantum processor.

Nothing in this repository validates Google Willow, any 105-qubit
processor, a hybrid superconducting-neutral-atom interface, or an
improvement in quantum gate fidelity.

## Primary limitation

The current model does not contain a complete physical theory.

It does not specify:

- A Hilbert space.
- A Hamiltonian.
- A Lindblad or open-system model.
- A noise model.
- A decoder.
- A code geometry.
- A scattering matrix.
- A physical interface.
- A measurable observable.
- A reproducible experiment.
- An independent reference model.

Therefore, no physical claim can be validated.

## Status of Delta_Phi

The value

\[
\Delta_\Phi \approx 3.0063
\]

is obtained from the ad hoc convention:

\[
10^{-6/\Delta_\Phi}
=
\frac{1}{\log_{10}\left(105^{49}\right)}.
\]

It is a numerical consequence of that convention.

It is **not**:

- A physical constant.
- A universal critical value.
- A measured parameter.
- A prediction of conformal field theory.
- A property of Willow.
- A property of any 105-qubit processor.
- A threshold for quantum error correction.
- A condition for unitarity.
- A condition for thermal-noise suppression.
- A condition for decoherence suppression.

## Status of the conformal relation

The relation

\[
\Omega
=
\left(
\frac{\tau_{\mathrm{supra}}}{\tau_{\mathrm{atome}}}
\right)^{1/\Delta_\Phi}
\]

is a modelling convention.

It is not derived from:

- Conformal field theory.
- Quantum mechanics.
- Superconducting-circuit theory.
- Neutral-atom physics.
- Quantum error correction.
- Thermodynamics.
- Information theory.

Therefore, it cannot be used to claim a physical synchronisation between
two quantum subsystems.

## Status of the entropy constraint

The inequality

\[
\Sigma_\Phi
=
\Delta S_{\mathrm{interface}}
+
\int_{t_0}^{t_1}
\frac{J_E(t)}{T(t)}
\,dt
\ge 0
\]

is a generic thermodynamic form.

It does not by itself establish:

- Stability.
- Unitarity.
- Noise suppression.
- Decoherence suppression.
- Quantum error correction.
- Logical gate fidelity improvement.
- Physical feasibility of an interface.

To use it, one must define the system boundary, entropy, heat current,
temperature, time interval, and thermodynamic process.

## Status of the impedance relation

The relation

\[
Z_{\mathrm{interface}}(\Phi)
\propto
\frac{
\mathcal{D}_{\mathcal{Q}}+\mathcal{O}_{\mathcal{Q}}
}{
m_{\Phi,\mathrm{eff}}\sigma_p^2
}
\]

is not currently well defined.

It lacks:

- Units.
- Dimensional consistency.
- A physical interpretation.
- A definition of \(Z_{\mathrm{interface}}\).
- A definition of \(\mathcal{D}_{\mathcal{Q}}\).
- A definition of \(\mathcal{O}_{\mathcal{Q}}\).
- A definition of \(m_{\Phi,\mathrm{eff}}\).
- A definition of \(\sigma_p^2\).

Therefore, it cannot be used to predict reflection, transmission,
stability, or noise suppression.

## Status of the scattering matrix

The proposed matrix

\[
S_{\mathrm{hyb}}
=
\begin{pmatrix}
R_{\mathrm{supra}} & T_{\mathrm{hyb}} \\
T_{\mathrm{hyb}} & R_{\mathrm{atome}}
\end{pmatrix}
\exp\left(
i\int_{\partial N}A_\Phi
\right)
\]

is an exploratory ansatz.

It is not a validated scattering model because it does not define:

- Input and output channels.
- Their normalisation.
- Their frequency dependence.
- The generating Hamiltonian.
- Boundary conditions.
- Loss channels.
- Absorption channels.
- The full scattering matrix.
- The relation between reflection and transmission coefficients.

## Status of unitarity

For a closed, lossless two-port system, unitarity requires:

\[
S^\dagger S = I.
\]

This condition cannot be established merely by assuming:

\[
|R|^2 + |T|^2 = 1.
\]

A cohomological condition such as:

\[
\int_{\partial N}A_\Phi
=
0
\pmod{2\pi}
\]

may constrain a phase, but it does not establish unitarity.

Unitarity requires a complete Hamiltonian, proper boundary conditions,
and a complete account of loss channels.

## Status of cohomology

The notation

\[
H^1_{\mathrm{Kayad}}(M,N;U(1))
\]

is not currently a well-defined mathematical object.

Before using it, one must define:

- The topological space \(M\).
- The subspace \(N\).
- The coefficient system.
- The chain complex.
- The coboundary operator.
- The connection or gauge field.
- The relation to standard relative cohomology.

Until then, no cancellation theorem, anomaly-free condition, or
unitarity proof can be derived.

## Status of surface-code claims

The formula

\[
P_{\mathrm{logical}}
\sim
C
\left(
\frac{p_{\mathrm{physical}}}{p_{\mathrm{threshold}}}
\right)^{(d+1)/2}
\]

is a rough asymptotic scaling relation.

It cannot be used to compare a baseline system with a hypothetical
optimised system unless both systems use:

- The same code family.
- The same code distance.
- The same noise model.
- The same decoder.
- The same logical operator.
- The same error metric.
- The same circuit-level noise model.
- The same threshold.
- The same evaluation protocol.

## Code-size correction

A \(7 \times 7\) surface-code patch generally contains 49 data qubits,
not 97 physical qubits per logical qubit.

The claim that “97 physical qubits are required per logical qubit” is
not established by the present model.

It must not be used without a specific code construction, noise model,
decoder, and logical-operator definition.

## Willow limitation

This repository does **not** claim that:

- Willow is improved.
- Willow is stabilised.
- Willow is solved.
- A 105-qubit processor is stabilised.
- A \(7 \times 7\) surface code is improved.
- Logical gate fidelity is improved.
- Thermal noise is eliminated.
- Decoherence is eliminated.
- A hybrid superconducting-neutral-atom interface is realised.
- A conformal field suppresses quantum noise.
- A scalar field controls a quantum processor.
- A cohomological condition removes decoherence.

## Rejection criteria

A hypothesis must be rejected or heavily revised if any of the following
occurs:

1. The mathematical model is internally inconsistent.
2. The units or dimensions are incompatible.
3. A claimed observable cannot be defined.
4. A simulation is not reproducible.
5. A result depends on an arbitrary convention without justification.
6. The baseline and proposed models use different assumptions.
7. The claimed improvement disappears under a fair comparison.
8. The predicted effect is not distinguishable from noise or systematic
   error.
9. The model contradicts an established conservation law without a
   documented extension or exception.
10. The claimed result cannot be reproduced from a clean repository
    clone.
11. The claimed result relies on circular reasoning.
12. The claimed result is presented as validation without independent
    reproduction.

## Circular-reasoning test

A simulation is circular if it assumes the conclusion it is supposed to
test.

Example:

```text
Assume Delta_Phi = 3.0063 stabilises the interface.
Assume the interface suppresses noise.
Assume reduced noise improves fidelity.
Compute fidelity.
Conclude that Delta_Phi = 3.0063 improves fidelity.
