#!/usr/bin/env python3
"""
Translation Verification Script
Ensures translations meet minimum size requirements
"""

import os
import sys

def verify_translation(filepath, min_lines=80000, min_chars=3000000):
    """Verify a translation file meets minimum requirements."""
    if not os.path.exists(filepath):
        return False, "File does not exist"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')
        
    line_count = len(lines)
    char_count = len(content)
    
    if line_count < min_lines:
        return False, f"Insufficient lines: {line_count:,} < {min_lines:,}"
    
    if char_count < min_chars:
        return False, f"Insufficient characters: {char_count:,} < {min_chars:,}"
    
    return True, f"Valid: {line_count:,} lines, {char_count:,} characters"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python verify_translation.py <translation_file>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    valid, message = verify_translation(filepath)
    
    print(f"File: {filepath}")
    print(f"Status: {'PASS' if valid else 'FAIL'}")
    print(f"Details: {message}")
    
    sys.exit(0 if valid else 1)