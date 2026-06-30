from pathlib import Path


def test_repo_smoke_paths_exist():
    required = [
        Path("configs/data.yaml"),
        Path("scripts/generate_mlflow_data.py"),
        Path("scripts/register_model_demo.py"),
    ]
    for path in required:
        assert path.exists(), f"Missing expected path: {path}"


def test_mlflow_import():
    import mlflow  # noqa: F401

    assert mlflow.__version__
