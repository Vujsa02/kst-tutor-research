"""Izvlači Math Coherence Map iz Learning Commons Knowledge Graph exporta
i mapira CCSS standarde na teme iz My Smart Mentor-a.

Ulaz: folder sa nodes.jsonl i relationships.jsonl (Knowledge Graph v1.17.0, ~1 GB, nije u repou):
  curl -L -o nodes.jsonl https://cdn.learningcommons.org/knowledge-graph/v1.17.0/exports/nodes.jsonl
  curl -L -o relationships.jsonl https://cdn.learningcommons.org/knowledge-graph/v1.17.0/exports/relationships.jsonl

Pokretanje:
  python3 -I coherence_map.py <folder_sa_jsonl> <izlaz.json>

Mapiranje standard -> tema (dict TOPIC_MAP) je MOJA procena, ne deo Coherence Map-a.
"""
import collections
import json
import sys

FD = "math-numbers-fractions-decimals"
PC = "math-numbers-percentages"
RP = "math-numbers-ratios-proportions"
INT = "math-numbers-integers-whole-numbers"
OO = "math-numbers-order-of-operations"
EXP = "math-numbers-exponents-roots"
EE = "math-algebra-expressions-equations"
INEQ = "math-algebra-inequalities"
LIN = "math-algebra-linear-equations"
PAT = "math-algebra-patterns-sequences"
FN = "math-algebra-functions"
ANG = "math-geometry-angles-lines"
AV = "math-geometry-perimeter-area-volume"
CG = "math-geometry-coordinate-geometry"
TRI = "math-geometry-triangles-polygons"
CIR = "math-geometry-circles"
TR = "math-geometry-transformations"
PR = "math-statistics-basic-probability"
DI = "math-statistics-range-data-interpretation"
MMM = "math-statistics-mean-median-mode"
CH = "math-statistics-charts-graphs-tables"
WPP = "math-word-problems-percents-real-world-context"
RTD = "math-word-problems-rate-time-distance"
MS = "math-word-problems-multi-step"

EXPLICIT = {
    FD: ["5.NBT.A.3", "5.NBT.A.4", "5.NBT.B.7", "6.NS.A.1", "6.NS.B.3", "7.NS.A.2.d",
         "4.NF.C.5", "4.NF.C.6", "4.NF.C.7"],
    EXP: ["5.NBT.A.2", "6.EE.A.1", "8.EE.A.1", "8.EE.A.2", "8.EE.A.3", "8.EE.A.4", "8.NS.A.1", "8.NS.A.2"],
    INT: ["6.NS.B.2", "6.NS.B.4", "6.NS.C.5", "6.NS.C.6.a", "6.NS.C.6.c", "6.NS.C.7.a", "6.NS.C.7.b",
          "6.NS.C.7.c", "6.NS.C.7.d", "7.NS.A.1.a", "7.NS.A.1.b", "7.NS.A.1.c", "7.NS.A.1.d",
          "7.NS.A.2", "7.NS.A.2.a", "7.NS.A.2.b", "7.NS.A.2.c", "7.NS.A.3"],
    OO: ["5.OA.A.1", "5.OA.A.2"],
    PAT: ["5.OA.B.3", "4.OA.C.5", "3.OA.D.9"],
    RP: ["6.RP.A.1", "6.RP.A.2", "6.RP.A.3", "6.RP.A.3.a", "6.RP.A.3.d", "7.RP.A.1", "7.RP.A.2", "7.G.A.1"],
    PC: ["6.RP.A.3.c"],
    WPP: ["7.RP.A.3"],
    RTD: ["6.RP.A.3.b"],
    MS: ["7.EE.B.3", "4.OA.A.3", "3.OA.D.8"],
    EE: ["6.EE.A.2", "6.EE.A.3", "6.EE.A.4", "6.EE.B.5", "6.EE.B.6", "6.EE.B.7",
         "7.EE.A.1", "7.EE.A.2", "7.EE.B.4", "7.EE.B.4.a"],
    INEQ: ["6.EE.B.8", "7.EE.B.4.b"],
    LIN: ["8.EE.B.5", "8.EE.B.6", "8.EE.C.7", "8.EE.C.7.a", "8.EE.C.7.b", "8.EE.C.8"],
    FN: ["6.EE.C.9", "8.F.A.1", "8.F.A.2", "8.F.A.3", "8.F.B.4", "8.F.B.5"],
    ANG: ["4.MD.C.5", "4.MD.C.6", "4.MD.C.7", "4.G.A.1", "7.G.B.5"],
    AV: ["3.MD.C.5", "3.MD.C.6", "3.MD.C.7.a", "3.MD.C.7.b", "3.MD.C.7.c", "3.MD.C.7.d", "3.MD.D.8",
         "4.MD.A.3", "5.MD.C.3", "5.MD.C.4", "5.MD.C.5.a", "5.MD.C.5.b", "5.MD.C.5.c",
         "6.G.A.1", "6.G.A.2", "6.G.A.4", "7.G.A.3", "7.G.B.6", "8.G.C.9"],
    CG: ["5.G.A.1", "5.G.A.2", "6.G.A.3", "6.NS.C.6.b", "6.NS.C.8", "8.G.B.8"],
    TRI: ["3.G.A.1", "4.G.A.2", "4.G.A.3", "5.G.B.3", "5.G.B.4", "7.G.A.2", "8.G.A.5", "8.G.B.6", "8.G.B.7"],
    CIR: ["7.G.B.4"],
    TR: ["8.G.A.1", "8.G.A.2", "8.G.A.3", "8.G.A.4"],
    PR: ["7.SP.C.5", "7.SP.C.6", "7.SP.C.7", "7.SP.C.8"],
    MMM: ["6.SP.A.3"],
    DI: ["6.SP.A.1", "6.SP.A.2", "6.SP.B.5", "7.SP.A.1", "7.SP.A.2", "7.SP.B.3", "7.SP.B.4",
         "8.SP.A.2", "8.SP.A.3"],
    CH: ["3.MD.B.3", "3.MD.B.4", "4.MD.B.4", "5.MD.B.2", "6.SP.B.4", "8.SP.A.1", "8.SP.A.4"],
}


