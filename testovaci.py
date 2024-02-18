pismena = ["a", "a", "b", "d", "e", "g"]

while pismena: #len(pismena) != 0
    print(", ".join(pismena))
    zadani = input("Ktere pismeno chces vyhodit?")
    while zadani in pismena:
        pismena.remove(zadani)