#!/usr/bin/env python3
"""
Translation Manager - Monitors and manages translation tasks
"""

import os
import time
import subprocess

class TranslationManager:
    def __init__(self):
        self.languages = ['italian', 'spanish', 'french', 'japanese']
        self.agents = [1, 2, 3, 4]
        self.min_lines = 80000
        self.min_chars = 3000000
        self.source_lines = 124456
        self.source_chars = 5458199
        
    def check_translation(self, lang, agent):
        """Check if a translation meets requirements."""
        filepath = f"/workspace/shakespeare-translations/{lang}/{lang}-shakespeare-agent{agent}-complete.txt"
        if not os.path.exists(filepath):
            # Try original filename
            filepath = f"/workspace/shakespeare-translations/{lang}/{lang}-shakespeare-agent{agent}.txt"
        
        if not os.path.exists(filepath):
            return False, 0, 0, "File not found"
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = len(content.split('\n'))
            chars = len(content)
        
        complete = lines >= self.min_lines and chars >= self.min_chars
        percent = (lines / self.source_lines) * 100
        
        return complete, lines, chars, f"{percent:.1f}% complete"
    
    def get_status_report(self):
        """Generate status report for all translations."""
        report = ["# Translation Status Report\n"]
        report.append(f"Target: {self.min_lines:,} lines, {self.min_chars:,} characters\n")
        report.append(f"Source: {self.source_lines:,} lines, {self.source_chars:,} characters\n\n")
        
        for lang in self.languages:
            report.append(f"## {lang.title()}\n")
            total_lines = 0
            for agent in self.agents:
                complete, lines, chars, status = self.check_translation(lang, agent)
                total_lines += lines
                emoji = "✅" if complete else "❌"
                report.append(f"- Agent {agent}: {emoji} {lines:,} lines, {chars:,} chars ({status})\n")
            
            lang_percent = (total_lines / (self.source_lines * 4)) * 100
            report.append(f"- **Total Progress**: {lang_percent:.1f}% of required translations\n\n")
        
        return "".join(report)
    
    def identify_incomplete(self):
        """Identify which translations need to be restarted."""
        incomplete = []
        for lang in self.languages:
            for agent in self.agents:
                complete, lines, chars, status = self.check_translation(lang, agent)
                if not complete:
                    incomplete.append({
                        'language': lang,
                        'agent': agent,
                        'current_lines': lines,
                        'current_chars': chars,
                        'status': status
                    })
        return incomplete

if __name__ == "__main__":
    manager = TranslationManager()
    print(manager.get_status_report())
    
    incomplete = manager.identify_incomplete()
    print(f"\n## Incomplete Translations: {len(incomplete)}")
    for task in incomplete:
        print(f"- {task['language']} Agent {task['agent']}: {task['current_lines']:,} lines ({task['status']})")