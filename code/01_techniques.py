"""04장. 가명처리 기법 적용 전·후 비교 (가상 데이터)"""
import hashlib, hmac, random
from sample_people import PEOPLE

SECRET_KEY = b"demo-secret-key-keep-separately"   # 실제로는 별도 보관(추가정보)
random.seed(7)


def pseudonym(value: str) -> str:
    """HMAC-SHA256 키 기반 해시 → 같은 사람은 항상 같은 가명, 키 없이는 되돌리기 어려움"""
    return "P-" + hmac.new(SECRET_KEY, value.encode(), hashlib.sha256).hexdigest()[:8]


def age_band(birth: str, base_year: int = 2026) -> str:
    age = base_year - int(birth[:4])
    return f"{age // 10 * 10}대"


rows = []
for p in PEOPLE:
    rows.append({
        "가명ID": pseudonym(p["휴대폰"]),                      # 토큰화(키 기반 해시)
        "연령대": age_band(p["생년월일"]),                      # 범주화
        "성별": p["성별"],
        "지역": p["우편번호"][:3] + "**",                       # 부분삭제(마스킹)
        "직업": p["직업"],
        "진단": p["진단"],
        "구매액": round(p["구매액"] + random.randint(-5000, 5000), -4),  # 잡음 추가 후 라운딩
    })

print("[원본 일부]")
for p in PEOPLE[:2]:
    print("  ", p)
print("\n[가명처리 후] 이름·휴대폰 삭제, 생년월일→연령대, 우편번호 앞 3자리, 구매액 잡음+만원 단위")
for r in rows:
    print("  ", r)
