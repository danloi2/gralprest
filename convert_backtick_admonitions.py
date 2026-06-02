#!/usr/bin/env python3
import os
import glob
import re

DOCS_DIR = "/Users/dani/Documents/VSCodeGitHub/gralprest/docs"

KEYWORDS_MAP = {
    "aholkua": "tip",
    "gomendio": "tip",
    "recomendación": "tip",
    "consejo": "tip",
    "kontuz": "warning",
    "segurtasuna": "warning",
    "cuidado": "warning",
    "advertencia": "warning",
    "peligro": "warning",
    "garrantzitsua": "important",
    "beharrezkoa": "important",
    "importante": "important",
    "obligatorio": "important",
    "adibidea": "example",
    "ejemplo": "example",
    "akats": "failure",
    "error": "failure",
    "zure txanda": "question",
    "tu turno": "question",
    "erreferentzia": "quote",
    "referencia": "quote",
}

def determine_type(title):
    title_lower = title.lower()
    for keyword, adm_type in KEYWORDS_MAP.items():
        if keyword in title_lower:
            return adm_type
    return "note"

def clean_title(title):
    # Remove MyST target attributes like id="..." or class="..."
    title = re.sub(r'\s+id="[^"]*"', '', title)
    title = re.sub(r'\s+class="[^"]*"', '', title)
    return title.strip()

def convert_admonitions(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    i = 0
    n = len(lines)
    changed = False

    while i < n:
        line = lines[i]
        # Match starting fence like ```{admonition} Title or :::{admonition} Title
        match = re.match(r"^(\s*)(`+|:+)\{admonition\}\s*(.*)$", line)
        if match:
            indent = match.group(1)
            fence_char = match.group(2)[0]
            fence_len = len(match.group(2))
            title = match.group(3).strip()
            
            title = clean_title(title)
            adm_type = determine_type(title)
            
            # Now find the matching closing fence
            admonition_body = []
            i += 1
            closed = False
            while i < n:
                curr_line = lines[i]
                # Check for closing fence of same char and length, with same indent
                # e.g. ``` or ::::
                close_match = re.match(r"^" + re.escape(indent) + re.escape(fence_char * fence_len) + r"\s*$", curr_line)
                if close_match:
                    closed = True
                    break
                else:
                    admonition_body.append(curr_line)
                i += 1
            
            if closed:
                changed = True
                # Format admonition
                new_lines.append(f'{indent}!!! {adm_type} "{title}"\n')
                # Indent all lines of the body by 4 spaces (relative to the original indent)
                for body_line in admonition_body:
                    if body_line.strip() == "":
                        new_lines.append("\n")
                    else:
                        new_lines.append(f"{indent}    {body_line}")
            else:
                # If not closed, write the original start line and rewind to process body normally
                new_lines.append(line)
                i = i - len(admonition_body)
        else:
            new_lines.append(line)
        i += 1

    if changed:
        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        return True
    return False

def main():
    files = glob.glob(os.path.join(DOCS_DIR, "**", "*.md"), recursive=True)
    updated = 0
    for filepath in sorted(files):
        try:
            if convert_admonitions(filepath):
                print(f"  ✅ Converted: {os.path.relpath(filepath, DOCS_DIR)}")
                updated += 1
        except Exception as e:
            print(f"  ❌ Error in {filepath}: {e}")
    print(f"\nDone: {updated}/{len(files)} files updated.")

if __name__ == "__main__":
    main()
