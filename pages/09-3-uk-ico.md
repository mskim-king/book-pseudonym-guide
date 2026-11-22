<!--
**상태**: 🔵 검토 중
**분류**: 09. 해외 제도와 사례
**태그**: #해외 #영국
**작성일**: 2026-11-22
-->
> 📅 **최종 확인**: 2026-11-22

영국은 EU 탈퇴 후 자체적인 UK GDPR을 운영하며, 개인정보 감독기관인 ICO(Information Commissioner's Office)가 실무 지침을 냅니다. ICO는 2025년 3월 28일 **익명처리·가명처리 최종 지침**을 공개했습니다.

## 요약

- ICO 지침은 공공·민간·비영리 분야의 **중·대규모 조직**을 대상으로 합니다.
- **가명처리**: 사람의 신원을 다른 것으로 바꿔 숨기지만, 조직 안에는 연결 고리가 남아 복원할 수 있습니다. → 여전히 개인정보
- **익명처리 과정 자체도 개인정보 처리**에 해당하므로, 익명처리를 하는 단계에서도 법적 의무를 지켜야 합니다.

## ICO 지침의 주요 내용

| 주제 | 내용 (해설 기준 요약) | 우리 제도와 비교 |
|---|---|---|
| 가명처리 | 식별자를 다른 값으로 대체, 연결 고리는 조직 안에 남음 → 개인정보 | 가명정보 = 개인정보 |
| 익명처리 | 합리적으로 사용 가능한 수단으로 식별할 수 없으면 개인정보 아님 | 익명정보 적용 제외 |
| 익명처리 과정 | 익명처리하는 행위 자체가 개인정보 처리 | 가명처리도 개인정보 처리 절차를 따름 |
| 식별 위험 판단 | 누가 어떤 정보·수단을 가질 수 있는지 등 **상황(맥락)**을 기준으로 판단 | 처리 환경 위험성 검토 |
| 대상 | 중·대규모 조직 (공공·민간·비영리) | — |

[[TIP("알아두기: '동기 있는 침입자' 관점")]]

영국에서는 오래전부터 재식별 위험을 판단할 때 **"동기 있는 침입자(motivated intruder)"**, 즉 특별한 전문 지식은 없지만 공개된 정보를 이용해 누군가를 찾아내려는 사람을 가정하는 방식이 쓰여 왔습니다. 우리 실무에서도 적정성 검토 때 "공개된 정보와 조합하면 누군가를 찾을 수 있는가?"를 따져 보는 데 유용한 관점입니다.

[[/TIP]]

## 예시: 맥락에 따라 달라지는 판단

| 같은 데이터 | 맥락 A | 맥락 B |
|---|---|---|
| 연령대·지역(시군구)·진단명 | 기관 내부 보안 분석실에서만 사용, 외부 데이터 반입 금지 | 인터넷에 공개 |
| 위험 평가 | 재식별 수단이 통제되어 위험 낮음 | 누구나 다른 정보와 조합 가능 → 위험 높음 |
| 필요한 조치 | 가명처리 + 접근 통제 | 더 강한 일반화, 셀 억제, 차분 프라이버시 검토 |

## 해설에서 지적된 점

일부 법률 해설은 최종 지침이 이전 초안들을 통합했지만, **기대만큼 명확하지 않고 일부 서술이 서로 맞지 않는 부분이 있다**고 평가했습니다. 실무에 적용할 때는 ICO 원문을 직접 확인하고, 해석이 갈리는 부분은 보수적으로 판단하는 것이 좋습니다.

## 실무 체크포인트

- [ ] 영국 정보주체의 데이터를 다룬다면 UK GDPR과 ICO 지침을 확인했는가
- [ ] 익명처리 과정 자체를 개인정보 처리로 관리하는가
- [ ] 데이터의 사용 맥락(누가, 어떤 수단)에 따라 위험을 평가했는가

## 근거·출처

| 구분 | 출처 | 비고 |
|---|---|---|
| 지침 원문 | [ICO Anonymisation guidance — About this guidance](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-sharing/anonymisation/about-this-guidance/) | 공식 |
| 해설 | [Key takeaways from the ICO's final anonymisation guidance (Bird & Bird)](https://www.twobirds.com/en/insights/2025/key-takeaways-from-the-ico%E2%80%99s-final-anonymisation-guidance) | 2025.3.28. 공개 |
| 해설 | [New ICO guidance on anonymisation and pseudonymisation (Taylor Wessing)](https://www.taylorwessing.com/en/global-data-hub/2025/spotlight-on-the-uk-data-landscape/gdh---new-ico-guidance-on-anonymisation-and-pseudonymisation) | 주요 내용 |
| 해설 | [ICO publishes anonymisation guidance (SCL)](https://www.scl.org/ico-publishes-anonymisation-guidance/) | 요약 |

## 관련 페이지

- 09-1. EU GDPR과 EDPB 가명처리 지침
- 09-6. 국가별 비교와 우리에게 주는 시사점
- 📚 03-2. 2단계: 위험성 검토
