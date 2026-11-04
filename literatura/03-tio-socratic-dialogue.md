# Tio, Sinha, Varakantham (2026): *Hey Chat, Can You Teach Me?*

**Izvor:** Sidney Tio, Arunesh Sinha, Pradeep Varakantham (jun 2026), *Hey Chat, Can You Teach Me? Structuring Socratic Dialogue for Human Learning in the Wild*, [arXiv:2606.11744](https://arxiv.org/abs/2606.11744) · **Pročitano:** 2026-11-011

**Zašto je važan:** najbliži rad mojoj temi. Spaja graf preduslova, procenu znanja iz dijaloga i LLM tutora.

## Šta je to

Autori polaze od toga da ljudi koriste LLM-ove za učenje „u divljini“, ali takvi razgovori nemaju strukturu ni kurikulum, a ni zapis o tome šta učenik već zna. Tutoriranje traži tri stvari istovremeno: **redosled gradiva, sokratovski dijalog i praćenje znanja učenika**. Tvrde da LLM-ovi (opšti i obrazovni) **loše rade sve to odjednom u dugim sesijama**, pa te poslove razdvajaju.

## Kako radi (ukratko)

1. **Graf preduslova.** Jezički model (Claude Sonnet 4.6) napravi usmereni aciklični graf za temu koju učenik zada: tema je koren, podteme su čvorovi, preduslovi su grane. Graf se pravi jednom i ostaje fiksan.
2. **Politika (PPO) bira čvor.** Mali model naučen ojačanim učenjem odlučuje **koji čvor sledeći** uči i **koliko poteza** dijaloga mu posvećuje. Trenira se u simulatoru, ne sa LLM-om.
3. **LLM vodi sokratovski razgovor** na tom čvoru i čita slobodan odgovor učenika. Drugi poziv (LLM sudija) pretvara odgovor u signal pozitivno/negativno.
4. **Savladanost je latentna.** Agent ne vidi „savladao je / nije“, već je procenjuje iz brojača odgovora po čvoru. U njihovom simuliranom učeniku čvor se može naučiti tek kad su svi preduslovi savladani, pa je ta ideja ista kao kod KST-a.

## Rezultati

Na 10 testnih tema (STEM i ne-STEM), sa **simuliranim učenicima**:
- PPO + simulator: ~93% uspeha. PPO sa prirodnim jezikom: 78–82% uspeha.
- LLM-samo tutori: GPT-5-mini ~3%, Gemini-Flash ~23%. Nasumičan izbor čvora: ~28%.
- Čak i **nasumičan** izbor čvora prolazi bolje od LLM-samo tutora, što ide u prilog tome da je struktura važnija od veličine modela.

Zaključak autora: **eksplicitna struktura kurikuluma pomaže tutoringu na način na koji skaliranje modela ne pomaže**. Takođe navode da LLM-samo tutori **slabe u dugim sesijama**, a politika ostaje stabilna.

## Veza sa mojim radom

**Poklapanje:** moja hipoteza (eksplicitna struktura + LLM bolji su od LLM-a samog) je ovde već potvrđena, ali na simulaciji. To ide u prilog mojoj temi i pomaže da se motiviše uvod.

**Razlike:**

| | Tio i sar. 2026 | Moj rad |
|---|---|---|
| Ko pravi graf | LLM, za svaku temu iznova | **Ekspert**, jednom, proveren |
| Formalizam | Graf preduslova, bez KST-a | **KST**: stanja znanja, fringe |
| Šta je „stanje“ | Brojači po čvoru (latentno) | Stanje znanja iz KST-a, ažurira se posle svakog odgovora |
| Ko bira sledeće | **RL politika** | **Outer fringe** (pravilo, bez treniranja) |
| Učenici | **Simulirani**, bez ljudi | Studija slučaja (cilj: stvarni učenici ili barem simulirani + stvarni) |
| Veličina grafa | Do 20 čvorova | Zavisi od kursa (SHSAT) |

## Šta mogu da iskoristim

- **Metodologija evaluacije.** Uspeh, pokrivenost grafa i **broj koraka do savladanosti** su jasne metrike koje mogu da preuzmem. Simulirani učenici su dobra dopuna studiji sa pravim učenicima i jeftini su za veći broj ponavljanja.
- **Podela posla:** struktura bira šta, LLM vodi razgovor. Potpuno se slaže sa idejom iz beleške 01.
- **LLM sudija koji pretvara slobodan odgovor u signal tačno/netačno** je jednostavan način da odgovor ulazi u ažuriranje stanja. Za KST mi treba nešto slično, s tim da bih dodao verovatnoću greške (pogađanje, nepažnja).
- **Upozorenje o „Agreeable Inaccuracies“** (tutor potvrdi pogrešnu tvrdnju učenika). To je realan rizik i za mog agenta i treba ga uvrstiti u edge case-ove.

## Šta ne koristim i zašto

- **RL politiku.** Outer fringe je jednostavnije, objašnjivo i ne traži treniranje. Mogu da je pomenem kao alternativu i moguće proširenje (RL da bira *koji* od više čvorova sa fringe-a).
- **Graf koji pravi LLM.** Namerno suprotno: ekspert garantuje da su preduslovi tačni.

## Ograničenja koja autori navode

- Svi odgovori učenika su **sintetički**, bez provere na ljudima.
- Grafovi su ograničeni na 20 čvorova, pa nije jasno da li se metoda skalira.
- Razlika između simulacije i stvarnosti (sim-to-real gap).

## Otvorena pitanja

- Kako tačno rade njihov LLM sudija i simulirani učenik? Pročitati dodatke (C i E).
- Da li se njihova metodologija može direktno preneti na KST stanja umesto na brojače po čvoru?
