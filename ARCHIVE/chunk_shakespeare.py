#!/usr/bin/env python3
"""
Shakespeare text chunking script.
Splits the complete Shakespeare text into 16 chunks with 1KB overlaps.
"""

import json
import os
import re

def find_clean_break(text, start_pos, preferred_pos, max_pos, overlap_size=0):
    """
    Find a clean break point in the text, preferring paragraph breaks over sentence breaks.
    
    Args:
        text: The full text
        start_pos: Starting position to search from
        preferred_pos: Preferred position for the break
        max_pos: Maximum allowed position for the break
        overlap_size: Size of overlap to subtract from positions
    
    Returns:
        The position of the clean break
    """
    # Ensure we don't go beyond the text length
    max_pos = min(max_pos, len(text))
    
    # First, look for paragraph breaks (double newlines) near the preferred position
    search_start = max(start_pos, preferred_pos - 5000)
    search_end = min(max_pos, preferred_pos + 5000)
    
    # Find all paragraph breaks in the search range
    paragraph_breaks = []
    for i in range(search_start, search_end - 1):
        if text[i:i+2] == '\n\n':
            paragraph_breaks.append(i + 2)  # Position after the double newline
    
    # If we found paragraph breaks, use the one closest to preferred position
    if paragraph_breaks:
        closest_break = min(paragraph_breaks, key=lambda x: abs(x - preferred_pos))
        return closest_break
    
    # If no paragraph breaks, look for sentence endings
    sentence_end_pattern = re.compile(r'[.!?]\s+')
    matches = list(sentence_end_pattern.finditer(text, search_start, search_end))
    
    if matches:
        # Find the match closest to the preferred position
        closest_match = min(matches, key=lambda m: abs(m.end() - preferred_pos))
        return closest_match.end()
    
    # If no clean breaks found, return the preferred position
    return min(preferred_pos, max_pos)

def create_chunks(file_path, num_chunks=16, overlap_size=1024):
    """
    Create chunks from a text file with specified overlap.
    
    Args:
        file_path: Path to the input file
        num_chunks: Number of chunks to create
        overlap_size: Size of overlap between chunks in characters
    
    Returns:
        List of chunk metadata
    """
    # Read the entire file
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    total_chars = len(text)
    base_chunk_size = (total_chars + (num_chunks - 1) * overlap_size) // num_chunks
    
    chunks_metadata = []
    current_pos = 0
    
    for i in range(num_chunks):
        # Calculate the ideal end position for this chunk
        if i == num_chunks - 1:
            # Last chunk goes to the end
            end_pos = total_chars
        else:
            ideal_end = current_pos + base_chunk_size
            # Find a clean break near the ideal position
            end_pos = find_clean_break(text, current_pos, ideal_end, total_chars)
        
        # Extract the chunk text
        chunk_text = text[current_pos:end_pos]
        
        # Save the chunk
        chunk_filename = f"chunk_{i+1:02d}.txt"
        chunk_path = os.path.join(os.path.dirname(file_path), chunk_filename)
        
        with open(chunk_path, 'w', encoding='utf-8') as f:
            f.write(chunk_text)
        
        # Create metadata for this chunk
        metadata = {
            "chunk_id": i + 1,
            "filename": chunk_filename,
            "start_position": current_pos,
            "end_position": end_pos,
            "character_count": len(chunk_text),
            "first_50_chars": chunk_text[:50].replace('\n', '\\n') if chunk_text else ""
        }
        
        # Add overlap information if applicable
        if i > 0:
            metadata["overlap_start"] = end_pos - overlap_size
            metadata["overlap_size"] = overlap_size
        
        chunks_metadata.append(metadata)
        
        # Move to the next chunk position (with overlap)
        if i < num_chunks - 1:
            current_pos = max(0, end_pos - overlap_size)
        else:
            current_pos = end_pos
    
    return chunks_metadata

def save_metadata(metadata, output_path):
    """Save chunk metadata to a JSON file."""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2)

def main():
    input_file = "/workspace/shakespeare-translations/shakespeare-complete.txt"
    metadata_file = "/workspace/shakespeare-translations/chunks-metadata.json"
    
    print(f"Processing file: {input_file}")
    
    # Check if file exists
    if not os.path.exists(input_file):
        print(f"Error: File {input_file} not found!")
        return
    
    # Get file size
    file_size = os.path.getsize(input_file)
    print(f"File size: {file_size:,} bytes")
    
    # Create chunks
    print(f"Creating 16 chunks with 1KB overlaps...")
    metadata = create_chunks(input_file, num_chunks=16, overlap_size=1024)
    
    # Save metadata
    save_metadata(metadata, metadata_file)
    print(f"Metadata saved to: {metadata_file}")
    
    # Print summary
    print("\nChunking complete! Summary:")
    print(f"Total chunks created: {len(metadata)}")
    total_chars_with_overlap = sum(chunk['character_count'] for chunk in metadata)
    print(f"Total characters (with overlaps): {total_chars_with_overlap:,}")
    print(f"Average chunk size: {total_chars_with_overlap // len(metadata):,} characters")
    
    # Print first few chunks info
    print("\nFirst 3 chunks:")
    for chunk in metadata[:3]:
        print(f"  Chunk {chunk['chunk_id']:02d}: {chunk['character_count']:,} chars, "
              f"positions {chunk['start_position']:,} - {chunk['end_position']:,}")

if __name__ == "__main__":
    main()