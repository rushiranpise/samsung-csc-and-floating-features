"""Decode a Samsung OMC file: rotate-left by a 256 entry shift table, XOR a 256 entry salt
table, then gunzip. The tables come from the csc_tool.c in Mzdyl/OneUI_CSC_Features."""
import gzip, pathlib, re, sys

SALTS = None
SHIFTS = None

def load_tables(c_source):
    global SALTS, SHIFTS
    text = pathlib.Path(c_source).read_text(encoding="utf-8", errors="replace")
    SALTS = [int(x) for x in re.search(r"salts\[\] = \{([^}]*)\}", text).group(1).split(",")]
    SHIFTS = [int(x) for x in re.search(r"shifts\[\] = \{([^}]*)\}", text).group(1).split(",")]

def decode(raw):
    out = bytearray(len(raw))
    for i, b in enumerate(raw):
        sh = SHIFTS[i % 256]
        out[i] = (((b << sh) | (b >> (8 - sh))) & 0xFF) ^ (SALTS[i % 256] & 0xFF)
    return bytes(out)

def decode_file(path):
    data = decode(pathlib.Path(path).read_bytes())
    try:
        return gzip.decompress(data).decode("utf-8", "replace")
    except OSError:
        return data.decode("utf-8", "replace")

if __name__ == "__main__":
    load_tables("csc_tool.c")
    for name in sys.argv[1:]:
        text = decode_file(name)
        out = pathlib.Path(name).with_suffix(".decoded")
        out.write_text(text, encoding="utf-8")
        print(f"{name}: {len(text)} chars -> {out}")
