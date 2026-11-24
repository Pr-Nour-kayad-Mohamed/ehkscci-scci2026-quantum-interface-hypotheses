#!/usr/bin/env python3
"""Evaluate the numerical consequence of an explicitly declared convention.

This script does not simulate Willow, a 105-qubit processor, a hybrid
quantum interface, a scattering matrix, gate fidelity, noise suppression,
or decoherence suppression.

It only solves the declared convention:

    10^(-6 / Delta_Phi) = 1 / log10(105^49)

The result is a numerical consequence of the convention, not a physical
validation.
"""

import argparse
import json
import math
from pathlib import Path


def compute_delta_phi(
    num_physical_qubits=105,
    surface_code_side_length=7,
    time_ratio_exponent=6.0,
):
    if num_physical_qubits <= 1:
        raise ValueError("num_physical_qubits must be greater than 1.")

    if surface_code_side_length <= 0:
        raise ValueError("surface_code_side_length must be positive.")

    if time_ratio_exponent <= 0:
        raise ValueError("time_ratio_exponent must be positive.")

    code_area = surface_code_side_length ** 2
    log_num_qubits = math.log10(num_physical_qubits)
    inner_log_argument = code_area * log_num_qubits

    if inner_log_argument <= 1:
        raise ValueError("The convention requires inner_log_argument > 1.")

    denominator = math.log10(inner_log_argument)

    if denominator <= 0:
        raise ValueError("The denominator must be positive.")

    return time_ratio_exponent / denominator


def build_report(
    num_physical_qubits=105,
    surface_code_side_length=7,
    time_ratio_exponent=6.0,
):
    delta_phi = compute_delta_phi(
        num_physical_qubits=num_physical_qubits,
        surface_code_side_length=surface_code_side_length,
        time_ratio_exponent=time_ratio_exponent,
    )

    left_hand_side = 10.0 ** (-time_ratio_exponent / delta_phi)
    right_hand_side = 1.0 / (
        (surface_code_side_length ** 2)
        * math.log10(num_physical_qubits)
    )

    residual = abs(left_hand_side - right_hand_side)

    return {
        "model": "SCCI-2026 quantum interface hypothesis",
        "status": "exploratory convention; not a physical validation",
        "inputs": {
            "num_physical_qubits": num_physical_qubits,
            "surface_code_side_length": surface_code_side_length,
            "surface_code_area": surface_code_side_length ** 2,
            "time_ratio_exponent": time_ratio_exponent,
        },
        "intermediate_values": {
            "log10_num_physical_qubits": math.log10(num_physical_qubits),
            "inner_log_argument": (
                (surface_code_side_length ** 2)
                * math.log10(num_physical_qubits)
            ),
            "convention_left_hand_side": left_hand_side,
            "convention_right_hand_side": right_hand_side,
            "absolute_residual": residual,
        },
        "result": {
            "delta_phi": delta_phi,
        },
        "interpretation": {
            "delta_phi_is_physical_constant": False,
            "delta_phi_is_validated_critical_value": False,
            "delta_phi_validates_willow": False,
            "delta_phi_stabilises_105_qubits": False,
            "delta_phi_implies_unitarity": False,
            "delta_phi_implies_noise_suppression": False,
            "delta_phi_implies_gate_fidelity_improvement": False,
        },
        "limitation": (
            "This calculation evaluates only the numerical consequence of "
            "an explicitly declared ad hoc convention. It does not validate "
            "SCCI-2026, Google Willow, any 105-qubit processor, a hybrid "
            "quantum interface, unitarity, noise suppression, or quantum "
            "gate fidelity."
        ),
    }


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Evaluate the numerical consequence of the declared "
            "SCCI-2026 quantum-interface modelling convention."
        )
    )

    parser.add_argument(
        "--num-physical-qubits",
        type=int,
        default=105,
    )

    parser.add_argument(
        "--surface-code-side-length",
        type=int,
        default=7,
    )

    parser.add_argument(
        "--time-ratio-exponent",
        type=float,
        default=6.0,
    )

    parser.add_argument(
        "--output",
        type=str,
        default="results/convention_delta_phi_report.json",
    )

    args = parser.parse_args()

    report = build_report(
        num_physical_qubits=args.num_physical_qubits,
        surface_code_side_length=args.surface_code_side_length,
        time_ratio_exponent=args.time_ratio_exponent,
    )

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2, ensure_ascii=False)
        handle.write("\n")

    print("SCCI-2026 quantum-interface convention report")
    print("---------------------------------------------")
    print(
        "Inputs: "
        f"N_q={args.num_physical_qubits}, "
        f"L={args.surface_code_side_length}, "
        f"time_ratio_exponent={args.time_ratio_exponent}"
    )
    print(
        "Delta_Phi implied by convention: "
        f"{report['result']['delta_phi']:.10f}"
    )
    print(
        "Absolute residual: "
        f"{report['intermediate_values']['absolute_residual']:.3e}"
    )
    print(f"Report written to: {args.output}")
    print()
    print(
        "Status: exploratory convention. This is not a physical validation "
        "of Willow, SCCI-2026, unitarity, noise suppression, or gate fidelity."
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
