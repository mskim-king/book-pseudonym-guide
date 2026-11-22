"""04-6. k-익명성·l-다양성 확인 — 준식별자 조합이 같은 사람이 몇 명인가 (가상 데이터)"""
from collections import defaultdict
from sample_people import PEOPLE


def check(records, qi, sensitive="진단"):
    groups = defaultdict(list)
    for r in records:
        groups[tuple(r[c] for c in qi)].append(r[sensitive])
    k = min(len(v) for v in groups.values())
    l = min(len(set(v)) for v in groups.values())
    risky = [(key, len(v)) for key, v in groups.items() if len(v) < 2]
    return k, l, groups, risky


raw = [{"생년": p["생년월일"][:4], "성별": p["성별"], "우편번호": p["우편번호"], "직업": p["직업"], "진단": p["진단"]} for p in PEOPLE]
k, l, _, risky = check(raw, ["생년", "성별", "우편번호", "직업"])
print(f"[처리 전] 준식별자(생년·성별·우편번호·직업)  k={k}, l={l}, 혼자인 사람 {len(risky)}명")

gen = [{"연령대": f"{(2026 - int(p['생년월일'][:4])) // 10 * 10}대", "지역": p["우편번호"][:3], "직업": p["직업"], "진단": p["진단"]} for p in PEOPLE]
k, l, groups, risky = check(gen, ["연령대", "지역", "직업"])
print(f"[범주화 후] 준식별자(연령대·지역·직업)        k={k}, l={l}, 혼자인 사람 {len(risky)}명")
for key, n in risky:
    print("   ↳ 재식별 위험:", key, f"({n}명)")

safe = [g for g in gen if not (g["직업"] == "의사")]   # 로컬 삭제: 혼자 튀는 레코드 제거
k, l, groups, risky = check(safe, ["연령대", "지역", "직업"])
print(f"[튀는 레코드 삭제 후]                         k={k}, l={l}, 혼자인 사람 {len(risky)}명")
for key, v in groups.items():
    print("   그룹", key, "→", len(v), "명, 진단:", sorted(set(v)))
