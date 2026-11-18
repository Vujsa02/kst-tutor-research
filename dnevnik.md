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

---

## 2026-11-14: Da li već postoji gotov prostor znanja za ELA i Math?

**Radio:** Mentor je tražio da proverim postoji li gotov graf za moje teme (40 tema u 9 grupa, ELA + Math). Kolega je predložio Learning Commons i Coherence Map. Preuzeo sam ceo Learning Commons Knowledge Graph (v1.17.0, ~1 GB JSONL), izvukao Math Coherence Map i napisao skriptu koja standarde mapira na moje teme. Proverio sam i ALEKS, Dynamic Learning Maps, Junyi i Tatsuoka podatke. Beleška: [prostor-znanja/postojeci-grafovi.md](prostor-znanja/postojeci-grafovi.md).

**Saznao:**
- Learning Commons i Coherence Map su praktično **isti graf**. Coherence Map (Student Achievement Partners) je original bez izvoza, a Learning Commons ga nudi kao podatke (406 CCSS math standarda, 757 usmerenih veza + 142 neusmerena para, CC BY 4.0). Preuzimanje radi bez naloga.
- **Math:** Coherence Map pokriva skoro sve moje math teme, a na nivou standarda je **aciklički**, pa može direktno da posluži kao surmise relacija. Za razrede 4–8 to je 160 čvorova i 253 veze.
- Kad standarde spojim u **moje teme, pojave se ciklusi** (npr. integers ⇄ fractions, krug u geometriji), jer su teme preširoke. Neke teme imaju samo po jedan standard, a „Logic and reasoning“ nema nijedan.
- **ELA:** nema gotovog grafa preduslova. Postoje samo standardi po razredima (vertikalna progresija iste veštine), ELA learning components samo za K–2, a hijerarhija veština čitanja je u literaturi sporna.
- U Learning Commons-u su i **NY Next Gen standardi sa crosswalk-om ka CCSS**. To je korisno jer je SHSAT njujorški test.
- Eedi misconceptions (8.117 zabluda) mogu kasnije da pomognu agentu da objasni **zašto** je odgovor pogrešan.

**Odlučio:**
- ✅ Math: Coherence Map je **polazni graf**. KST čvorovi su standardi, a teme iz My Smart Mentor-a su grupe/oznake. Ekspert proverava moje mapiranje.
- ✅ ELA: graf pravim ručno (eventualno uz LLM) sa polaznom hipotezom *detalj → inference → sinteza*, a ekspert ga potvrđuje. U radu to navodim kao ograničenje.
- ❌ ALEKS (zatvoren), Dynamic Learning Maps (nema javnog preuzimanja, druga populacija učenika), Junyi (zabranjena komercijalna upotreba, drugi kurikulum).
- 🟡 Tatsuoka fraction subtraction čuvam kao mali test skup za KST kod.

**Sledeće:** pitati mentora da li je kombinacija preuzetog (math) i ručnog (ELA) grafa prihvatljiva. Zatim mapirati 45 dijagnostičkih pitanja na standarde.

---

## 2026-11-15: ELA izvori vezani za SHSAT i slične testove; broj math čvorova

**Radio:** tražio sam bilo šta za ELA vezano za SHSAT ili slične testove (i zatvorene izvore, samo za ideju). Izračunao sam koliko math čvorova ostaje za različite opsege razreda. Dopunjena beleška: [prostor-znanja/postojeci-grafovi.md](prostor-znanja/postojeci-grafovi.md) (odeljci 6 i 7).

**Saznao:**
- SHSAT zvanični vodič daje samo sadržaj i usklađenost sa NY standardima, ali ne i graf.
- **College Board PSAT 8/9 / SAT** veštine se skoro 1:1 poklapaju sa mojim ELA temama, a *Skills Insight* daje opise po 7 nivoa skora. To je progresija **unutar** veštine.
- Renaissance Star tvrdi da ima graf preduslova za čitanje, ali je zatvoren. ETS CBAL ima nivoe za argumentaciju.
- Zajedničko za sve ELA izvore: **nivoi unutar veštine, a ne preduslovi između veština**.
- Math: 406 je ceo K–12 graf. Za razrede 5–8 ostaje 128 čvorova (106 kad se spoje podstandardi), za 6–8 ostaje 101 (81).

