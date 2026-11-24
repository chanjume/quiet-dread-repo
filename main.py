import os

ENTRY = "LGTM — the 2 a.m. deploy this approves will outlive us both, and the on-call rotation already knows it."

assert len(ENTRY) <= 140, "entry must be a single line of at most 140 characters"
assert "\n" not in ENTRY, "entry must be a single line"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
