##pip install pysradbx

import subprocess
import sys 

# -------- CONFIGURATION --------
GSE_ID = sys.argv[1]
# --------------------------------

def run_cmd(command):
    """Run a shell command and print its output live."""
    print(f"\n[Running] {command}")
    subprocess.run(command, shell=True, check=True)

def get_srp_from_file(file_path):
    """Read SRP ID from sra.txt (skips header)."""
    with open(file_path, "r") as f:
        lines = f.read().strip().splitlines()
    if len(lines) < 2:
        raise ValueError(f"No SRP ID found in {file_path}")
    # Second column of the second line
    return lines[1].split()[1]

# Step 1: Download GEO study data
run_cmd(f"pysradb download -g {GSE_ID} --out-dir {GSE_ID}")

# Step 2: Map GSE to SRP and save to sra.txt
run_cmd(f"pysradb gse-to-srp {GSE_ID} > sra.txt")

# Step 3: Read SRP ID from file
SRP_ID = get_srp_from_file("sra.txt")
print(f"\n[Info] Found SRP ID: {SRP_ID}")

# Step 4: Get detailed metadata for SRP ID
run_cmd(f"pysradb metadata {SRP_ID} --detailed > {GSE_ID}/{GSE_ID}.tsv")

run_cmd(f"rm -rf sra.txt")

print("\n✅ All steps completed successfully!")
