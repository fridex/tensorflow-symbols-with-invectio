from invectio import gather_symbols_provided
from thoth.python import Source
import json
import os
import requests
import zipfile


def main() -> None:
    """Obtain symbols provided by TensorFlow in various releases."""
    pypi = Source("https://pypi.org/simple")

    os.makedirs("data", exist_ok=True)

    for tensorflow_version in pypi.get_package_versions("tensorflow"):
        print(f"Obtaining info for TensorFlow in version {tensorflow_version!r}")
        artifacts = [a for a in pypi.get_package_artifacts("tensorflow", tensorflow_version) if "manylinux" in a.artifact_name]
        if len(artifacts) == 0:
            print(f"!!! no artifacts to download for TensorFlow in version {tensorflow_version}")
            continue

        artifacts[0]._extract_py_module()
        symbols = gather_symbols_provided(artifacts[0].dir_name, ignore_errors=True)

        with open(f"data/tensorflow-{tensorflow_version}.json", "w") as f:
            json.dump(symbols, f, sort_keys=True, indent=2)


__name__ == "__main__" and main()
