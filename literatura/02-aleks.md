# ALEKS: KST u praksi (bez razgovora)

**Izvor:** Cosyn, Uzun, Doble, Matayoshi (2021), *A practical perspective on knowledge space theory: ALEKS and its data*, Journal of Mathematical Psychology 101 **Pročitano:** 2026-11-04

Dopunski izvori: Doignon & Falmagne (arXiv:1511.06757, samo apstrakt), Matayoshi i sar. (EDM 2022, samo uvod).

**Napomena o čitanju:** pročitao sam uvod, opis sistema, evaluaciju procene, učenje, zaboravljanje i diskusiju. Matematičke definicije slojeva stanja (Sekcija 2.3) i dodatak nisam prolazio detaljno. Tekst je izvučen iz PDF-a skriptom, pa formule nisu pouzdane, ali proza jeste.

## Šta je to

**ALEKS** (*Assessment and LEarning in Knowledge Spaces*) je komercijalni sistem za adaptivno učenje matematike, hemije, statistike i računovodstva, koji koristi **oko 4–5 miliona učenika godišnje**. To je najveća industrijska implementacija KST-a. Rad opisuje kako se teorija prevodi u praksu i proverava je na podacima (milioni procena).

**Za mene je važno što:** ALEKS radi tačno ciklus iz teme (procena → outer fringe → učenje → ponovna procena), ali **bez razgovora**. Učenik rešava zadatke u kojima su odgovori i objašnjenja unapred napisani.

## Kako radi

**Struktura znanja.** Kurs ima nekoliko stotina *stavki* (tipično 300–600, npr. „reši jednačinu sa jednom nepoznatom“). *Stanje znanja* je skup stavki koje učenik ume. Zbog preduslova većina podskupova je nemoguća: za kurs od 314 stavki postoji oko **10²³ mogućih stanja** umesto 2³¹⁴ (≈10⁹⁴). Kako se struktura gradi rad ne opisuje, samo upućuje na literaturu.

**Početna procena.**
- To je **probabilistička pretraga** po stanjima. Sistem drži raspodelu verovatnoće nad stanjima, bira pitanje čija je verovatnoća „učenik zna“ oko 50%, pa posle svakog odgovora preračuna verovatnoće.
- Ima **najviše 30 pitanja** (29 adaptivnih + 1 „extra problem“ koje služi samo za evaluaciju sistema). Idealno bi bilo 77, ali je 30 odabrano zbog umora učenika.
- Na kraju je svaka stavka „u stanju“ (verovatnoća >80%), „van stanja“ (<20%) ili **„neizvesna“**. Neizvesne se ne ubrajaju u stanje, ali se kasnije brže uče.
- Postoji dugme **„ne znam“**: pošto je greška iz nepažnje moguća, netačan odgovor se ne tumači agresivno, a „ne znam“ ubrzava procenu.
- Pitanja su **otvorenog tipa** (bez višestrukog izbora), pa je **pogađanje vrlo retko**. Zato je glavni šum **greška iz nepažnje**.
- Praćenje napretka kasnije radi lokalnu pretragu oko skoro naučenih stavki.

**Učenje (learning mode).**
1. Iz stanja se izračuna outer fringe, tj. stavke koje je učenik „spreman da uči“.
2. **Učenik sam bira** jednu stavku sa tog spiska.
3. Dobije primer sa objašnjenjem, pa vežba nove primere iste stavke. Nova stavka ima „skor“: tačan odgovor +1 (drugi uzastopni +2), netačan −1. Stavka je **privremeno naučena kad skor dostigne 5** (3 za „brze“ slučajeve). **Pet netačnih zaredom** je neuspeh i učenik se nežno usmerava na drugu stavku.
4. Stavka se dodaje u stanje, fringe se preračuna, i tako u krug.
5. Posle određenog broja stavki ili vremena sledi **provera napretka** (progress assessment) koja ažurira stanje i može da **ukloni** stavke koje su zaboravljene.

Autori sami kažu da **šta znači „naučio je stavku“ nije deo KST-a**, već „evoluirajuća heuristika“, kao i ciklus učenje–provera, koji se oslanja na kognitivnu psihologiju (retrieval practice, mešano vežbanje).

## Rezultati iz podataka

