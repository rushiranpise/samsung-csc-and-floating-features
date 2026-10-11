import re, sys, zipfile
pat = re.compile(rb"(?:CscFeature_|SEC_FLOATING_FEATURE_)[A-Za-z0-9_]+")
keys = set()
try:
    with zipfile.ZipFile(sys.argv[1]) as z:
        for n in z.namelist():
            if n.endswith((".dex", ".so")) or n.startswith("assets/") and n.endswith(".bin"):
                try:
                    keys |= {m.decode() for m in pat.findall(z.read(n))}
                except Exception:
                    pass
except Exception as e:
    print("ERR", e, file=sys.stderr)
for k in sorted(keys):
    print(k)
