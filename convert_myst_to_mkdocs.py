#!/usr/bin/env python3
"""
Convert MyST/JupyterBook syntax to MkDocs Material syntax in all .md files.
"""

import re
import os
import glob

DOCS_DIR = "/Users/dani/Documents/VSCodeGitHub/gralprest/docs"

# Map MyST admonition types to MkDocs Material types
ADMONITION_MAP = {
    "note": "note",
    "tip": "tip",
    "warning": "warning",
    "caution": "warning",
    "important": "important",
    "hint": "tip",
    "danger": "danger",
    "error": "danger",
    "seealso": "info",
    "attention": "warning",
}


def convert_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # --- 1. Clean MyST-specific frontmatter keys ---
    # Remove site: block (multi-line)
    content = re.sub(r"^site:\n(?:  [^\n]*\n)+", "", content, flags=re.MULTILINE)
    # Remove subtitle: and subject: lines
    content = re.sub(r"^(subtitle|subject):[^\n]*\n", "", content, flags=re.MULTILINE)

    # --- 2. Convert :::{image} directives to markdown images ---
    def convert_image(m):
        src = m.group(1).strip()
        opts_block = m.group(2)
        alt = ""
        width = ""
        cls = ""

        alt_m = re.search(r":alt:\s*(.+)", opts_block)
        if alt_m:
            alt = alt_m.group(1).strip()

        only_m = re.search(r":class:\s*(.+)", opts_block)
        if only_m:
            cls_val = only_m.group(1).strip()
            if "dark:hidden" in cls_val:
                cls = "#only-light"
            elif "hidden dark:block" in cls_val:
                cls = "#only-dark"

        width_m = re.search(r":width:\s*(\S+)", opts_block)
        if width_m:
            width = f'{{ width="{width_m.group(1)}" }}'

        img_src = src + cls
        return f"![{alt}]({img_src}){width}\n"

    content = re.sub(
        r":::\{image\}\s+([^\n]+)\n((?:[^\n]*\n)*?):::",
        convert_image,
        content,
    )

    # --- 3. Convert :::{epigraph} to blockquote ---
    def convert_epigraph(m):
        body = m.group(1)
        lines = body.strip().splitlines()
        # Last line starting with "-- " is the attribution
        result_lines = []
        attribution = ""
        for line in lines:
            if line.strip().startswith("-- "):
                attribution = f"> *— {line.strip()[3:]}*"
            else:
                result_lines.append(f"> {line}")
        out = "\n".join(result_lines)
        if attribution:
            out += "\n" + attribution
        return out + "\n"

    content = re.sub(
        r":::\{epigraph\}\n(.*?):::",
        convert_epigraph,
        content,
        flags=re.DOTALL,
    )

    # --- 4. Convert :::{glossary} block (just remove wrapper, keep content) ---
    content = re.sub(
        r":::\{glossary\}\n(.*?):::",
        lambda m: m.group(1),
        content,
        flags=re.DOTALL,
    )

    # --- 5. Convert :::{show-index} (remove entirely) ---
    content = re.sub(r":::\{show-index\}\n:::", "", content)

    # --- 6. Convert ::::{grid} ... with :::{card} into grid cards ---
    def convert_grid_block(m):
        inner = m.group(1)
        cards_html = '<div class="grid cards" markdown>\n\n'
        # Find each :::{card} Title ... :::
        card_pattern = re.compile(r':::\{card\} (.+?)\n(.*?):::', re.DOTALL)
        for card_m in card_pattern.finditer(inner):
            title = card_m.group(1).strip()
            body = card_m.group(2).strip()
            # Extract :link: option
            link_m = re.search(r"^:link:\s*(\S+)", body, re.MULTILINE)
            link = ""
            if link_m:
                link = link_m.group(1)
                body = body.replace(link_m.group(0), "").strip()
            card_content = f"-   __{title}__\n\n    ---\n\n"
            for line in body.splitlines():
                card_content += f"    {line}\n"
            if link:
                card_content += f"\n    [Acceder](gral/{link}.md)\n"
            card_content += "\n"
            cards_html += card_content
        cards_html += "</div>\n"
        return cards_html

    content = re.sub(
        r"::::\{grid\}[^\n]*\n(.*?)::::",
        convert_grid_block,
        content,
        flags=re.DOTALL,
    )

    # --- 7. Convert named admonitions: :::{admonition} Title ---
    def convert_named_admonition(m):
        title = m.group(1).strip()
        cls_m = re.search(r":class:\s*(\S+)", m.group(2))
        adm_type = "note"
        if cls_m:
            adm_type = ADMONITION_MAP.get(cls_m.group(1), "note")
        body = re.sub(r"^:class:[^\n]*\n?", "", m.group(2), flags=re.MULTILINE)
        body_lines = body.strip().splitlines()
        result = f'!!! {adm_type} "{title}"\n'
        for line in body_lines:
            result += f"    {line}\n"
        return result

    content = re.sub(
        r":::\{admonition\} (.+?)\n(.*?):::",
        convert_named_admonition,
        content,
        flags=re.DOTALL,
    )

    # --- 8. Convert simple admonitions: :::{note}, :::{tip}, etc. ---
    for myst_type, mkdocs_type in ADMONITION_MAP.items():
        def convert_simple_admonition(m, mkdocs_type=mkdocs_type):
            body_lines = m.group(1).strip().splitlines()
            # Check if first line is a title (not an option)
            title_part = ""
            body_start = 0
            if body_lines and not body_lines[0].startswith(":"):
                # Could be inline title - use as-is
                pass
            result = f"!!! {mkdocs_type}\n"
            for line in body_lines:
                result += f"    {line}\n"
            return result

        content = re.sub(
            rf":::\{{{myst_type}\}}\n(.*?):::",
            convert_simple_admonition,
            content,
            flags=re.DOTALL,
        )

    # --- 9. Convert :::{list-table} to markdown table ---
    def convert_list_table(m):
        title = m.group(1).strip() if m.group(1) else ""
        body = m.group(2)
        # Extract header-rows option
        header_rows_m = re.search(r":header-rows:\s*(\d+)", body)
        header_rows = int(header_rows_m.group(1)) if header_rows_m else 0
        body = re.sub(r"^:[^:]+:[^\n]*\n", "", body, flags=re.MULTILINE)
        # Parse rows: lines starting with * are rows, - are cells
        rows = []
        current_row = []
        for line in body.splitlines():
            stripped = line.strip()
            if stripped.startswith("* -") or stripped == "*":
                if current_row:
                    rows.append(current_row)
                current_row = []
                cell = stripped[3:].strip() if stripped.startswith("* -") else ""
                if cell:
                    current_row.append(cell)
            elif stripped.startswith("- "):
                current_row.append(stripped[2:].strip())
        if current_row:
            rows.append(current_row)

        if not rows:
            return f"*{title}*\n" if title else ""

        # Build markdown table
        max_cols = max(len(r) for r in rows)
        table = ""
        if title:
            table += f"**{title}**\n\n"
        for i, row in enumerate(rows):
            # Pad row
            row = row + [""] * (max_cols - len(row))
            table += "| " + " | ".join(row) + " |\n"
            if i == header_rows - 1:
                table += "| " + " | ".join(["---"] * max_cols) + " |\n"
        return table

    content = re.sub(
        r":::\{list-table\}([^\n]*)\n(.*?):::",
        convert_list_table,
        content,
        flags=re.DOTALL,
    )

    # --- 10. Remove any remaining ::: closers left over ---
    content = re.sub(r"^:::\n?", "", content, flags=re.MULTILINE)
    content = re.sub(r"^::::\n?", "", content, flags=re.MULTILINE)

    # --- 11. Remove remaining :option: lines (MyST directive options) ---
    content = re.sub(r"^:[a-z_-]+:[^\n]*\n", "", content, flags=re.MULTILINE)

    # --- 12. Clean up multiple blank lines ---
    content = re.sub(r"\n{3,}", "\n\n", content)

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False


def main():
    files = glob.glob(os.path.join(DOCS_DIR, "**", "*.md"), recursive=True)
    changed = 0
    for filepath in sorted(files):
        try:
            if convert_file(filepath):
                print(f"  ✅ Converted: {os.path.relpath(filepath, DOCS_DIR)}")
                changed += 1
            else:
                print(f"  ⬜ No changes: {os.path.relpath(filepath, DOCS_DIR)}")
        except Exception as e:
            print(f"  ❌ Error in {filepath}: {e}")
    print(f"\nDone: {changed}/{len(files)} files updated.")


if __name__ == "__main__":
    main()
