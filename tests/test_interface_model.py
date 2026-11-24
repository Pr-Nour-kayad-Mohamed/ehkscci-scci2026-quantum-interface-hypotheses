#!/usr/bin/env python3
"""Tests for the SCCI-2026 quantum-interface convention calculator.

These tests verify only the mathematical consistency of the declared
modelling convention.

They do not validate Willow, any 105-qubit processor, a hybrid quantum
interface, unitarity, noise suppression, or gate fidelity.
"""

import json
import math
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from interface_model import build_report, compute_delta_phi


class TestDeltaPhiConvention(unittest.TestCase):
    def test_01_default_delta_phi_value(self):
        delta_phi = compute_delta_phi()
        expected = 3.0063086330189743
        self.assertAlmostEqual(delta_phi, expected, places=12)

    def test_02_absolute_residual_is_zero(self):
        report = build_report()
        residual = report["intermediate_values"]["absolute_residual"]
        self.assertAlmostEqual(residual, 0.0, places=15)

    def test_03_default_inputs_are_correct(self):
        report = build_report()
        inputs = report["inputs"]
        self.assertEqual(inputs["num_physical_qubits"], 105)
        self.assertEqual(inputs["surface_code_side_length"], 7)
        self.assertEqual(inputs["surface_code_area"], 49)
        self.assertEqual(inputs["time_ratio_exponent"], 6.0)

    def test_04_intermediate_log_value_is_correct(self):
        report = build_report()
        expected_log = math.log10(105)
        actual_log = report["intermediate_values"]["log10_num_physical_qubits"]
        self.assertAlmostEqual(actual_log, expected_log, places=15)

    def test_05_inner_log_argument_is_correct(self):
        report = build_report()
        expected = 49 * math.log10(105)
        actual = report["intermediate_values"]["inner_log_argument"]
        self.assertAlmostEqual(actual, expected, places=15)

    def test_06_rejects_non_positive_qubit_count(self):
        with self.assertRaises(ValueError):
            compute_delta_phi(num_physical_qubits=0)

    def test_07_rejects_non_positive_code_side_length(self):
        with self.assertRaises(ValueError):
            compute_delta_phi(surface_code_side_length=0)

    def test_08_rejects_non_positive_time_ratio_exponent(self):
        with self.assertRaises(ValueError):
            compute_delta_phi(time_ratio_exponent=0)

    def test_09_report_status_is_exploratory(self):
        report = build_report()
        self.assertEqual(
            report["status"],
            "exploratory convention; not a physical validation",
        )

    def test_10_report_does_not_claim_willow_validation(self):
        report = build_report()
        interpretation = report["interpretation"]
        self.assertFalse(interpretation["delta_phi_validates_willow"])
        self.assertFalse(interpretation["delta_phi_stabilises_105_qubits"])

    def test_11_report_does_not_claim_unitarity(self):
        report = build_report()
        self.assertFalse(
            report["interpretation"]["delta_phi_implies_unitarity"]
        )

    def test_12_report_does_not_claim_noise_suppression(self):
        report = build_report()
        self.assertFalse(
            report["interpretation"]["delta_phi_implies_noise_suppression"]
        )

    def test_13_report_does_not_claim_gate_fidelity_improvement(self):
        report = build_report()
        self.assertFalse(
            report["interpretation"][
                "delta_phi_implies_gate_fidelity_improvement"
            ]
        )

    def test_14_report_contains_limitation(self):
        report = build_report()
        self.assertIn("does not validate", report["limitation"])

    def test_15_command_line_creates_json_report(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_path = Path(temporary_directory) / "report.json"

            result = subprocess.run(
                [
                    sys.executable,
                    "src/interface_model.py",
                    "--output",
                    str(output_path),
                ],
                capture_output=True,
                text=True,
                check=True,
            )

            self.assertIn(
                "Delta_Phi implied by convention",
                result.stdout,
            )
            self.assertTrue(output_path.exists())

            with output_path.open("r", encoding="utf-8") as handle:
                report = json.load(handle)

            self.assertIn("result", report)
            self.assertIn("delta_phi", report["result"])

    def test_16_command_line_uses_custom_qubit_count(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_path = Path(temporary_directory) / "custom_report.json"

            subprocess.run(
                [
                    sys.executable,
                    "src/interface_model.py",
                    "--num-physical-qubits",
                    "200",
                    "--output",
                    str(output_path),
                ],
                capture_output=True,
                text=True,
                check=True,
            )

            with output_path.open("r", encoding="utf-8") as handle:
                report = json.load(handle)

            self.assertEqual(
                report["inputs"]["num_physical_qubits"],
                200,
            )


if __name__ == "__main__":
    unittest.main()
