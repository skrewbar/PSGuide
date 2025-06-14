import os
import sys
import unicodedata
from pathlib import Path


def normalize_filename(path: Path):
    normalized_name = unicodedata.normalize("NFC", path.name)
    if path.name != normalized_name:
        new_path = path.with_name(normalized_name)
        print(f"Normalizing: {normalized_name}")
        path.rename(new_path)
        return True
    return False


def walk_and_normalize(path: Path) -> bool:
    changed = False
    for dirpath, dirnames, filenames in os.walk(path, topdown=False):
        for name in filenames:
            changed |= normalize_filename(Path(dirpath) / name)
        for name in dirnames:
            changed |= normalize_filename(Path(dirpath) / name)
    return changed


def main():
    repo_root = Path.cwd()
    changed = walk_and_normalize(repo_root)

    if changed:
        print(
            "Filenames have been normalized. Please stage the changes and commit again."
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
