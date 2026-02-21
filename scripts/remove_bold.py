import re, os, glob

base = r'c:\Users\vidal\OneDrive\Documentos\13 - CLONEGIT\meu_site\books'
books = ['bioengenharia-solos', 'ciencia-paisagem', 'geotecnologias-sig', 'pi']

total_removed = 0

for book in books:
    book_dir = os.path.join(base, book)
    qmd_files = sorted(glob.glob(os.path.join(book_dir, '*.qmd')))
    qmd_files += sorted(glob.glob(os.path.join(book_dir, 'capitulos', '*.qmd')))
    
    book_removed = 0
    for fpath in qmd_files:
        fname = os.path.relpath(fpath, base)
        with open(fpath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        in_special = 0
        in_code = False
        in_yaml = False
        changed = 0
        new_lines = []
        
        for i, line in enumerate(lines):
            stripped = line.strip()
            
            if i == 0 and stripped == '---':
                in_yaml = True
                new_lines.append(line)
                continue
            if in_yaml and stripped == '---':
                in_yaml = False
                new_lines.append(line)
                continue
            if in_yaml:
                new_lines.append(line)
                continue
            
            if stripped.startswith('```'):
                in_code = not in_code
                new_lines.append(line)
                continue
            if in_code:
                new_lines.append(line)
                continue
            
            if stripped.startswith(':::'):
                if stripped == ':::':
                    if in_special > 0:
                        in_special -= 1
                else:
                    in_special += 1
                new_lines.append(line)
                continue
            
            if in_special > 0:
                new_lines.append(line)
                continue
            
            if stripped.startswith('|'):
                new_lines.append(line)
                continue
            
            if stripped.startswith('>'):
                new_lines.append(line)
                continue
            
            new_line = re.sub(r'\*\*([^*]+?)\*\*', r'\1', line)
            if new_line != line:
                n = len(re.findall(r'\*\*[^*]+?\*\*', line))
                changed += n
            new_lines.append(new_line)
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        
        if changed > 0:
            print(f'  {fname}: {changed} negritos removidos')
            book_removed += changed
    
    print(f'[{book}] Total: {book_removed} negritos removidos')
    print()
    total_removed += book_removed

print(f'=== TOTAL GERAL: {total_removed} negritos removidos ===')