- **Procena je dobra:** na preko 3 miliona procena AUROC je 0,86–0,89, a tačnost oko 80–81%. Slika se uglavnom formira za prvih ~10 pitanja, ostatak fino podešava.
- **Slabija je za najlakše stavke**, jer tu dominiraju greške iz nepažnje.
- **Učenje sa fringe-a uglavnom uspeva:** stavka sa outer fringe-a je uspešno naučena u 81% (6. razred), 84% (Algebra I) i 94% (College Algebra) pokušaja. Neuspeha je samo 1–4%. Autori to tumače i kao meru koliko je struktura znanja ispravna.
- **Zaboravljanje:** stavke koje su tek naučene (prvi sloj stanja) padnu na oko 60% tačnih odgovora posle nekoliko dana, a one „dublje u stanju“ drže se oko 80%.
- **Preispitivanje BLIM-a:** klasični model pretpostavlja da verovatnoća pogrešnog odgovora zavisi samo od stavke (konstantna „nepažnja“ i „pogađanje“). Podaci pokazuju da zavisi i od **položaja stavke u odnosu na stanje**.

## Veza sa mojim radom

**Poklapanje:** isti formalni okvir i isti ciklus. ALEKS je dokaz da outer fringe kao izbor sledećeg gradiva radi na velikoj skali i da učenici na njemu uspevaju u većini pokušaja. To je moj najjači oslonac za KST deo dizajna.

**Razlike (i to je prostor mog doprinosa):**
- **Nema razgovora**: objašnjenja su unapred napisana, a procena se radi iz zadataka sa jasnim odgovorom.
- **Učenik sam bira** sa fringe-a, a ne agent.
- **Nema poređenja sa neadaptivnim redosledom** u ovom radu (koliko sam pročitao). Rad proverava da sistem radi onako kako teorija predviđa, ali ne meri da li je bolji od običnog redosleda.
- ALEKS-ova struktura se gradi uz ekspertizu **i velike količine podataka**. Moja je mala i ručna.

## Šta mogu da iskoristim

- **Pravilo za „naučeno“:** ALEKS koristi skor (+1/+2/−1, cilj 5, pet promašaja = neuspeh). Meni treba isto pravilo, a LLM zna da proceni odgovor ali ne i kad je stavka naučena, pa mu to treba zadati. Skor je jednostavan i objašnjiv početak.
- **Tri ishoda procene: u stanju / van stanja / neizvesno.** Neizvesne stavke se ne smeju tretirati kao nepoznate.
- **Dugme „ne znam“** (i u razgovoru: učeniku dati izlaz da kaže da ne zna umesto da pogađa).
- **Ograničen broj pitanja (≤30)** zbog umora, nalazi se i u mom okviru, a uz moju dijagnostiku od 45 pitanja daje ulaznu tačku.
- **Periodična provera naučenog** da bi se uhvatilo zaboravljanje. Fresh-naučene stavke su najranjivije, pa ih treba prve proveravati.
- **Metrike za evaluaciju procene** (AUROC, tačnost, „extra problem“): nasumično pitanje koje ne utiče na procenu, a služi da se proveri koliko je procena tačna. Ovo mogu da preuzmem za proveru svog agenta.
- **Ideja iz EDM 2022:** novi ALEKS-ov motor koji kombinuje neuronsku mrežu i KST bolji je od čistog KST-a, pa KST ne mora da bude jedini izvor procene.

## Šta ne koristim i zašto

- **Skalu i inženjering** (parcijalne podstrukture, optimizacije zbog 10²³ stanja). Moj kurs će verovatno biti mali, pa stanja mogu da se nabroje (proveriti kad se zna broj čvorova).
- **Pretpostavku da pogađanja gotovo nema.** U ALEKS-u to važi zbog otvorenih odgovora. U razgovoru sa LLM-om sudijom je drugačije: odgovor se tumači slobodno, a učenik može da pogodi ili da ponovi ono što je tutor rekao, pa moram uračunati veći i drugačiji šum. (Moje zaključivanje, ne tvrdnja iz rada.)

## Otvorena pitanja

- Kako izgraditi malu strukturu znanja za SHSAT (stavke, preduslovi) i ko je proverava?
- Da li uopšte treba da koristim punu raspodelu verovatnoće nad stanjima, ili je za mali kurs dovoljno jednostavnije praćenje po stavkama?
- Kako LLM sudija iz razgovora izvodi „tačno/netačno“ na način koji je uporediv sa ALEKS-ovim zadacima?
