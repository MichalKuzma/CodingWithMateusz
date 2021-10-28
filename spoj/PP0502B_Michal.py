t = int(input())                                # Wczytaj liczbę testów t
for i in range(t):                              # Pętla wykona się t razy - dla każdego testu
	tab = input().split()[1:]                   # Wczytaj linię z wejścia, podziel po spacjach i przypisz wszystkie, poza pierwszą wartością (od indeksu 1 dalej) do zmiennej tab
	newTab = []                                 # Zmienna newTab będzie przechowywała wartości z tab w odwrotnej kolejności
	for j in range(len(tab) - 1, -1, -1):       # Pętla po wartościach od długości tab - 1 (najwyższy indeks listy tab) do 0 (do -1, "exclusive", czyli bez samego -1), z krokiem -1
		newTab += [tab[j]]                      # Scal listę newTab z listą zawierającą tylko jeden element - tab[j] - w ten sposób każdy kolejny element "od końca" (patrz wyżej) przyklejamy do nowej listy
	print(' '.join(newTab))                     # Na koniec każdego testu wypisz newTab scalone spacjami