# TODO

## Literatura
- [x] Gemini Guided Learning / LearnLM
- [x] Tio, Sinha, Varakantham (2026): najbliži rad temi (dodatke C i E još nisam pročitao)
- [x] Cosyn i sar. (2021): ALEKS, pročitano u celini (osim dodatka), vidi belešku 02
- [ ] Scarlatos i sar. (2025): kako iz dijaloga zaključiti šta učenik zna
- [ ] *The Path to Conversational AI Tutors* (2026)
- [ ] Steiner & Hochweber (2026): KST + LLM
- [x] *Evaluating Gemini in an arena for learning* (arXiv:2505.24477), vidi belešku 01
- [ ] *Dialogic Pedagogy for LLMs* (arXiv:2506.19484): ZPD + LLM

## Prostor znanja
- [x] Proveriti da li postoji gotov graf (Learning Commons, Coherence Map, ALEKS, DLM, Junyi): math delimično da, ELA ne
- [ ] Proći lokalni vodič za proveru (koraci 3–6: jq provere, sporna mapiranja, ciklusi, ELA izvori)
- [x] ~~Odlučiti granularnost~~: KST čvor = CCSS standard, `msm_topics` je lista (vidi dnevnik 2026-11-17)
- [x] ~~Opseg razreda~~: math 5–8 · ~~strog preduslov~~: da · ~~obim studije~~: ceo SHSAT · ~~ekspert~~: ja
- [ ] Pregledati veze i mapiranje CCSS standard → tema ([skripte/coherence_map.py](prostor-znanja/skripte/coherence_map.py)) (ja kao ekspert)
- [ ] Dodati `ny_kod` iz crosswalk-a i ručno pregledati 13 NY standarda koji se razlikuju od CCSS-a
- [x] ~~Odlučiti ELA model~~: veština × nivo
- [ ] Odlučiti odakle nivoi za ELA: razredi 6/7/8 iz standarda ili Skills Insight bendovi
- [ ] Napraviti nacrt ELA grafa (detalj → inference → sinteza, plus Revising/Grammar)
- [ ] Teme bez standarda ili sa samo jednim: Logic and reasoning, Percentages, Circles, Mean/median/mode
- [ ] Proveriti CCSS *Language Progressive Skills* tabelu (gramatika)
- [x] ~~Mapirati NY Next Gen → CCSS~~: crosswalk postoji u Learning Commons-u (166/167 za math 5–8), za ELA ne postoji

## Arhitektura (posle literature)
- [x] Gde se agent uključuje u My Smart Mentor (posle dijagnostike? uz nedeljni plan?)
- [x] Kako se ponasati kada je ucenik "zaglavljen" na nekom cvoru i ima poteskoce da napreduje dalje?
- [ ] Mapiranje 45 dijagnostičkih pitanja na čvorove prostora znanja
- [ ] Format baze prostora znanja (čvorovi, preduslovi, materijal po čvoru)
- [ ] Kako LLM odgovor učenika pretvara u ažuriranje stanja
- [ ] Pravilo „stavka je naučena“: polazna tačka je ALEKS-ov skor (+1, drugi uzastopni +2, −1, cilj 5, pet promašaja zaredom = neuspeh)
- [ ] Šum u proceni iz razgovora: kako LLM sudija pretvara slobodan odgovor u tačno/netačno, i koliko su pogađanje i greške iz nepažnje veći nego u ALEKS-u
- [ ] Edge case-ovi: pogađanje, slučajne greške, zaboravljanje, skretanje sa teme, tutor koji potvrdi pogrešnu tvrdnju učenika (Tio i sar., „agreeable inaccuracies“)
- [ ] Pamćenje između sesija: učenik se vraća posle par dana, stanje znanja mora da se sačuva i učita (Gemini to ne radi eksplicitno)
- [ ] Evaluacija: metrike iz Tio i sar. (uspeh, pokrivenost grafa, broj koraka do savladanosti) + simulirani učenici


## Pitanja za mentora
- [x] Da li je SHSAT (My Smart Mentor) prihvatljiv kao „reprezentativni kurs“ za studiju slučaja?
- [ ] Da li je prihvatljivo da je math graf preuzet (Coherence Map), a ELA graf napravljen ručno? (vidi [prostor-znanja/postojeci-grafovi.md](prostor-znanja/postojeci-grafovi.md))
- [ ] Da li je prihvatljivo da se iskoristi iz Learning Commons-a "Learning Components" kao cvorovi koji bi bili informacija LLM-u kako da nauci odredjeni cvor i sta se smatra naucenim cvorom ili postoje neki podaci koje Peter mozda ima vezane za ELA i Math oblasti koje bih mogoa da koristim kao bazu znanja za KST