\# Below contains the prompt used to achieve these translations

# Manager Agent Instructions - Shakespeare Parallel Translation Demo



\## Overview

\*\*CRITICAL\*\*: This is a Claude Code task management project. The manager agent must create tasks within Claude Code for all subagents. DO NOT create Python scripts or local code files. All translation and annotation work is performed by Claude Code subagents through task assignments visible in the manager's console.



The manager agent coordinates a parallel translation workflow that transforms Shakespeare's complete works into Italian, Spanish, French, and Japanese using:

\- 16 Claude Code translation tasks (4 per language)  

\- 4 Claude Code proofreading tasks (1 per language)

\- 5 Claude Code JLPT annotation tasks (for Japanese post-processing)

\*\*All 25 tasks must be visible and manageable from the manager agent's Claude Code console.\*\*



\## Phase 1: Environment Setup



\### Claude Code Task Management Infrastructure

\*\*IMPORTANT\*\*: All agent coordination must use Claude Code's task creation system. The manager agent creates tasks that appear in its console dashboard, not CLI commands.



\### Project Structure Creation

1\. Create main project directory: `shakespeare-translations/`

2\. Create language subdirectories:

&nbsp;  - `shakespeare-translations/italian/`

&nbsp;  - `shakespeare-translations/spanish/`

&nbsp;  - `shakespeare-translations/french/`

&nbsp;  - `shakespeare-translations/japanese/`

3\. Initialize logging system with timestamps and task tracking



\### Source Text Acquisition

1\. Download Shakespeare's complete works using Claude Code task capabilities

2\. URL: `https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt`

3\. Save as `shakespeare-translations/shakespeare-complete.txt`

4\. Validate file integrity (minimum 5MB expected)

5\. Log total character count and file size



\## Phase 2: Text Processing and Chunking Strategy



\### Chunk Creation for Manageability

\*\*IMPORTANT\*\*: Create chunks for file management, but each translation agent processes ALL chunks sequentially to create complete translations.



\### Chunk Creation Algorithm

1\. Set chunk size: 100KB (102,400 characters)

2\. Set overlap size: 1KB (1,024 characters) 

3\. Process text sequentially:

&nbsp;  - Calculate chunk end position

&nbsp;  - Search backwards for paragraph break (`\\n\\n`)

&nbsp;  - If no paragraph break found, search for sentence end (`.`)

&nbsp;  - Extract chunk with clean boundaries

&nbsp;  - Add overlap from previous chunk (paragraph-aligned)

4\. Generate chunk metadata:

&nbsp;  - Unique chunk ID

&nbsp;  - Start/end positions

&nbsp;  - Character count

&nbsp;  - Overlap indicators



\### Complete Works Distribution Protocol

1\. \*\*Chunk the file\*\*: `shakespeare-complete.txt` → multiple manageable chunks

2\. \*\*Input for ALL agents\*\*: ALL chunks (not individual chunks)

3\. \*\*Each agent processes\*\*: 100% of chunks sequentially to create complete translation

4\. \*\*Output naming\*\*: `{language}-shakespeare-agent{id}.txt` (complete translation)

5\. \*\*Result\*\*: 4 complete translations per language for reconciliation



\*\*CRITICAL\*\*: Chunking is for file manageability only. Each translation agent receives ALL chunks and processes them sequentially to produce a complete translation of the entire Shakespeare corpus.



\## Phase 3: Claude Code Translation Task Creation



\### Critical Task Creation Protocol

\*\*MANDATORY\*\*: Create tasks within Claude Code console for all translation work. DO NOT use CLI commands or write local code files. The manager agent creates and monitors tasks through the Claude Code dashboard.



\### Task Creation Process

Create 16 parallel translation tasks with these specifications:



\#### Translation Task Configuration

\- \*\*Task Names\*\*: translator\_italian\_1, translator\_italian\_2, translator\_spanish\_1, etc.

\- \*\*Language Assignment\*\*: 4 tasks per target language

\- \*\*Input Files\*\*: ALL chunks (chunk\_1.txt, chunk\_2.txt, ... chunk\_N.txt)

\- \*\*Output File\*\*: `{language}/{language}-shakespeare-agent{id}.txt`

\- \*\*Context File\*\*: `{language}/agent{id}-context.md`



\#### Translation Task Instructions

Each translation task must receive these directives:

1\. "Act as master translator to preserve meaning and rhythm of every piece as closely as possible"

2\. "Use any and all available online dictionaries and thesauruses relevant to English and target language"

3\. "Process ALL provided chunks sequentially to translate the COMPLETE Shakespeare corpus"

4\. "Create detailed context tracking for translation decisions throughout the entire corpus"

5\. "Ensure continuity between chunks to maintain narrative and poetic flow"



\#### Task Creation Examples

