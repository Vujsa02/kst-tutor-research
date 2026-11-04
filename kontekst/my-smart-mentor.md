# My Smart Mentor: proizvod u koji se rešenje ugrađuje

## Kako radi danas

- Platforma za pripremu **SHSAT** testa.
- Učenik radi **dijagnostički test od 45 pitanja**.
- Na osnovu odgovora se procenjuje u kojim **oblastima znanja** (knowledge areas) je jak, a u kojim slab.
- Sistem pravi **plan za narednih 12 nedelja**: koje testove da radi i koje oblasti da uči.

**Šta nedostaje:** učenik može samo da radi testove. Nema načina da **uči**.

## Ideja

Posle dijagnostike (ili u nekom drugom trenutku, što je još otvoreno) uključuje se AI agent koji:

1. koristi **prostor znanja** koji je definisao ekspert: čvorove (npr. „linearne funkcije“) i preduslove među njima;
2. zna (ili kroz razgovor utvrdi) **trenutno stanje znanja** učenika;
3. bira sledeći pojam sa **outer fringe-a**, odnosno pojam čije je sve preduslove učenik već savladao;
4. **uči kroz razgovor**, oslanjajući se na materijal vezan za taj čvor (npr. PDF „šta treba da znaš o linearnim funkcijama“);
5. posle **svakog odgovora** učenika **ažurira stanje** i nastavlja dalje.

## Šta treba napraviti

- **Bazu prostora znanja**: čvorove, preduslove i materijal po čvoru. Pravi je ekspert.
- **Agenta** koji koristi tu bazu.
- Odluku **gde se agent uključuje** u postojeći tok (posle dijagnostike, uz nedeljni plan ili posle svakog testa).

## Otvorena pitanja (za fazu arhitekture)

- Kako se 45 pitanja dijagnostike mapiraju na čvorove prostora znanja? Može li dijagnostika da da **početno stanje** pa agent ne mora sve da proverava ispočetka?
- Kako se 12-nedeljni plan i outer fringe slažu? Da li plan postaje dinamičan?
- Edge case-ovi (pogađanje, slučajne greške, zaboravljanje, učenik koji skreće sa teme…) dolaze kasnije.
