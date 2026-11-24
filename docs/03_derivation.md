# Derivations and Logical Status

## Purpose

This document separates what can be derived from the stated assumptions,
what remains a modelling convention, and what cannot be claimed without
a complete physical or mathematical model.

Nothing here validates Google Willow, any 105-qubit processor, a hybrid
superconducting-neutral-atom interface, or an improvement in quantum
gate fidelity.

## Logical categories

| Category | Meaning |
|---|---|
| Definition | A mathematical object is specified |
| Assumption | A condition is imposed |
| Convention | A rule is chosen for exploration |
| Derivation | A result follows from definitions and assumptions |
| Numerical result | A value is computed from a specified formula |
| Physical claim | A statement about reality or hardware |
| Validation | A claim is independently reproduced and tested |

## Important rule

A numerical result is not a physical validation.

A formula can produce a number, but that number has physical meaning
only if the formula itself is derived from a well-defined model and the
model is tested against an independent reference.

## Starting definitions

The following objects are defined in `01_definitions.md`:

\[
\Phi,\quad
\Omega,\quad
\Delta_\Phi,\quad
m_{\Phi,\mathrm{eff}},\quad
\mathcal{K}_{\mathcal{Q}},\quad
\mathcal{D}_{\mathcal{Q}},\quad
\mathcal{O}_{\mathcal{Q}},\quad
\Sigma_\Phi.
\]

At present, most of these objects are modelling variables, not
well-defined physical observables.

## Timescale ratio

### Assumption

Let:

\[
\tau_{\mathrm{supra}} = 10^{-9}\,\mathrm{s},
\qquad
\tau_{\mathrm{atome}} = 10^{-3}\,\mathrm{s}.
\]

### Derived ratio

Then:

\[
\frac{\tau_{\mathrm{supra}}}{\tau_{\mathrm{atome}}}
=
\frac{10^{-9}}{10^{-3}}
=
10^{-6}.
\]

### Logical status

This is a valid arithmetic derivation from the two assumed timescales.

It does not establish any physical relationship between a
superconducting subsystem and a neutral-atom subsystem.

## Proposed conformal relation

### Convention

The exploratory model adopts:

\[
\Omega
=
\left(
\frac{\tau_{\mathrm{supra}}}{\tau_{\mathrm{atome}}}
\right)^{1/\Delta_\Phi}.
\]

### Substitution

Using the timescale ratio:

\[
\Omega
=
\left(10^{-6}\right)^{1/\Delta_\Phi}.
\]

Therefore:

\[
\Omega
=
10^{-6/\Delta_\Phi}.
\]

### Logical status

This is a valid algebraic consequence of the chosen convention.

It is **not** a derivation from conformal field theory, quantum
mechanics, superconducting-circuit theory, or neutral-atom physics.

## Critical-value convention

### Convention

The model adopts:

\[
10^{-6/\Delta_\Phi}
=
\frac{1}{\log_{10}\left(105^{49}\right)}.
\]

### Algebraic manipulation

Taking base-10 logarithms:

\[
-\frac{6}{\Delta_\Phi}
=
-\log_{10}\left(\log_{10}\left(105^{49}\right)\right).
\]

Therefore:

\[
\frac{6}{\Delta_\Phi}
=
\log_{10}\left(\log_{10}\left(105^{49}\right)\right).
\]

Using:

\[
\log_{10}\left(105^{49}\right)
=
49\log_{10}(105),
\]

we obtain:

\[
\frac{6}{\Delta_\Phi}
=
\log_{10}\left(49\log_{10}(105)\right).
\]

Thus:

\[
\Delta_\Phi
=
\frac{6}{\log_{10}\left(49\log_{10}(105)\right)}.
\]

### Numerical evaluation

Using:

\[
\log_{10}(105) \approx 2.0212,
\]

we obtain:

\[
49\log_{10}(105)
\approx 99.038.
\]

Therefore:

\[
\log_{10}(99.038)
\approx 1.9958.
\]

Finally:

\[
\Delta_\Phi
\approx
\frac{6}{1.9958}
\approx
3.0063.
\]

### Logical status

This is a valid numerical consequence of the chosen convention.

It is **not** a physical prediction, a measured constant, or a validated
critical value.

## What the value does not prove

The value

\[
\Delta_\Phi \approx 3.0063
\]

does **not** prove that:

- A conformal transition exists.
- A hybrid interface is physically possible.
- Willow is stabilised.
- A 105-qubit processor is stabilised.
- Thermal noise is suppressed.
- Decoherence is suppressed.
- Quantum gate fidelity improves.
- A surface code improves.
- A cohomological obstruction vanishes.
- A scattering matrix is unitary.

## Entropy inequality

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

### Possible derivation

If:

- \(S_{\mathrm{interface}}\) is a well-defined entropy;
- \(J_E(t)\) is a well-defined heat current;
- \(T(t)>0\) is a well-defined temperature;
- the system obeys the second law of thermodynamics;

then a non-negative entropy production may be consistent with the
inequality.

### Missing assumptions

The inequality cannot be derived without specifying:

- The thermodynamic system boundary.
- The entropy definition.
- The heat-current definition.
- The temperature definition.
- The process class.
- The relation between classical and quantum entropy.
- The dynamics of the interface.

### Logical status

The inequality is a plausible thermodynamic constraint, but it is not
sufficient to establish stability, unitarity, noise suppression, or
quantum-error-correction improvement.