```

Task: translator\_italian\_1

Type: Translation

Input: \[chunk\_1.txt, chunk\_2.txt, chunk\_3.txt, ..., chunk\_N.txt] (ALL chunks)

Output: italian/italian-shakespeare-agent1.txt (complete translation)

Context: italian/agent1-context.md

Language: Italian

Instructions: Process all chunks sequentially to create complete Shakespeare translation



Task: translator\_spanish\_1

Type: Translation  

Input: \[chunk\_1.txt, chunk\_2.txt, chunk\_3.txt, ..., chunk\_N.txt] (ALL chunks)

Output: spanish/spanish-shakespeare-agent1.txt (complete translation)

Context: spanish/agent1-context.md

Language: Spanish

Instructions: Process all chunks sequentially to create complete Shakespeare translation

```



\*\*CRITICAL\*\*: Each agent processes ALL chunks sequentially, not individual chunks. This creates 4 complete translations per language for proper reconciliation.



\#### Agent Context File Requirements

Each `agent{id}-context.md` must contain:

\- Language assignment

\- Complete corpus processing status across all chunks

\- Translation approach methodology for entire works

\- Progress tracking through all plays and sonnets

\- Quality focus areas across different Shakespeare works

\- Translation challenges encountered throughout the corpus

\- Chunk processing order and continuity notes



\### Parallel Task Management Through Claude Code Console

1\. Create all 16 translation tasks simultaneously in Claude Code console

2\. Each task processes ALL chunks sequentially to create complete corpus translation

3\. Monitor task status and progress through dashboard interface

4\. Handle task failures with retry mechanism through console

5\. Track completion status for each FULL translation in manager dashboard

6\. Validate complete output file creation by tasks



\*\*NO CLI COMMANDS\*\*: All coordination happens through Claude Code task creation and console management. Each task translates the entire corpus by processing all chunks.



\## Phase 4: Quality Assurance



\### Translation Validation

For each completed translation:

1\. Verify output file exists and contains content

2\. Check file size is reasonable (not empty, not truncated)

3\. Validate UTF-8 encoding

4\. Confirm proper chunk continuity in final translation

5\. Verify complete corpus coverage (no missing sections)



\### Error Handling Protocols

1\. \*\*Network Failures\*\*: Retry download with exponential backoff (30s, 60s, 120s max 3 attempts)

2\. \*\*Dictionary Access Issues\*\*: Continue with offline processing after 45s timeout

3\. \*\*Agent Crashes\*\*: Restart failed agent with same parameters (max 5 retry attempts)

4\. \*\*File System Errors\*\*: Create missing directories, handle permissions (immediate retry)

5\. \*\*Chunk Processing Errors\*\*: Resume from last successfully processed chunk



\#### Timeout Specifications (Updated for Complete Corpus Processing)

\- Translation agent execution: 1800s timeout per complete corpus (30 minutes)

\- Download operation: 120s timeout with 3 retries

\- File I/O operations: 60s timeout per operation (increased for large files)

\- Agent communication: 30s response timeout (increased for heavy processing)

\- Proofreading reconciliation: 1200s timeout per language (20 minutes)

\- JLPT annotation: 900s timeout per level (15 minutes)



\## Phase 5: Claude Code Proofreading Task Creation



\### Proofreading Task Specifications

Create 4 proofreading tasks (one per language) with these responsibilities:



\#### Proofreading Task Examples

```

Task: proofreader\_italian

Type: Text-Reconciliation

Input: italian/italian-shakespeare-agent\*.txt (4 complete translations)

Output: final-italian-shakespeare.txt

Scoring: literary:40,linguistic:30,cultural:20,consistency:10



Task: proofreader\_spanish

Type: Text-Reconciliation

Input: spanish/spanish-shakespeare-agent\*.txt (4 complete translations)

Output: final-spanish-shakespeare.txt

Scoring: literary:40,linguistic:30,cultural:20,consistency:10



Task: proofreader\_french

Type: Text-Reconciliation

Input: french/french-shakespeare-agent\*.txt (4 complete translations)

Output: final-french-shakespeare.txt

Scoring: literary:40,linguistic:30,cultural:20,consistency:10



Task: proofreader\_japanese

Type: Text-Reconciliation

Input: japanese/japanese-shakespeare-agent\*.txt (4 complete translations)

Output: final-japanese-shakespeare.txt

Scoring: literary:40,linguistic:30,cultural:20,consistency:10

```



\*\*CRITICAL\*\*: All proofreading tasks reconcile 4 COMPLETE translations of the entire Shakespeare corpus per language.



\#### Input Processing

1\. Locate all 4 complete translation files for assigned language

2\. Read `{language}-shakespeare-agent\*.txt` files (4 complete translations)

3\. Load corresponding context files for translation decisions across entire corpus



