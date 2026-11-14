"""Builds the Calibrations section of the site from calibrations/ (run by mkdocs-gen-files).

- Every notebook in calibrations/ becomes a page under notes/calibration/, titled by its
  first "# " heading. A new notebook needs no symlink and no nav edit.
- Every CSV in calibrations/results/ becomes a table on a Results page (mkdocs-table-reader).
- The section's nav is written to notes/calibration/SUMMARY.md (mkdocs-literate-nav).
"""
import json
from pathlib import Path

import mkdocs_gen_files

SRC = Path("calibrations")
DST = Path("notes/calibration")


def title_of(nb):
    for cell in json.loads(nb.read_text())["cells"]:
        if cell["cell_type"] == "markdown":
            for line in "".join(cell["source"]).splitlines():
                if line.startswith("# "):
                    return line[2:].strip()
    return nb.stem.replace("_", " ").capitalize()


titles = {}
for nb in sorted(SRC.glob("*.ipynb")):
    titles[nb.stem] = title_of(nb)
    with mkdocs_gen_files.open(DST / nb.name, "w") as f:
        f.write(nb.read_text())

results = ["# Results", "",
           "The fleet table each calibration notebook writes to `calibrations/results/`, "
           "read when the site is built."]
for csv in sorted((SRC / "results").glob("*.csv")):
    name = titles.get(csv.stem, csv.stem)
    link = f"[notebook]({csv.stem}.ipynb)" if csv.stem in titles else ""
    results += ["", f"## {name}", "", link, "",
                f"{{{{ read_csv('{csv.as_posix()}', floatfmt='.4g') }}}}"]
with mkdocs_gen_files.open(DST / "results.md", "w") as f:
    f.write("\n".join(results) + "\n")

nav = ["* [Calibrations](index.md)"]
nav += [f"* [{titles[stem]}]({stem}.ipynb)" for stem in titles]
nav += ["* [Results](results.md)"]
with mkdocs_gen_files.open(DST / "SUMMARY.md", "w") as f:
    f.write("\n".join(nav) + "\n")
