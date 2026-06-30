import subprocess
import sys
from pathlib import Path


def run(cmd: list[str], label: str) -> None:
    print(f"\n=== {label} ===")
    result = subprocess.run(cmd, cwd=Path(__file__).resolve().parent.parent, text=True)
    if result.returncode != 0:
        raise SystemExit(f"{label} failed with exit code {result.returncode}")
    print(result.stdout, end="")


def main() -> None:
    run([sys.executable, "-m", "pytest", "tests/test_smoke.py"], "Running smoke tests")
    run([sys.executable, "scripts/generate_mlflow_data.py"], "Generating MLflow experiment data")
    run([sys.executable, "scripts/register_model_demo.py"], "Registering model versions")


if __name__ == "__main__":
    main()
