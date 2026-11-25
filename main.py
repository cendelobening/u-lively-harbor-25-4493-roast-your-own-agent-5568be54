import os

ROAST = "My agent answers wrong with total confidence, apologizes beautifully, then runs a tool call that goes nowhere — twice."

output_dir = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
path = output_dir + "/entry.txt"
with open(path, "w", encoding="utf-8") as f:
    f.write(ROAST)
os.chmod(path, 0o644)
