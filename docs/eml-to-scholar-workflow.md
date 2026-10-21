# EML to FilteScholar workflow

Use this procedure when asked to process the latest merged email folder and refresh the FilteScholar summary.

1. From the repository root, identify the latest `merged_YYYYMMDD_YYYYMMDD` directory by the ending date in its name. Use a user-specified directory if they name one explicitly. Confirm the selected directory exists.
2. In `eml_to_Txt.py`, update the default `script_dir` to the selected directory's relative path. Preserve all unrelated existing edits.
3. Run the converter from the repository root with the FilteScholar virtual environment under `$HOME/.local/share/virtualenvs/FilteScholar-*/bin/python`. Use the matching existing environment and verify it can import `bs4`; do not fall back to the system Python or create a repository `.venv`. If the environment or dependency is unavailable, report that instead of installing packages or changing dependency files without a request.
4. Capture the exact timestamped `merged_eml_content_*.txt` path printed by the converter. Confirm the run succeeded and note any input files the converter skipped.
5. In `main.py`, set `new_file` to that exact generated filename. Take the value of `new_file` before changing it and add that filename to the end of `old_files`, removing any duplicate first.
6. Prune `old_files` entries whose embedded `YYYYMMDD` date is earlier than the date one calendar year before the current local date. Keep entries exactly on the cutoff date. Apply the cutoff to every old-file entry, including the previous `new_file`; preserve the order of remaining entries and keep the previous `new_file` last if it is within the cutoff.
7. Run `main.py` from the repository root with the same FilteScholar virtual environment. Confirm it finishes, review its log for missing or skipped inputs, and report the generated `FileScholar.md` path.

Do not run tests as part of this workflow unless the user asks for tests. Keep edits limited to the paths and files needed for the requested run, and preserve unrelated working-tree changes.