## Impedance relation

### Proposed relation

\[
Z_{\mathrm{interface}}(\Phi)
\propto
\frac{
\mathcal{D}_{\mathcal{Q}}+\mathcal{O}_{\mathcal{Q}}
}{
m_{\Phi,\mathrm{eff}}\sigma_p^2
}.
\]

### Dimensional analysis

The relation cannot be checked until the units of every quantity are
specified.

At present:

- \(\mathcal{D}_{\mathcal{Q}}\) has no defined units.
- \(\mathcal{O}_{\mathcal{Q}}\) has no defined units.
- \(m_{\Phi,\mathrm{eff}}\) has no defined units.
- \(\sigma_p^2\) has no defined units.
- \(Z_{\mathrm{interface}}\) has no defined type or units.

### Logical status

This is not currently a derivable physical relation.

It is an unproven modelling ansatz.

## Noise-filtering limit

### Proposed claim

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

### What would be needed

To derive these limits, one must specify:

- A scattering matrix \(S\).
- Input and output channels.
- Their normalisation.
- A Hamiltonian or transfer function.
- Boundary conditions.
- Frequency dependence.
- Loss channels.
- The dependence of \(R\) and \(T\) on \(m_{\Phi,\mathrm{eff}}\).

### Logical status

These limits are assumed, not derived.

They cannot be used as evidence of noise suppression.

## Unitarity condition

### General condition

For a closed, lossless scattering process:

\[
S^\dagger S = I.
\]

### Required derivation

To establish unitarity, one must show that:

- The evolution is generated by a Hermitian Hamiltonian.
- The input and output bases are complete.
- The boundary conditions conserve probability.
- There are no unmodelled loss channels.
- The scattering matrix is properly normalised.

### Cohomological condition

Even if:

\[
\int_{\partial N}A_\Phi
=
0
\pmod{2\pi},
\]

this does not by itself imply:

\[
S^\dagger S = I.
\]

### Logical status

The cohomological condition may constrain a phase, but it does not
establish unitarity.

## Surface-code scaling

### Proposed approximation

\[
P_{\mathrm{logical}}
\sim
C
\left(
\frac{p_{\mathrm{physical}}}{p_{\mathrm{threshold}}}
\right)^{(d+1)/2}.
\]

### Conditions for use

This approximation requires:

- A specified code family.
- A specified code distance \(d\).
- A specified noise model.
- A specified decoder.
- A specified logical operator.
- A specified error metric.
- A specified threshold.
- A specified circuit-level noise model.

### Logical status

The formula is a rough asymptotic scaling relation, not a universal law.

It cannot be used to compare a baseline system with a hypothetical
optimised system unless both systems use identical assumptions except
for the mechanism being tested.

## Gate-fidelity claim

### Proposed claim

A reduction in physical error rate improves logical gate fidelity.

### Valid general principle

In many error-correcting codes, reducing physical error rates can reduce
logical error rates, provided the noise model, decoder, and code
geometry remain fixed.

### Invalid inference

It is invalid to infer a specific gate-fidelity improvement from an
arbitrary reduction in \(p_{\mathrm{physical}}\).

### Required derivation

To claim a gate-fidelity improvement, one must specify:

- The physical error model.
- The decoder.
- The code distance.
- The logical gate.
- The logical error rate.
- The baseline and proposed models.
- The statistical protocol.
- The uncertainty estimate.

### Logical status

No gate-fidelity improvement is established by the present model.

## Cohomology claim

### Proposed object

\[
H^1_{\mathrm{Kayad}}(M,N;U(1)).
\]

### Required construction

To define this object, one must specify:

- The topological space \(M\).
- The subspace \(N\).
- The coefficient system.
- The chain complex.
- The coboundary operator.
- The connection or gauge field.
- The relation to standard relative cohomology.

### Logical status

Until these objects are defined, the notation is not a well-defined
mathematical object.

Therefore, no cancellation theorem can be derived.

## What can currently be derived

From the current assumptions, the only valid derivation is:

\[
\frac{\tau_{\mathrm{supra}}}{\tau_{\mathrm{atome}}}
=
10^{-6}.
\]

And, given the ad hoc convention:

\[
10^{-6/\Delta_\Phi}
=
\frac{1}{\log_{10}\left(105^{49}\right)},
\]

one may derive:

\[
\Delta_\Phi
\approx
3.0063.
\]

## What cannot currently be derived

The following cannot be derived from the present assumptions:

- A physical value of \(\Delta_\Phi\).
- A stable interface.
- A unitary scattering matrix.
- Suppression of thermal noise.
- Suppression of decoherence.
- Improvement of logical gate fidelity.
- Improvement of a surface code.
- Stabilisation of Willow.
- Validation of SCCI-2026.
- Validation of any 105-qubit processor.

## Required next step

Before any simulation, the following must be completed:

1. Define the Hilbert space.
2. Define the Hamiltonian.
3. Define the noise model.
4. Define the boundary conditions.
5. Define the input and output channels.
6. Define the observable being measured.
7. Define the baseline model.
8. Define the proposed model.
9. Define the statistical comparison.
10. Define the failure condition.

## Version

This document is version 0.1.0 of the exploratory quantum-interface
hypothesis.

It is subject to revision whenever a definition, assumption, derivation,
simulation, or experimental result changes.
