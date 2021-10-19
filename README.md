# **Blender Light Manipulation**
A script that makes it easier to work with light

## 1. Wstęp

W poniższej dokumentacji przedstawiony zostanie skrypt, który swoim
działaniem będzie pomagać w manipulowaniu wieloma źródłami świateł
jednocześnie.

## 2. Włączenie skryptu

Po załadowaniu pliku ze skryptem do Blendera możemy go uruchomić.
Spowoduje to pojawienie się nowej zakładki “Oświetlenie” w opcjach z
narzędziami, tam znajdują się wszystkie opcje skryptu.

## 3. Podstawowe opcje

  - Jeżeli nie zaznaczymy żadnego światła, jedyną dostępną opcją będzie
  “Dodaj światło” (Rys. 1). Gdy klikniemy na przycisk “Add Light” pojawi się
  menu z dostępnymi typami świateł do dodania (Rys. 1).

    ![Rys. 1 Widok bez zaznaczonego żadnego światła.](https://i.imgur.com/cUSHbBA.png)

    >Rys. 1 Widok bez zaznaczonego żadnego światła.

    ![Rys. 2 Menu dodawania światła](https://i.imgur.com/fieCnDN.png)

    >Rys. 2 Menu dodawania światła

  - Jeżeli mamy już w scenie światło i jest ono zaznaczone, otwiera się całe
  menu manipulowania światłem (Rys. 3).

    ![Rys. 3 Menu manipulowania światłem](https://i.imgur.com/0Rb0TCx.png)

    >Rys. 3 Menu manipulowania światłem

  - Omówienie opcji manipulowania światłem:
    
    - Lokalizacja
    
      W zakładce lokalizacji znajduje się przycisk “Przenieś” oraz trzy
      slidery odpowiadające koordynatom światła. Kliknięcie przycisku
      powoduje chwycenie źródła światła i przenoszenie go za pomocą
      myszki (analogiczne działanie do skrótu klawiszowego ‘g’). Slidery
      służą do precyzyjnego sterowania pozycją światła. Jeżeli chcemy
      manipulować pozycję wielu świateł za pomocą sliderów, należy
      przytrzymać Alt.
    
      ![Rys. 4 Zakładka Lokalizacja](https://i.imgur.com/mHrpGQI.png)

      >Rys. 4 Zakładka Lokalizacja

    - Rozmiar
    
      Zakładka rozmiar jest podobna do zakładki lokalizacji. Znajdziemy
      tu przycisk do zmiany rozmiaru (działanie analogiczne do skrótu
      klawiszowego ‘s’), oraz slidery do precyzyjnego skalowania światła.
      Jeżeli chcemy manipulować rozmiarem wielu świateł za pomocą
      sliderów, należy przytrzymać Alt.

      ![Rys. 5 Zakładka Rozmiar](https://i.imgur.com/teB5Xn0.png)

      >Rys. 5 Zakładka Rozmiar

    - Rotacja
    
      Ponownie zakładka, przypominająca poprzednie. Znajduje się w niej
      przycisk do obrotu (działanie analogiczne do skrótu klawiszowego
      ‘r’), oraz slidery do precyzyjnego obrotu źródła światła. Jeżeli
      chcemy manipulować obrót wielu świateł za pomocą sliderów,
      należy przytrzymać Alt.

      ![Rys. 6 Zakładka Rotacja](https://i.imgur.com/WgZ8N08.png)

      >Rys. 6 Zakładka Rotacja

    - Światło
    
      Jest to zakładka zawierająca właściwości światła, takie jak: nazwa,
      typ światła, kolor i inne ustawienia zależące od typu światła.
      Dostępne opcje różnią się w zależności od typu światła (np. Dla
      światła typu spot dostępna jest właściwość rozmycie, a dla światła
      typu sun właściwość kąt).

      ![Rys. 7 Zakładka Światło](https://i.imgur.com/aNuwhaq.png)

      >Rys. 7 Zakładka Światło

    - Podgląd
    
      W zakładce podgląd znajduje się podgląd aktualnie zaznaczonego
      światła (UWAGA! Podgląd nie odświeża się po każdej zmianie
      właściwości światła. Aby odświeżyć podgląd należy przeskalować
      okienko z podglądem).

      ![Rys. 8 Zakładka Podgląd](https://i.imgur.com/7xYWxwH.png)

      >Rys. 8 Zakładka Podgląd

    - Zaznacz wszystkie
    
      W tej zakładce znajduje się przycisk “Zaznacz wszystkie”, który
      zaznacza wszystkie światła znajdujące się na scenie i wyświetla ich
      właściwości.

      ![Rys. 9 Zakładka Wszystkie światła](https://i.imgur.com/XDxmPbx.png)

      >Rys. 9 Zakładka Wszystkie światła

## 4. Przykład użycia skryptu

  W ramach przykładu stworzona zostanie scena z obiektami, które zostaną
  oświetlone przy pomocy skryptu.
  
  - Najpierw dodane zostały obiekty typu plane i monkey, dla obiektu
  plane dodane zostały shadery.
  
  ![](https://i.imgur.com/7ZsDZef.png)

  - Teraz za pomocą opcji “Add Light” z zakładki “Dodaj światło” dodane
  zostało źródło światła typu Area. W zakładce lokalizacja zmienione
  zostały koordynaty Y oraz Z, a w zakładce rotacja zmieniony został
  koordynat X. W zakładce światło zwiększono energię światła oraz
  zmieniono kolor.
  
  ![](https://i.imgur.com/8f0vdGg.png)

  - Następnie dodano dwa światła typu Spot (analogicznie jak w punkcie
  b). Zmieniono ich pozycję w osi Z i Y (przytrzymując Alt zmieniono
  pozycję obu świateł na raz). Zmieniono także ich obrót. W zakładce
  Wszystkie światła zmieniono energię, kolor i rozmycie światła.
  
  ![](https://i.imgur.com/YpmBVF0.png)

  - Dodając światło typu sun i modyfikując jego właściwości dodano
  niebieską poświatę (Zmieniono także kolor jednego ze świateł typu
  spot).
  
  ![](https://i.imgur.com/bpXiLvR.png)

  - Na koniec dodano światło typu Area oświetlające jeden bok.
  
  ![](https://i.imgur.com/NgyEeGU.png)
