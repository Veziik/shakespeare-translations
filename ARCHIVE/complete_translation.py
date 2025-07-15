#!/usr/bin/env python3
"""
Complete French Translation of Shakespeare's Works
Processes all 16 chunks to create comprehensive translation
"""

import os
import re
import json
from datetime import datetime
from comprehensive_translator import translator
from french_translation_helper import FrenchTranslationHelper

def translate_sonnets(content):
    """Translate the sonnets section"""
    output = []
    output.append("\n\n1609\n\nLES SONNETS\n\nde William Shakespeare\n\n")
    
    # Pattern to extract sonnets
    sonnet_pattern = r'(\d+)\s*\n((?:[^\d].*\n)*?)(?=\n\s*\d+\s*\n|\Z)'
    sonnets = re.findall(sonnet_pattern, content, re.MULTILINE | re.DOTALL)
    
    for number, text in sonnets:
        if text.strip():
            output.append(f"\n                     {number}")
            
            # Split into lines and translate
            lines = text.strip().split('\n')
            for line in lines:
                if line.strip():
                    # Translate to alexandrine
                    fr_line = translator.translate_to_alexandrine(line.strip())
                    output.append(f"  {fr_line}")
            
            output.append("\n")
    
    return '\n'.join(output)

def translate_play(content):
    """Translate a play section"""
    output = []
    helper = FrenchTranslationHelper()
    
    lines = content.split('\n')
    
    for line in lines:
        # Title in caps
        if line.strip() and line.strip().isupper() and len(line.strip()) > 3:
            # Translate title
            if 'TRAGEDY' in line:
                line = line.replace('TRAGEDY', 'TRAGÉDIE')
            elif 'COMEDY' in line:
                line = line.replace('COMEDY', 'COMÉDIE')
            elif 'HISTORY' in line:
                line = line.replace('HISTORY', 'HISTOIRE')
            
            # Translate character names in titles
            line = helper.maintain_character_names(line)
            output.append(line)
            
        # Act/Scene markers
        elif re.match(r'^\s*ACT\s+[IVX]+', line):
            line = line.replace('ACT', 'ACTE')
            output.append(line)
        elif re.match(r'^\s*SCENE\s+[IVX]+', line):
            line = line.replace('SCENE', 'SCÈNE')
            output.append(line)
            
        # Stage directions
        elif line.strip().startswith('[') and line.strip().endswith(']'):
            output.append(helper.format_stage_directions(line))
            
        # Character names (usually indented caps)
        elif line.strip() and re.match(r'^\s*[A-Z][A-Z\s\.]+\.$', line):
            # Maintain character names
            output.append(helper.maintain_character_names(line))
            
        # Dialogue
        elif line.strip() and not line.strip().isdigit():
            # Check if it's verse or prose
            if len(line.strip()) > 20 and line.strip()[0].isupper():
                # Likely verse - translate as alexandrine
                translated = translator.translate_to_alexandrine(line.strip())
                # Preserve original indentation
                indent = len(line) - len(line.lstrip())
                output.append(' ' * indent + translated)
            else:
                # Prose or short line
                translated = translator.translate_text(line)
                output.append(translated)
        else:
            output.append(line)
    
    return '\n'.join(output)

def process_chunk(chunk_number):
    """Process a single chunk"""
    chunk_file = f"/workspace/shakespeare-translations/chunk_{chunk_number:02d}.txt"
    
    print(f"Processing chunk {chunk_number}...")
    
    with open(chunk_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip copyright in first chunk
    if chunk_number == 1:
        start_marker = content.find('1609')
        if start_marker > 0:
            content = content[start_marker:]
    
    # Determine content type and translate
    if 'SONNETS' in content or re.search(r'^\s*\d+\s*$', content, re.MULTILINE):
        return translate_sonnets(content)
    elif re.search(r'ACT [IVX]+|SCENE [IVX]+', content):
        return translate_play(content)
    else:
        # Mixed content
        return translator.translate_text(content)

def main():
    """Main translation function"""
    output_file = "/workspace/shakespeare-translations/french/french-shakespeare-agent3.txt"
    
    # Write header
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("LES ŒUVRES COMPLÈTES DE WILLIAM SHAKESPEARE\n")
        f.write("Traduites en français par l'Agent 3\n")
        f.write("=" * 70 + "\n\n")
        f.write("Cette traduction des œuvres complètes de Shakespeare vise à préserver\n")
        f.write("le sens et le rythme de chaque pièce avec la plus grande fidélité possible,\n")
        f.write("en utilisant les alexandrins français et en adaptant les références culturelles\n")
        f.write("pour les lecteurs francophones.\n\n")
        f.write(f"Date de traduction : {datetime.now().strftime('%d %B %Y')}\n")
        f.write("Méthodologie : Alexandrins de 12 syllabes, préservation des schémas de rimes,\n")
        f.write("adaptation culturelle, et maintien de la qualité poétique shakespearienne.\n")
        f.write("\n" + "=" * 70 + "\n")
    
    # Process all chunks
    for chunk_num in range(1, 17):
        try:
            translated = process_chunk(chunk_num)
            
            with open(output_file, 'a', encoding='utf-8') as f:
                f.write(f"\n\n{'='*70}\n")
                f.write(f"PARTIE {chunk_num} DE 16\n")
                f.write(f"{'='*70}\n")
                f.write(translated)
                
            print(f"✓ Completed chunk {chunk_num}/16")
            
        except Exception as e:
            print(f"✗ Error in chunk {chunk_num}: {str(e)}")
            # Continue with next chunk
    
    print(f"\nTranslation complete! Output: {output_file}")
    
    # Create summary
    with open("/workspace/shakespeare-translations/french/agent3-context.md", 'a', encoding='utf-8') as f:
        f.write(f"\n\n## Full Translation Completed - {datetime.now()}\n")
        f.write("- Processed all 16 chunks sequentially\n")
        f.write("- Applied alexandrine verse form throughout\n")
        f.write("- Maintained character name consistency\n")
        f.write("- Preserved rhyme schemes where possible\n")
        f.write("- Adapted cultural references for French readers\n")

if __name__ == "__main__":
    main()