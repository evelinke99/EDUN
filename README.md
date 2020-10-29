# EDUN
Egyszerű Deriválás Unalom Nélkül

Használati utasítás:

-szükséges csomagok: sympy, numpy, pyQt5, random, pyqtgraph

Az edun.py futtatásával indítható el az alkalmazás.

A főmenüből kiválaszhatjuk, hogy a deriválási szabályok melyikét kívánjuk gyakorolni, illetve találhatunk egy "Kaland" menüt, melyben bonyolultabb feladatokat oldhatunk meg játékosan.

Az első 4 menü gyakorlás végett készült, és hasonló működéssel bír:
->generálódik egy random feladat, melynek megoldását az f'(x) mezőbe írhatjuk be.
-> fontos: A megoldás bevitelekor ügyeljünk a műveleti sorrendre, melyet zárójelekkel jelezzünk!
->az ellenőzés gombbal leellenőrizhetjük megoldásunkat
->amennyiben a megoldás helyes, továbbléphetünk a következő feladatra
->az alapfüggvény bármikor kirajzolódik, a derivált függvény csak abban az esetben ha beírtuk a helyes megoldást

Kaland menü:
Az előzőekhez hasonlóan generálódik egy random feladat, melynek helyességét ellenőrizhetjük.
Helyes válaszok esetén, lépésenként felépíthetünk egy hidat.
Ám vigyázat rossz válasz esetén 2 lépéssel hátrébb kerülhetünk.

Az egyes menükből való kilépés a logóval ellátott gombbal lehetséges, melyre kattintva megjelink egy felugró ablak ami felajánlja a mentés lehetőségét.