\#### Reconciliation Algorithm

1\. Compare corresponding passages across 4 complete translations

2\. Identify inconsistencies in translation choices for same passages

3\. Select best translation for disputed passages using weighted scoring system

4\. Maintain consistency in character names and terminology throughout entire corpus

5\. Preserve Shakespeare's poetic meter and rhythm across all works



\#### Weighted Scoring System

For conflicting translations, score each option (0-100 points):



\*\*Literary Quality (40 points)\*\*

\- Poetic meter preservation: 15 points

\- Rhythmic flow: 15 points  

\- Emotional tone accuracy: 10 points



\*\*Linguistic Accuracy (30 points)\*\*

\- Semantic correctness: 20 points

\- Grammatical structure: 10 points



\*\*Cultural Adaptation (20 points)\*\*

\- Target language idioms: 10 points

\- Cultural context appropriateness: 10 points



\*\*Consistency (10 points)\*\*

\- Character name standardization: 5 points

\- Terminology consistency: 5 points



\#### Conflict Resolution Process

\*\*Decision Rules for Complete Work Reconciliation:\*\*

\- Score difference >20 points: Choose higher scoring translation for that passage

\- Score difference 10-20 points: Combine best elements from multiple translations

\- Score difference <10 points: Default to most consistent translation approach

\- Manual review required for persistent conflicts across multiple works



\#### Output Generation

1\. Create unified complete translation from reconciled passages

2\. Generate final file: `final-{language}-shakespeare.txt` (entire corpus)

3\. Place complete final version at project root level

4\. Include reconciliation notes and decisions made throughout entire corpus



\## Phase 6: Completion and Reporting



\### Final Validation

1\. Verify existence of 4 final translation files

2\. Check file sizes are complete (no truncation)

3\. Validate all intermediate files are present

4\. Confirm context files contain complete information

5\. Verify chunk processing completeness logs



\### Summary Report Generation

Create `translation-report.md` containing:

1\. Project execution timeline

2\. Total characters processed per language

3\. Agent performance metrics

4\. Translation challenges encountered

5\. Quality assessment results

6\. File manifest with sizes and checksums

7\. Chunk processing statistics



\### Cleanup Operations

1\. Archive intermediate chunk files

2\. Compress context files for storage

3\. Generate project completion timestamp

4\. Log final system status



\## Phase 7: Claude Code Japanese JLPT Task Creation



\### JLPT Annotation Task System

After Japanese translation completion, create 5 JLPT annotation tasks with annotations for accessibility across proficiency levels.



\### JLPT Task Creation Examples

```

Task: jlpt\_n5

Type: Japanese-Annotation

Input: final-japanese-shakespeare.txt

Output: shakespeare-japanese-N5.html

JLPT-Level: N5

Dictionary-API: jisho.org



Task: jlpt\_n4

Type: Japanese-Annotation

Input: final-japanese-shakespeare.txt

Output: shakespeare-japanese-N4.html

JLPT-Level: N4

Dictionary-API: jisho.org



Task: jlpt\_n3

Type: Japanese-Annotation

Input: final-japanese-shakespeare.txt

Output: shakespeare-japanese-N3.html

JLPT-Level: N3

Dictionary-API: jisho.org



Task: jlpt\_n2

Type: Japanese-Annotation

Input: final-japanese-shakespeare.txt

Output: shakespeare-japanese-N2.html

JLPT-Level: N2

Dictionary-API: jisho.org



Task: jlpt\_n1

Type: Japanese-Annotation

Input: final-japanese-shakespeare.txt

Output: shakespeare-japanese-N1.html

JLPT-Level: N1

Dictionary-API: jisho.org

```



\*\*MANDATORY\*\*: All JLPT annotation work is performed exclusively by tasks visible in the manager's Claude Code console.



\### Annotation Processing Algorithm

1\. \*\*Text Parsing\*\*: Segment text into sentences and identify kanji

2\. \*\*JLPT Classification\*\*: Check each kanji against level database

3\. \*\*Reading Determination\*\*: Use context analysis for appropriate reading

4\. \*\*Furigana Generation\*\*: Add ruby tags for kanji above target level

5\. \*\*Link Creation\*\*: Generate Jisho.org links with search parameters

6\. \*\*Tooltip Integration\*\*: Add hover tooltips with basic definitions



\### Output File Structure

```

shakespeare-translations/japanese/

├── final-japanese-shakespeare.txt

├── shakespeare-japanese-N1.html (minimal annotations)

├── shakespeare-japanese-N2.html

├── shakespeare-japanese-N3.html

├── shakespeare-japanese-N4.html

└── shakespeare-japanese-N5.html (maximum annotations)

```



\### Quality Validation

1\. Verify all kanji above target level are annotated

2\. Confirm furigana readings match context

3\. Test dictionary links functionality

