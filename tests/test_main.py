from pathlib import Path
from tempfile import TemporaryDirectory

from h5xrd.main import main


def test_main():
    with TemporaryDirectory() as csv_dir:
        main('data', csv_dir)
        count = 0
        for csv_file in Path(csv_dir).iterdir():
            count += 1
            with csv_file.open("r") as f:
                header = f.readline()
                assert header == "2theta,intensity"
        assert count == 10
