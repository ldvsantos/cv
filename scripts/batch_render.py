"""
Batch render all modified QMD files.
Reads git diff to find changed files and renders each one.
"""
import subprocess
import os
import sys
import time

# Get list of modified QMD files from git
result = subprocess.run(
    ["git", "diff", "--name-only", "--diff-filter=M"],
    capture_output=True, text=True, encoding="utf-8"
)
files = [f.strip() for f in result.stdout.strip().split("\n") if f.strip().endswith(".qmd")]

print(f"Found {len(files)} modified QMD files to render")
print("=" * 60)

success = 0
failed = 0
skipped = 0

for i, qmd in enumerate(files, 1):
    # Determine the working directory (where _quarto.yml is)
    qmd_path = qmd.replace("/", os.sep)
    qmd_dir = os.path.dirname(qmd_path)
    
    # Find the nearest _quarto.yml going up
    work_dir = qmd_dir
    while work_dir and not os.path.exists(os.path.join(work_dir, "_quarto.yml")):
        parent = os.path.dirname(work_dir)
        if parent == work_dir:
            break
        work_dir = parent
    
    if not os.path.exists(os.path.join(work_dir, "_quarto.yml")):
        print(f"[{i}/{len(files)}] SKIP (no _quarto.yml): {qmd}")
        skipped += 1
        continue
    
    # Calculate relative path from work_dir to qmd
    rel_path = os.path.relpath(qmd_path, work_dir)
    
    t0 = time.time()
    print(f"[{i}/{len(files)}] Rendering: {qmd} ...", end=" ", flush=True)
    
    try:
        proc = subprocess.run(
            ["quarto", "render", rel_path],
            cwd=work_dir,
            capture_output=True, text=True, encoding="utf-8",
            timeout=300  # 5 min per file max
        )
        elapsed = time.time() - t0
        
        if "Output created:" in proc.stderr or "Output created:" in proc.stdout:
            print(f"OK ({elapsed:.1f}s)")
            success += 1
        else:
            # Check if HTML was actually created
            html_path = qmd_path.replace(".qmd", ".html")
            if os.path.exists(html_path):
                print(f"OK ({elapsed:.1f}s)")
                success += 1
            else:
                print(f"WARN ({elapsed:.1f}s)")
                print(f"  stderr: {proc.stderr[:200]}")
                failed += 1
    except subprocess.TimeoutExpired:
        print(f"TIMEOUT (>300s)")
        failed += 1
    except Exception as e:
        print(f"ERROR: {e}")
        failed += 1

print("=" * 60)
print(f"Done: {success} OK, {failed} FAILED, {skipped} SKIPPED out of {len(files)}")