**Predlog (još nije odlučeno):**
- ELA čvor = **veština × nivo**, preduslov = niži nivo iste veštine + par ekspertskih veza između veština.
- Math: razredi 5–8, podstandardi spojeni osim onih koji su sami tema (Percentages, Rate/time/distance), oko 110 čvorova. Za studiju slučaja verovatno samo 1–2 grupe.

---

## 2026-11-17: Kako Learning Commons, Coherence Map i KST idu zajedno + odluke

**Radio:** napravio nalog na Learning Commons-u, preuzeo dataset *U.S. academic standards* (ELA) i prošao kroz Coherence Map sajt. Kroz razgovor sam razjasnio odnos između izvora i KST-a.

**Saznao:**
- **Learning Commons knowledge graph nije graf preduslova.** To je baza (~315.000 čvorova, ~551.000 veza) u kojoj su veze uglavnom hijerarhija (`hasChild`), usklađenost (veština/lekcija → standard) i crosswalk-ovi. Jedini graf preduslova u njoj je Math Coherence Map (1.041 veza).
- **Dataset** je jedan deo baze od jednog izvora (Coherence Map od SAP-a, learning components od Achievement Network-a, misconceptions od Eedi-ja…). Datasetovi su povezani preko standarda.
- **Smer:** SAP je prvo napravio Coherence Map, a Learning Commons ga je preuzeo (CC0).
- **Puna strelica** = preduslov (`buildsTowards`), **isprekidana** = povezani standardi bez smera (`relatesTo`).
- **ELA standards dataset:** 93.544 standarda iz 52 jurisdikcije, uključujući NY (1.148). Jedina vrsta veze je hijerarhija, **nema preduslova**.
- **Crosswalk** je tabela prevoda između NY i CCSS standarda, izračunata preko zajedničkih learning components (mera *jaccard*). Za NY math 5–8: 166 od 167 standarda ima par u CCSS-u, a 153 su isti. **13 se razlikuje** (NY je pomerio ili promenio gradivo). Za NY ELA crosswalk ne postoji.
- **Datumi:** standardi su menjani 2025–2026, crosswalk je nov (2026-11-06), a Coherence Map veze nemaju datum (dataset ažuriran 2025-09-23).
- **Odnos sa KST-om:** Coherence Map daje strelice (relaciju preduslova). KST od njih pravi dozvoljena stanja znanja, procenu i outer fringe. Learning Commons je izvor **sadržaja** po čvoru (tekst standarda, learning components, misconceptions, IM lekcije), dakle RAG, a ne deo KST-a.

**Odlučio:**
- ✅ **KST čvor = CCSS standard.** Learning components nisu čvorovi (nemaju veze među sobom), nego sadržaj za lekciju i procenu.
- ✅ Svaki čvor ima polja `ccss_kod` (glavni ključ), `ny_kod` (iz crosswalk-a, za SHSAT i dijagnostiku) i `msm_topics` (**lista**, jer standard može da pripada u više tema, npr. 7.RP.A.3).
- ✅ **Math: razredi 5–8** (~110 čvorova).
- ✅ `buildsTowards` tretiram kao **strog preduslov** (KST), uz napomenu u radu da izvor kaže „verovatno“.
- ✅ **Studija slučaja: ceo SHSAT** (ELA + Math).
- ✅ **Ekspert sam ja.** Ja pregledam veze, mapiranje na teme i 13 NY standarda koji se razlikuju.
- ✅ **ELA model: veština × nivo** (npr. Main idea 1 → 2 → 3). Nivoi dolaze iz razreda 6/7/8 ili iz Skills Insight bendova. Preduslov je niži nivo iste veštine, plus moje veze između veština (npr. Evidence → Inference → Main idea).