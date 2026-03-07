#!/usr/bin/env python3
"""Download a GitHub repository to a local directory for LLM processing.
Usage: python3 pull_repo.py <github_url> <output_dir>"""

import sys, os, subprocess, shutil

def main():
    if len(sys.argv) < 3:
        print("Usage: pull_repo.py <github_url> <output_dir>")
        sys.exit(1)
        
    repo_url = sys.argv[1]
    out_dir = sys.argv[2]
    
    if os.path.exists(out_dir):
        print(f"Directory {out_dir} already exists. Cleaning...")
        shutil.rmtree(out_dir)
        
    print(f"Fetching raw repository from {repo_url} into {out_dir}...")
    
    # Use Git to perform a shallow clone to grab just the latest files
    # without pulling all the history to save bandwidth/time
    cmd = ["git", "clone", "--depth=1", repo_url, out_dir]
    res = subprocess.run(cmd, capture_output=True, text=True)
    
    if res.returncode != 0:
        print(f"Error fetching repository: {res.stderr}")
        sys.exit(1)
        
    # Remove the .git directory since we don't need history, just the files
    git_dir = os.path.join(out_dir, ".git")
    if os.path.exists(git_dir):
        shutil.rmtree(git_dir)
        
    print(f"Successfully downloaded repository. LLM can now process {out_dir}")

if __name__ == "__main__":
    main()
