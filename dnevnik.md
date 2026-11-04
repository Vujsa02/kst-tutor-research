# Istraživački dnevnik

Najnoviji unos je na dnu. Svaki unos sadrži: šta sam radio, šta sam saznao, šta sam odlučio ili odbacio i šta je sledeće.

---

## 2026-10-28: Početni pregled literature

**Radio:** Široka pretraga literature na teme KST, LLM tutori, procena znanja iz dijaloga i ZPD. Rezultat je dokument [Pregled literature: KST i konverzacioni agenti](https://claude.ai/artifact/EJ31C29YQhJ2raeQXKZkBd).

**Saznao:**
- Nisam našao rad koji radi **baš ovo**: ekspertski KST + procena stanja iz prirodnog jezika + izbor sa outer fringe-a + poređenje sa neadaptivnim redosledom.
- Postoje sistemi koji imaju **samo jedan deo**: ili čist LLM tutor (Gemini/LearnLM), ili KST bez razgovora (ALEKS), ili graf preduslova koji pravi sam LLM, a ne ekspert (Tio i sar. 2026).
- Najbliži radovi: Tio i sar. 2026, Steiner & Hochweber 2026, ALEKS i *The Path to Conversational AI Tutors* (2026).

**Sledeće:** detaljnije pogledati Gemini, jer ga je mentor naveo kao primer.

---

## Prvi čas: zahtevi mentora

- Voditi Git repo sa artefaktima, kodom i ovim dnevnikom.
- Mentor je naveo Gemini (learning mode) kao primer nečeg bliskog, što bi vredelo istražiti.

---

## 2026-11-01: Gemini Guided Learning / LearnLM i postavljanje repoa

**Radio:**
- Pročitao oba LearnLM rada i dva Google bloga. Beleška: [literatura/01-gemini-learnlm.md](literatura/01-gemini-learnlm.md).
- Postavio strukturu repoa i zapisao kontekst teme i proizvoda u koji se rešenje ugrađuje ([kontekst/](kontekst/)).

**Saznao:**
- Gemini Guided Learning je LLM dorađen za pedagogiju, **bez eksplicitnog modela znanja učenika** (bar nije opisan u radovima).
- Google sam zaključuje da se ponašanje tutora najbolje zadaje **sistemskim instrukcijama**, a da samo promptovanje nije dovoljno pouzdano za pedagoške odluke.
- Nisu merili **ishode učenja**, samo kvalitet ponašanja. Razgovore su vodili eksperti koji glume učenike.

**Ispravka ranije pretpostavke:** mislio sam da je ZPD eksplicitni princip u LearnLM-u, ali to **ne piše** ni u jednom pročitanom izvoru. Najbliže je „prilagodi se ciljevima i potrebama učenika“.

**Odlučio:**
- ✅ Ideja za arhitekturu: **KST modul odlučuje šta se uči, a LLM kako se uči**. KST posle svakog odgovora generiše sistemsku instrukciju za LLM.
- ❌ Fine-tuning/RL modela kao u LearnLM-u ne radim (preskupo i van fokusa). Koristim gotov LLM.

**Sledeće:** Tio i sar. 2026 (najbliži rad), zatim Doignon & Falmagne (osnove KST-a).

---

## 2026-11-01 (nastavak): Gemini arena, ZPD, ALEKS, Tio i sar.

**Radio:**
- Pročitao *Evaluating Gemini in an arena for learning* i dopunio belešku [01](literatura/01-gemini-learnlm.md) o tome kako Google evaluira.
- Zapisao šta je ZPD i kako se odnosi na outer fringe: [kontekst/zpd.md](kontekst/zpd.md).
- Napisao belešku [02 (ALEKS)](literatura/02-aleks.md) i [03 (Tio i sar.)](literatura/03-tio-socratic-dialogue.md).

**Saznao:**
- **Gemini evaluacija:** sesija počinje unapred zadatim **scenarijem** (tema, cilj, ličnost učenika, plan razgovora, materijal), a učenika glume pedagoški eksperti. Dva modela se slepo porede, a drugi eksperti ih ocenjuju po rubrici od 25 stavki. To je merenje **ponašanja**, a ne učenja. Evaluacija je **jedna sesija**, a rad sam kaže da to nisu dugi putevi učenja i da memorija između sesija nije ispitana. Za Guided Learning ne piše da pamti šta učenik zna. U Gemini aplikaciji postoji opšta funkcija pamćenja preferencija iz prošlih razgovora, ali nema dokaza da nosi mapu znanja.
- **Pažnja:** „lošiji je za duge razgovore“ **ne piše** u Google radovima, to je samo da nije ispitano. Tvrdnju da LLM-samo tutori slabe u dugim sesijama iznose Tio i sar. (na simulaciji).
- **ALEKS** je dokaz da KST radi u praksi (milioni učenika), ali bez razgovora. U EDM 2022 radu je novi motor sa neuronskom mrežom + KST bolji od čistog KST-a, pa ni u ALEKS-u KST nije sam dovoljan.
- **Tio i sar.** pokazuju da eksplicitan graf preduslova + politika daje mnogo bolje rezultate od LLM-samo tutora (na simuliranim učenicima). Razlike prema meni: graf pravi LLM (ne ekspert), nema KST-a, bira RL politika (ne outer fringe), nema stvarnih učenika.

**Problem:** PDF-ovi Cosyn 2021 i arXiv pregleda stigli su kao kompresovan binarni fajl, a lokalna instalacija biblioteke za čitanje PDF-a nije uspela (mreža iz sandbox-a). Zato je beleška 02 **delimična**: oslanja se na apstrakt, uvod EDM 2022 rada i opšte poznavanje KST-a. Ono što dolazi iz prvog pregleda literature je tako i označeno.

**Odlučio:**
- ✅ Outer fringe tretiram kao **operacionalizaciju** ZPD-a, ne kao njen identitet (ZPD zavisi od pomoći i od konkretnog učenika, outer fringe samo od preduslova).
- ✅ Na pitanje „šta je novo u mom radu“ sad imam preciznije: **ekspertski KST + procena iz razgovora + izbor sa outer fringe-a (bez RL-a) + poređenje sa neadaptivnim redosledom na ishodima učenja**.
- ✅ Metrike iz Tio i sar. (uspeh, pokrivenost, koraci do savladanosti) preuzimam kao polaznu tačku za evaluaciju.

**Sledeće:** preuzeti Cosyn 2021 i pročitati ga u celini, zatim Scarlatos i sar. (kako iz dijaloga zaključiti šta učenik zna), pa *Dialogic Pedagogy for LLMs* (ZPD).

---

## 2026-11-04: ALEKS pročitan u celini, procena da li je literature dovoljno

**Radio:** stavio PDF Cosyn 2021 u repo, izvukao iz njega tekst skriptom i pročitao ga. Beleška [02](literatura/02-aleks.md) je prepisana sa punim tekstom.

**Saznao:**
- ALEKS koristi 4–5 miliona učenika godišnje. Ciklus je potvrđen u tekstu: procena (≤30 pitanja) → učenik **sam bira** stavku sa outer fringe-a → vežba i skor (cilj 5) → stavka ulazi u stanje → fringe se preračunava → periodična provera napretka.
- Procena iz zadataka je dobra (AUROC 0,86–0,89), a učenje sa fringe-a uspeva u 81–94% pokušaja. To je najbolji dokaz do sada da je outer fringe razuman izbor „sledećeg gradiva“.
- **Šta znači „naučio je“ nije deo KST-a**, nego heuristika. U mom sistemu to mora da odluči agent (ili pravilo oko njega), a ALEKS-ov skor je dobar početak.
- Zaboravljanje je realno: tek naučene stavke padnu na ~60% tačnosti posle nekoliko dana, pa stanje treba povremeno proveravati.
- Rad **ne poredi** ALEKS sa neadaptivnim redosledom i nema razgovor. Autori čak kažu da podaci dovode u pitanje pretpostavku klasičnog modela (konstantna greška iz nepažnje i pogađanja).

**Zaključak o literaturi (sad kad imam 3 rada):**
- Tri rada zajedno **opravdavaju smer**: Gemini pokazuje da LLM tutor bez eksplicitne strukture nije merio učenje, ALEKS da KST sa outer fringe-om radi na velikoj skali, a Tio i sar. da struktura + LLM bolje radi od LLM-a samog (u simulaciji).
- Ali **ne dokazuju** da će moj pristup raditi, i nijedan od njih ne radi baš to. To je upravo ono što moj rad treba da proveri.
- Ostaju tri rada koje vredi samo prelistati (apstrakt + zaključak), jer odgovaraju na pitanja koja će mentor verovatno postaviti: Scarlatos i sar. (procena znanja iz dijaloga), *The Path to Conversational AI Tutors* (predlaže KST kao spoljašnju petlju) i Steiner & Hochweber (KST + LLM).

**Odlučio:** 
- ne čitam sve u detalje za preostale radove. Prelistavam ta tri rada, a onda prelazim na arhitekturu.
- Prvo bi isao diagnostic test da proceni inicijalno stanje u KST-u kao kod ALEKS koji ce morati da se preradi da bude adaptivni (nije jos jasno da li bi bolje radio adaptivni primer ili ne)
- Primamljivije mi deluje da se krecem horizontalno po tom stablu umesto po dubini, jer se cesto neke lekcije kojih se ne podsecamo zaborave brzo a na ovaj nacin bi drzali to znanje svezim (mozda bi valjalo i to proveriti)
- Ako se ucenik zaglavi na nekom cvoru to je onda znak da ili je lose procenjeno znanje (gde onda treba ponovno proveriti preduslove ili ih se podsetiti) ili je lose gradivo onda (cuvamo broj pokusaja i oznaku blokiran), pa ako se pojavljuje na vise ucenika onda je mozda problem u gradivu, preporuka moze biti kasnije da nastavi zbog umora (ALEKS samo nezno usmerava na drugu stavku)