import streamlit as st

st.set_page_config(page_title="Test Archetypów Marki", layout="centered")
st.title("🔮 Test Archetypów Marki")
st.markdown("### Część I – Pytania główne (2 pytania na archetyp)")

# 12 archetypów po 2 pytania
archetypes = {
    "Niewinny": [
        "Moja marka kojarzy się z prostotą, szczerością i spokojem.",
        "Klienci czują się bezpieczni i zaopiekowani, korzystając z niej."
    ],
    "Odkrywca": [
        "Moja marka inspiruje do podróży, wolności i odkrywania.",
        "Chcę, by marka była symbolem autentyczności i indywidualizmu."
    ],
    "Mędrzec": [
        "Moja marka przekazuje wiedzę i porządkuje informacje.",
        "Chcę być źródłem mądrości i wiarygodnych danych."
    ],
    "Bohater": [
        "Moja marka pomaga pokonywać wyzwania.",
        "Cechuje ją odwaga i pozytywny wpływ."
    ],
    "Buntownik": [
        "Moja marka łamie zasady i prowokuje zmianę.",
        "Ceni niezależność i niezgodę na status quo."
    ],
    "Magik": [
        "W mojej marce jest element transformacji i magii.",
        "Klienci doświadczają czegoś niezwykłego."
    ],
    "Kochanek": [
        "Moja marka buduje bliskość i przyjemność.",
        "Odwołuje się do zmysłów i emocji."
    ],
    "Błazen": [
        "Moja marka jest lekka i zabawna.",
        "Pomaga się wyluzować i podejść z dystansem."
    ],
    "Zwyczajny": [
        "Moja marka jest swojska i codzienna.",
        "Daje poczucie przynależności i autentyczności."
    ],
    "Opiekun": [
        "Moja marka wspiera, chroni i troszczy się.",
        "Jest pełna empatii i gotowości do pomocy."
    ],
    "Twórca": [
        "Moja marka inspiruje do tworzenia czegoś nowego.",
        "Ceni kreatywność, ekspresję i wizję."
    ],
    "Władca": [
        "Moja marka symbolizuje prestiż i jakość.",
        "Lubi mieć kontrolę i wyznaczać standardy."
    ]
}

scores = {}
for arch, questions in archetypes.items():
    total = 0
    for q in questions:
        total += st.slider(q, 1, 5, 3, key=q)
    scores[arch] = total

# Część II – pytania kontrastujące
st.markdown("### 🔁 Część II – Pytania kontrastujące")

contrasts = [
    ("Bohater", "Opiekun", "Moja marka prowadzi ludzi przez trudności", "Moja marka otula troską"),
    ("Mędrzec", "Błazen", "Dzielę się wiedzą i porządkuję złożone informacje", "Wnoszę lekkość i humor"),
    ("Odkrywca", "Zwyczajny", "Oferuję nowe ścieżki", "Dbam o normalność i codzienność"),
    ("Magik", "Kochanek", "Zachwycam, inspiruję i zaskakuję", "Stawiam na bliskość i zmysłowość"),
    ("Buntownik", "Władca", "Kwestionuję normy", "Reprezentuję prestiż i porządek"),
    ("Władca", "Twórca", "Wyznaczam standardy i kontroluję", "Tworzę i inspiruję")
]

contrast_scores = {a: 0 for a in archetypes}
for a, b, desc_a, desc_b in contrasts:
    answer = st.radio(f"{desc_a} ⬅️ lub ➡️ {desc_b}", [desc_a, desc_b], key=f"{a}_{b}")
    if answer == desc_a:
        contrast_scores[a] += 1
    else:
        contrast_scores[b] += 1

# Część III – pytania sytuacyjne
st.markdown("### ⚡ Część III – Reakcja na kryzys")

reaction = st.selectbox("W sytuacji kryzysowej moja marka przede wszystkim:", [
    "Motywuje do działania i zmiany (Bohater)",
    "Zapewnia opiekę i spokój (Opiekun)",
    "Zaskakuje kampanią lub gestem (Magik)",
    "Edukacyjnie tłumaczy sytuację (Mędrzec)",
    "Rozładowuje napięcie humorem (Błazen)",
    "Wraca do autentycznych wartości (Zwyczajny)",
    "Wprowadza odważne, ryzykowne rozwiązania (Buntownik)",
    "Dopracowuje produkt lub strategię (Twórca)"
])

for arch in archetypes:
    if arch in reaction:
        contrast_scores[arch] += 1

# Część IV – pytanie końcowe
st.markdown("### 🎭 Część IV – Tożsamość marki")

identity = st.selectbox("Gdyby Twoja marka była osobą, byłaby:", [
    "Uczonym (Mędrzec)", "Przyjacielem z sąsiedztwa (Zwyczajny)", "Artystą z wizją (Twórca)",
    "Motywatorem i liderem zmiany (Bohater)", "Dobrym duchem (Magik)", "Partnerem emocjonalnym (Kochanek)",
    "Reformatorem (Buntownik)", "Królem/Królową (Władca)", "Eksploratorem (Odkrywca)",
    "Wesołkiem (Błazen)", "Opiekunem (Opiekun)", "Optymistą (Niewinny)"
])

for arch in archetypes:
    if arch in identity:
        contrast_scores[arch] += 1

# Wyniki
if st.button("📊 Pokaż wynik końcowy"):
    final = {arch: scores[arch] + contrast_scores.get(arch, 0) for arch in archetypes}
    sorted_final = sorted(final.items(), key=lambda x: x[1], reverse=True)
    top_score = sorted_final[0][1]
    top = [a for a, s in sorted_final if s == top_score]

    if len(top) == 1:
        st.success(f"🎯 Twój dominujący archetyp to: **{top[0]}**")
    else:
        st.info("Twoja marka łączy cechy kilku archetypów:")
        for a in top:
            st.write(f"• {a}")

    st.markdown("### 📈 Szczegółowe wyniki:")
    for a, s in sorted_final:
        st.write(f"{a}: {s} pkt")
