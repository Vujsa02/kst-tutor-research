# Gemini Guided Learning / LearnLM

**Izvori:**
- Jurenka i sar. (2024), *Towards Responsible Development of Generative AI for Education*, [arXiv:2407.12687](https://arxiv.org/abs/2407.12687): prvi model, **LearnLM-Tutor**
- LearnLM Team (2024), *LearnLM: Improving Gemini for Learning*, [arXiv:2412.16429](https://arxiv.org/abs/2412.16429): druga verzija, **LearnLM**
- Google blog, [Guided Learning in Gemini](https://blog.google/outreach-initiatives/education/guided-learning/) (avgust 2025)
- Google blog sa I/O 2025 (maj 2025): LearnLM ugrađen u Gemini 2.5

**Zašto ovo čitam:** mentor je Gemini-jev learning mode naveo kao primer nečeg bliskog mojoj temi.

## Šta je to

**Guided Learning** je mod u Gemini aplikaciji (od avgusta 2025). Umesto da odmah da odgovor, Gemini vodi korisnika kroz gradivo: postavlja pitanja, razlaže problem na korake i povremeno ubaci kviz. Ispod toga je **LearnLM**, Google-ova porodica modela dorađenih za učenje u saradnji sa nastavnicima i pedagoškim ekspertima.

## Kako radi (ukratko)

- **Prva verzija (LearnLM-Tutor, Gemini 1.0):** model je dodatno treniran na primerima dobrih tutorskih razgovora. Neke su vodili ljudski tutori, neke je napisao AI pa su ljudi filtrirali, a manji broj „zlatnih“ razgovora napisali su nastavnici.
- **Druga verzija (LearnLM, Gemini 1.5 Pro):** promenili su pristup. Zaključili su da je „idealni tutor“ nemoguće definisati univerzalno, pa model treba da **dobro prati pedagoške instrukcije** koje mu zada nastavnik ili developer kroz sistemski prompt. Na primer: *„ako je učenik tačno odgovorio na 3 pitanja, pređi na sledeću temu“*.
- Pedagoški principi koje model treba da poštuje: aktivno učenje, kontrola kognitivnog opterećenja, metakognicija, radoznalost i **prilagođavanje ciljevima i potrebama učenika**.

## Veza sa mojim radom

**Šta je slično:** cilj je isti, konverzacioni tutor koji uči, a ne samo daje odgovore.

**Šta je drugačije (i to je suština):**
- U objavljenim radovima **nije opisan eksplicitan model znanja učenika**: nema grafa preduslova ni praćenja stanja kroz kurs. Sve je „u glavi“ modela. (Ne znam da li toga ima u produkciji. Znam samo da nije opisano.)
- **Zona proksimalnog razvoja se ne pominje** u radovima koje sam pročitao. Najbliže je princip „prilagodi se potrebama učenika“. Kod mene je ZPD formalizovan kao outer fringe.
- Filozofija im je suprotna mojoj. Pozivaju se na „bitter lesson“: podaci i skaliranje obično pobede ručno pravljena pravila i strukture. **Moj rad testira suprotno**, da eksplicitna struktura (KST) pomaže LLM-u.

## Šta mogu da iskoristim

- **KST modul kao generator sistemskih instrukcija.** Google sam kaže da je prompt pravi način da se zada ponašanje tutora. Moj KST modul može posle svakog odgovora da napravi instrukciju tipa *„učenik zna A i B, sledeći pojam je C, materijal je ovaj“*. LLM onda radi ono u čemu je dobar (razgovor), a KST odlučuje **šta** se uči. Ovo je prirodan šablon za arhitekturu.
- **Argument za KST iz njihovog istraživanja sa korisnicima.** Učenici su kao probleme online kurseva naveli neusklađenost sa predznanjem i želju za čestim proverama znanja. To su upravo preduslovi i stalna procena stanja. I učenici i nastavnici su kao slabost AI tutora naveli i to što ne poznaju konkretan nastavni plan. To je argument za prostor znanja koji definiše ekspert.
- **Argument protiv „samo prompt“ pristupa.** Sami autori su probali da pedagogiju dobiju samo promptovanjem i zaključili da je to nepouzdano i nedosledno. Kod mene KST preuzima odluke koje prompt ne može pouzdano da nametne (šta sledeće, da li je pojam savladan).
- **Rupa u evaluaciji koju ja popunjavam.** Oni nisu merili ishode učenja, već samo to koliko se ponašanje modela slaže sa pedagoškim standardom. Razgovore su vodili eksperti koji glume učenike. Moje poređenje sa neadaptivnim redosledom meri **ishod**, i to je jasna razlika.
- **Pedagoški principi** (aktivno učenje, ne davati odgovor odmah i sl.) mogu da uđu u bazni prompt mog agenta.

## Šta ne koristim i zašto

- **Fine-tuning / RL modela.** To je skupo, traži ogromne skupove podataka i nije fokus mog rada. Koristim gotov LLM preko API-ja, a pamet o redosledu je u KST-u.
- **Njihovu evaluaciju (eksperti ocenjuju razgovore)** kao glavnu metodu, jer meri stil, a ne učenje. Može eventualno kao dodatna, kvalitativna provera.

## Dopuna: kako Google zapravo evaluira (i šta Gemini „zna“ o učeniku)

Ovo dolazi iz trećeg rada, [*Evaluating Gemini in an arena for learning*](https://arxiv.org/abs/2505.24477) (LearnLM Team, maj 2025), i iz LearnLM rada (2412.16429, Sekcija 3).

**Kako počinje jedna evaluaciona sesija.** Učenik ne bira temu slobodno. Svaki od 49 **scenarija** unapred zadaje temu, cilj učenika, ličnost učenika, kontekst (u učionici ili samostalno učenje), plan razgovora, materijal za učenje i sistemske instrukcije. Prva poruka učenika se **šalje automatski**. Dalje razgovor vodi **pedagoški ekspert koji glumi učenika** po tom scenariju. Oba modela u poređenju dobijaju identične instrukcije i materijal.

**Kako se meri da li radi dobro.** Slepo poređenje dva modela: ekspert u sekvenci razgovara sa oba, a drugi skup eksperata (206) ocenjuje transkripte po rubrici od 25 stavki (5 principa: kognitivno opterećenje, aktivno učenje, metakognicija, radoznalost, prilagođavanje učeniku) i bira koji je model bolje pomogao učeniku da ostvari cilj. Gemini 2.5 Pro je u oko 73% poređenja (bez nerešenih) imao prednost nad Claude 3.7 Sonnet, GPT-4o i o3 (broj iz apstrakta; pojedinačne procente po modelu treba proveriti u radu pre citiranja).

**Zanimljiv nalaz:** kad su glumci ocenjivali „šta mi je pomoglo“, Gemini i ChatGPT-4o su bili izjednačeni, ali su eksperti koji čitaju iste transkripte jasno preferirali Gemini. Autori kažu da se „ono što učenicima odmah pomaže razlikuje od onoga što je pedagoški ispravno“. To podržava razlog za moj eksperiment: treba meriti stvarno znanje, a ne zadovoljstvo.
