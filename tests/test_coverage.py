#!/usr/bin/env python3
"""
test_coverage.py — Test coverage validation for typst-brain

Usage:
    python3 test_coverage.py              # Run all tests
    python3 test_coverage.py --quick      # Quick validation
    python3 test_coverage.py --verbose    # Detailed output

Exit codes:
    0 = all tests passed
    1 = some tests failed
    2 = test discovery error
"""

import sys
import os
import subprocess
import glob
from pathlib import Path
from datetime import datetime

BRAIN = os.environ.get("TYPST_BRAIN_HOME", str(Path(__file__).parent.parent))
TESTS_DIR = os.path.join(BRAIN, "tests")
CHUNKS_DIR = os.path.join(BRAIN, "chunks")
CORE_DIR = os.path.join(BRAIN, "core")


class TestResult:
    def __init__(self, name, passed, message=""):
        self.name = name
        self.passed = passed
        self.message = message


def test_chunks_exist():
    """Verify all chunk files exist."""
    results = []
    expected = [
        "01-syntax-scripting.md",
        "02-layout-page.md",
        "03-table-figure.md",
        "04-math-symbols.md",
        "05-text-styling.md",
        "06-introspection.md",
        "07-data-loading.md",
    ]
    
    for chunk in expected:
        path = os.path.join(CHUNKS_DIR, chunk)
        if os.path.exists(path):
            results.append(TestResult(f"chunk:{chunk}", True))
        else:
            results.append(TestResult(f"chunk:{chunk}", False, f"Missing: {path}"))
    
    return results


def test_core_files_exist():
    """Verify core files exist."""
    results = []
    core_files = [
        "quick-reference.md",
    ]
    
    for f in core_files:
        path = os.path.join(CORE_DIR, f)
        if os.path.exists(path):
            results.append(TestResult(f"core:{f}", True))
        else:
            results.append(TestResult(f"core:{f}", False, f"Missing: {path}"))
    
    return results


def test_typ_files_compile():
    """Test that .typ files compile without errors."""
    results = []
    typ_files = glob.glob(os.path.join(TESTS_DIR, "*.typ"))
    
    for typ_file in typ_files:
        name = os.path.basename(typ_file)
        try:
            result = subprocess.run(
                ["typst", "compile", typ_file, "/tmp/test-output.pdf"],
                capture_output=True,
                timeout=30
            )
            if result.returncode == 0:
                results.append(TestResult(f"compile:{name}", True))
            else:
                results.append(TestResult(f"compile:{name}", False, result.stderr[:200]))
        except subprocess.TimeoutExpired:
            results.append(TestResult(f"compile:{name}", False, "Timeout"))
        except FileNotFoundError:
            results.append(TestResult(f"compile:{name}", False, "typst not found"))
    
    return results


def test_scripts_syntax():
    """Verify Python scripts have valid syntax."""
    results = []
    scripts_dir = os.path.join(BRAIN, "scripts")
    py_files = glob.glob(os.path.join(scripts_dir, "*.py"))
    
    for py_file in py_files:
        name = os.path.basename(py_file)
        try:
            result = subprocess.run(
                ["python3", "-m", "py_compile", py_file],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                results.append(TestResult(f"syntax:{name}", True))
            else:
                results.append(TestResult(f"syntax:{name}", False, result.stderr[:200]))
        except subprocess.TimeoutExpired:
            results.append(TestResult(f"syntax:{name}", False, "Timeout"))
    
    return results


def run_all_tests(verbose=False):
    """Run all test suites."""
    all_results = []
    
    print("=== Typst-Brain Test Suite ===")
    print(f"Started: {datetime.now().isoformat()}")
    print()
    
    # Run test suites
    all_results.extend(test_chunks_exist())
    all_results.extend(test_core_files_exist())
    all_results.extend(test_scripts_syntax())
    all_results.extend(test_typ_files_compile())
    
    # Summary
    passed = sum(1 for r in all_results if r.passed)
    failed = sum(1 for r in all_results if not r.passed)
    
    print(f"\n=== Results ===")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    
    if verbose:
        print("\n=== Details ===")
        for r in all_results:
            status = "✓" if r.passed else "✗"
            print(f"  {status} {r.name}")
            if not r.passed and r.message:
                print(f"    {r.message}")
    
    print(f"\nCompleted: {datetime.now().isoformat()}")
    
    return 0 if failed == 0 else 1


def main():
    verbose = "--verbose" in sys.argv or "-v" in sys.argv
    quick = "--quick" in sys.argv or "-q" in sys.argv
    
    if quick:
        # Quick mode: only check file existence
        results = test_chunks_exist() + test_core_files_exist()
        failed = sum(1 for r in results if not r.passed)
        print(f"Quick check: {len(results) - failed}/{len(results)} passed")
        return 0 if failed == 0 else 1
    
    return run_all_tests(verbose=verbose)


if __name__ == "__main__":
    sys.exit(main())
