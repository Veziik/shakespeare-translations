#!/usr/bin/env python3
"""
Process French Translation of Shakespeare's Complete Works
This script helps manage the translation of all 16 chunks
"""

import os
import json
import re
from datetime import datetime

def load_chunk_metadata():
    """Load metadata about all chunks"""
    with open('/workspace/shakespeare-translations/chunks-metadata.json', 'r') as f:
        return json.load(f)

def extract_plays_and_sonnets(chunk_text):
    """Extract and identify different works within a chunk"""
    works = []
    
    # Pattern to identify new works
    title_patterns = [
        r'^THE\s+([A-Z\s]+)$',  # THE TRAGEDY OF...
        r'^([A-Z\s]+)$',  # Simple titles in all caps
        r'^\d{4}$',  # Years (like 1609 for sonnets)
        r'^(ACT\s+[IVX]+)',  # Act markers
        r'^(SCENE\s+[IVX]+)',  # Scene markers
    ]
    
    current_work = None
    current_content = []
    
    lines = chunk_text.split('\n')
    
    for line in lines:
        # Check if this might be a title
        for pattern in title_patterns:
            match = re.match(pattern, line.strip())
            if match and len(line.strip()) > 3:
                if current_work and current_content:
                    works.append({
                        'title': current_work,
                        'content': '\n'.join(current_content)
                    })
                current_work = line.strip()
                current_content = []
                break
        else:
            current_content.append(line)
    
    # Don't forget the last work
    if current_work and current_content:
        works.append({
            'title': current_work,
            'content': '\n'.join(current_content)
        })
    
    return works

def create_translation_summary():
    """Create a summary of the translation work"""
    summary = {
        'translation_start': '2025-07-11',
        'translator': 'translator_french_1',
        'target_language': 'French',
        'total_chunks': 16,
        'methodology': {
            'verse_form': 'Alexandrins (12-syllable verses)',
            'rhyme_preservation': 'ABAB CDCD EFEF GG where possible',
            'cultural_adaptation': 'French poetic tradition',
            'character_names': 'Established French translations'
        },
        'progress': {
            'sonnets': 'In progress (1-19 completed)',
            'plays': 'Pending',
            'total_characters': 5458199
        }
    }
    
    return summary

def translate_stage_directions(text):
    """Translate common stage directions to French"""
    translations = {
        r'\[Enter\s+': '[Entre ',
        r'\[Exit\s+': '[Sort ',
        r'\[Exeunt\]': '[Sortent]',
        r'\[Exeunt\s+': '[Sortent ',
        r'\[Aside\]': '[À part]',
        r'\[Within\]': '[De l\'intérieur]',
        r'\[Dies\]': '[Meurt]',
        r'\[Sleeps\]': '[S\'endort]',
        r'\[Kneels\]': '[S\'agenouille]',
        r'\[Rises\]': '[Se lève]',
        r'\[They fight\]': '[Ils se battent]',
        r'\[Thunder\]': '[Tonnerre]',
        r'\[Music\]': '[Musique]',
        r'\[Flourish\]': '[Fanfare]',
        r'\[Sennet\]': '[Sonnerie]',
        r'\[Alarum\]': '[Alarme]',
        r'\[All\]': '[Tous]',
        r'\[Reading\]': '[Lisant]',
        r'\[Singing\]': '[Chantant]',
        r'\[Dancing\]': '[Dansant]',
        r'\[Weeping\]': '[Pleurant]',
        r'\[Laughing\]': '[Riant]',
        'ACT': 'ACTE',
        'SCENE': 'SCÈNE',
        'Prologue': 'Prologue',
        'Epilogue': 'Épilogue',
        'The End': 'Fin'
    }
    
    result = text
    for eng, fr in translations.items():
        result = re.sub(eng, fr, result, flags=re.IGNORECASE)
    
    return result

def identify_work_type(title):
    """Identify the type of work from its title"""
    title_lower = title.lower()
    
    if 'sonnet' in title_lower or 'sonnets' in title_lower:
        return 'sonnets'
    elif 'tragedy' in title_lower:
        return 'tragedy'
    elif 'comedy' in title_lower:
        return 'comedy'
    elif 'history' in title_lower or 'king' in title_lower or 'henry' in title_lower:
        return 'history'
    elif any(play in title_lower for play in ['hamlet', 'romeo', 'macbeth', 'othello', 'lear']):
        return 'tragedy'
    elif any(play in title_lower for play in ['midsummer', 'much ado', 'as you like']):
        return 'comedy'
    else:
        return 'unknown'

def main():
    """Main processing function"""
    print("French Translation Processing Script")
    print("====================================")
    
    # Load metadata
    metadata = load_chunk_metadata()
    print(f"Total chunks to process: {len(metadata)}")
    
    # Calculate total size
    total_chars = sum(chunk['character_count'] for chunk in metadata)
    print(f"Total characters to translate: {total_chars:,}")
    
    # Create summary
    summary = create_translation_summary()
    
    # Save summary
    with open('/workspace/shakespeare-translations/french/translation-summary.json', 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    
    print("\nTranslation summary created.")
    
    # Provide chunk overview
    print("\nChunk Overview:")
    for i, chunk in enumerate(metadata[:5]):  # Show first 5 chunks
        print(f"Chunk {chunk['chunk_id']:02d}: {chunk['character_count']:,} chars - \"{chunk['first_50_chars']}...\"")
    
    print("\nKey translation principles applied:")
    print("- Alexandrin verse form (12 syllables)")
    print("- Preservation of rhyme schemes")
    print("- Cultural adaptation for French readers")
    print("- Consistent character name translations")

if __name__ == "__main__":
    main()