#!/usr/bin/env python3
"""
Helper script to process Shakespeare chunks for translation
"""

import os
import re

def extract_content_sections(chunk_path, start_line=0, num_lines=100):
    """Extract specific lines from a chunk file"""
    with open(chunk_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Skip to start_line and get num_lines
    return lines[start_line:start_line+num_lines]

def find_shakespeare_start(chunk_path):
    """Find where actual Shakespeare content begins (after headers)"""
    with open(chunk_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines):
        # Look for typical Shakespeare work titles or sonnet numbers
        if re.match(r'^\s*(THE SONNETS|COMEDY|TRAGEDY|HISTORY|\d+)\s*$', line):
            return i
    return 0

def get_chunk_info(chunk_num):
    """Get information about a specific chunk"""
    chunk_path = f"/workspace/shakespeare-translations/chunk_{chunk_num:02d}.txt"
    if not os.path.exists(chunk_path):
        return None
    
    with open(chunk_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    start_idx = find_shakespeare_start(chunk_path)
    
    # Extract first meaningful content
    content_preview = []
    for i in range(start_idx, min(start_idx + 50, len(lines))):
        if lines[i].strip():
            content_preview.append(lines[i].rstrip())
        if len(content_preview) >= 10:
            break
    
    return {
        'chunk_num': chunk_num,
        'total_lines': len(lines),
        'content_start': start_idx,
        'preview': content_preview
    }

# Analyze all chunks
if __name__ == "__main__":
    print("Analyzing Shakespeare chunks...")
    for i in range(1, 17):
        info = get_chunk_info(i)
        if info:
            print(f"\nChunk {i:02d}:")
            print(f"  Total lines: {info['total_lines']}")
            print(f"  Content starts at line: {info['content_start']}")
            print(f"  Preview: {info['preview'][0] if info['preview'] else 'N/A'}")