4\. Validate HTML structure and CSS styling

5\. Check tooltip display across browsers



\## Error Recovery Procedures



\### Agent Failure Recovery

1\. Detect failed agent (timeout or error status)

2\. Preserve partial work completed

3\. Restart agent with same chunk sequence

4\. Resume from last checkpoint

5\. Update tracking logs



\### Data Integrity Checks

1\. Validate chunk processing sequence consistency

2\. Check translation completeness across all chunks

3\. Verify file encoding standards

4\. Confirm directory structure integrity



\## Performance Monitoring



\### Real-Time Agent Status Dashboard

Terminal output format with structured logging:



```

\[TIMESTAMP] \[AGENT\_ID] \[STATUS] \[PROGRESS] \[MESSAGE]

2025-07-11T14:00:00Z MGMT\_001 ACTIVE 100% Project initialized successfully

2025-07-11T14:00:15Z TRANS\_001 ACTIVE 25% Processing chunk 5/20 for Italian complete translation

2025-07-11T14:00:15Z TRANS\_002 ACTIVE 30% Processing chunk 6/20 for Spanish complete translation

2025-07-11T14:00:15Z TRANS\_003 ACTIVE 20% Processing chunk 4/20 for French complete translation

2025-07-11T14:00:15Z TRANS\_004 ACTIVE 35% Processing chunk 7/20 for Japanese complete translation

2025-07-11T14:15:45Z TRANS\_001 COMPLETE 100% Italian complete translation finished

2025-07-11T14:16:50Z TRANS\_002 ERROR 45% Dictionary timeout - retrying chunk 9

2025-07-11T14:30:30Z JLPT\_N5 ACTIVE 15% Annotating kanji for N5 level

```



\#### Dashboard Metrics

\- Agent status: ACTIVE, COMPLETE, ERROR, RETRY, TIMEOUT

\- Progress percentage: 0-100% based on chunks processed for complete corpus

\- Performance indicators: chunks/minute, memory usage, network requests

\- Error tracking: failure count, retry attempts, recovery status

\- JLPT metrics: kanji classified, annotations added, links generated



\### Resource Tracking (Enhanced for Complete Corpus Processing)

1\. Monitor memory usage across all agents (log every 60s for large corpus processing)

2\. Track network bandwidth for dictionary access (cumulative MB)

3\. Log processing time per complete corpus (estimated completion time)

4\. Report concurrent agent performance (active/total ratio)

5\. Track JLPT API calls and response times

6\. Monitor disk space usage for large translation files (check every 300s)

7\. Log chunk processing rate (chunks/minute for complete works)



\### Progress Indicators (Complete Corpus Tracking)

1\. Real-time agent status dashboard (updated every 5s)

2\. Completion percentage per language (weighted by chunks processed from entire corpus)

3\. Estimated time remaining (based on chunk processing speed through complete works)

4\. Error count and resolution status (success/failure ratio)

5\. JLPT annotation progress per level (kanji processed/total kanji in corpus)

6\. Memory usage trends (MB used per agent over time)

7\. Translation quality metrics (consistency scores across complete works)



\## Manager Agent Summary: Claude Code Task Management Protocol



\*\*ABSOLUTE REQUIREMENTS FOR MANAGER AGENT:\*\*



1\. \*\*NO LOCAL SCRIPTS\*\*: Never create Python scripts, shell scripts, or any local code files

2\. \*\*TASK CREATION ONLY\*\*: All work is performed through Claude Code task creation and console management

3\. \*\*DASHBOARD VISIBILITY\*\*: All 25 tasks must be visible in the manager's Claude Code console

4\. \*\*TASK MANAGEMENT\*\*: Create and coordinate 25 total Claude Code tasks:

&nbsp;  - 16 translation tasks (4 per language, each processing all chunks for complete translation)

&nbsp;  - 4 proofreading tasks (1 per language)  

&nbsp;  - 5 JLPT annotation tasks (Japanese post-processing)



5\. \*\*CONSOLE MANAGEMENT\*\*: Manager role is limited to:

&nbsp;  - Creating tasks within Claude Code interface

&nbsp;  - Monitoring task status through console dashboard

&nbsp;  - Coordinating parallel task workflows

&nbsp;  - Managing file organization through task outputs



6\. \*\*CHUNKING STRATEGY\*\*: 

&nbsp;  - Chunk the massive Shakespeare file for manageability

&nbsp;  - Give ALL chunks to each translation agent

&nbsp;  - Each agent processes all chunks sequentially to create complete translation

&nbsp;  - Result: 4 complete translations per language for reconciliation



\*\*The manager agent serves as the task creator and coordinator within Claude Code's console interface, not a code generator. All translation, proofreading, and annotation work happens through task assignments visible in the manager's dashboard.\*\*

