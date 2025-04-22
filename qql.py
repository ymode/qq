#!/usr/bin/env python3
"""
Legacy shim for `qql` – kept for backward‑compatibility.
It simply delegates to `qq` with the `--model llama` flag.
"""

import os
import runpy
import sys
from pathlib import Path

# Build arguments by injecting --model llama right after program name
argv = ["qq", "--model", "llama", *sys.argv[1:]]

# Execute qq.py in the current package with the modified arguments
qq_path = Path(__file__).with_name("qq.py")
sys.argv = argv
runpy.run_path(str(qq_path), run_name="__main__")