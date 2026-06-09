from pathlib import Path
py_dir=Path.home() /'Desktop'/'vscode'/'python'
pydoc=[p for p in py_dir.rglob('*.py')]
print(pydoc)
sc=[]
for f in pydoc:
    with open(f,'r',encoding='utf-8') as file:
        for line in file:
            if line.startswith('import') or line.startswith('from'):
                sc.append(line.strip())
nesc=list(set(sc))
print(nesc)
qc=['os', 'sys', 'math', 're', 'pathlib', 'json', 'unittest']
ac=list(set(nesc)-set(qc))
print(ac)
