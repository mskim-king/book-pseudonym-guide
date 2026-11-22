"""05장. 가명정보 결합 흐름 시뮬레이션 (가상 데이터, 단순화한 모형)

실제 결합은 「가명정보의 결합 및 반출 등에 관한 고시」에 따라
결합키관리기관(한국인터넷진흥원)과 결합전문기관이 나누어 수행합니다.
"""
import hashlib, hmac, secrets

# 결합키 생성 규칙(예: 이름+휴대폰+생년월일 → 해시)과 솔트는 신청 기관들이 사전에 합의한 것으로 가정
SHARED_SALT = b"agreed-salt-for-this-project"


def combine_key(name, phone, birth):
    return hashlib.sha256(SHARED_SALT + f"{name}|{phone}|{birth}".encode()).hexdigest()


# A기관(카드사)·B기관(통신사)의 원본 (가상)
A = [("김민수", "010-2345-6789", "1983-04-12", {"월카드사용": 1_520_000}),
     ("이서연", "010-3456-7890", "1985-09-03", {"월카드사용": 870_000}),
     ("최유진", "010-5678-9012", "1991-11-15", {"월카드사용": 640_000})]
B = [("김민수", "010-2345-6789", "1983-04-12", {"월데이터GB": 12}),
     ("최유진", "010-5678-9012", "1991-11-15", {"월데이터GB": 35}),
     ("한지민", "010-1111-2222", "2000-01-01", {"월데이터GB": 50})]


def prepare(org, data):
    """① 일련번호 ② 결합키 ③ 가명정보 생성 → ①② 는 결합키관리기관, ①③ 은 결합전문기관으로"""
    to_kisa, to_agency = [], []
    for name, phone, birth, attrs in data:
        serial = f"{org}-{secrets.token_hex(3)}"
        to_kisa.append((serial, combine_key(name, phone, birth)))
        to_agency.append((serial, attrs))          # 이름·연락처 없이 속성만
    return to_kisa, to_agency


A_kisa, A_agency = prepare("A", A)
B_kisa, B_agency = prepare("B", B)

# 결합키관리기관: 같은 결합키를 가진 일련번호끼리 연결(결합키연계정보) — 결합키 자체는 넘기지 않음
key_to_A = {k: s for s, k in A_kisa}
link_info = [(key_to_A[k], s_b) for s_b, k in B_kisa if k in key_to_A]
print("결합키연계정보(일련번호 쌍):", link_info)

# 결합전문기관: 연계정보로 가명정보를 결합, 새 결합ID 부여
A_map, B_map = dict(A_agency), dict(B_agency)
combined = [{"결합ID": f"C{i:03d}", **A_map[a], **B_map[b]} for i, (a, b) in enumerate(link_info, 1)]
print("결합 결과:", combined)
print(f"A {len(A)}명, B {len(B)}명 → 양쪽에 모두 있는 {len(combined)}명만 결합 (이름·연락처는 전달되지 않음)")