def topic_map(codes):
    m = {}
    for c in codes:  # podrazumevano po domenu za razrede 3-5
        parts = c.split(".")
        if len(parts) < 2:
            continue
        g, dom = parts[0], parts[1]
        if g in ("3", "4", "5") and dom == "NF":
            m[c] = FD
        elif g in ("3", "4", "5") and dom == "NBT":
            m[c] = INT
        elif g in ("3", "4") and dom == "OA":
            m[c] = INT
    for t, cs in EXPLICIT.items():
        for c in cs:
            m[c] = t
    return {c: t for c, t in m.items() if c in codes}


def main(data_dir, out_path):
    rels, ids = [], set()
    with open(f"{data_dir}/relationships.jsonl") as f:
        for line in f:
            o = json.loads(line)
            if o["label"] in ("buildsTowards", "relatesTo"):
                rels.append((o["label"], o["source_identifier"], o["target_identifier"]))
                ids.update([o["source_identifier"], o["target_identifier"]])
    std = {}
    with open(f"{data_dir}/nodes.jsonl") as f:
        for line in f:
            o = json.loads(line)
            if o["identifier"] in ids:
                p = o["properties"]
                std[o["identifier"]] = {
                    "code": p.get("statementCode"),
                    "grade": json.loads(p.get("gradeLevel") or "[]"),
                    "description": p.get("description") or "",
                }
    edges = [(l, std[s]["code"], std[t]["code"]) for l, s, t in rels if s in std and t in std]
    codes = {v["code"] for v in std.values()}
    tm = topic_map(codes)

    cross = collections.Counter()
    for l, s, t in edges:
        a, b = tm.get(s), tm.get(t)
        if l == "buildsTowards" and a and b and a != b:
            cross[(a, b)] += 1

    out = {
        "source": "Learning Commons Knowledge Graph v1.17.0, Math Coherence Map (Student Achievement Partners, CC0; KG CC BY 4.0)",
        "note": "topic polje je ručno mapiranje (procena), nije deo izvora",
        "standards": sorted(
            ({**v, "topic": tm.get(v["code"])} for v in std.values()), key=lambda x: x["code"]
        ),
        "edges": [{"type": l, "from": s, "to": t} for l, s, t in edges],
        "topic_edges": [
            {"from": a, "to": b, "n": n, "reverse_n": cross.get((b, a), 0)}
            for (a, b), n in cross.most_common()
        ],
    }
    with open(out_path, "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print(f"standarda: {len(std)}, veza: {len(edges)}, mapirano na teme: {len(tm)}, veza među temama: {len(cross)}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
