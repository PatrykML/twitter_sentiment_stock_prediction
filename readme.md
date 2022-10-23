Kod źródłowy ustrukturyzowany jest w pięciu katalogach:

    * datasets - katalog w którym znajdują się wszystkie zbiory danych z których korzystałem w pracy,
    * data_cleaning - wszystkie narzędzia które zostały wykorzystane do eksploracji danych, wyczyszczenia ich oraz połączenia,
    * models - katalog w którym znajdują się modele na podstawie których uzyskałem wyniki,
    * plots - katalog z wykresami wykorzystanymi w pracy,
    * results - katalog z wynikami w formie tekstowej.

Każdy plik z rozszerzeniem ipynb i py posiada krótki opis na temat jego przeznaczenia.

W models możemy znaleźć wszystkie modele predykcyjne, test metodą Grangera i obliczenie liczb Shapleya.

W data_cleaning znajdziemy wstępną eksploracje danych twitterowych i giełdowych, sprawdzenie korelacji Pearsona, wyczyszczenie danych, stworzenie wszystkich zmiennych pomocniczych i agregacje danych.

W datasets znajdziemy pliki z historycznymi notowaniami giełdy, tweety i
zagregowanymi danymi dla każdej spółki. Najnowsze dane w finalnej postaci dla każdej spółki znajdują się w katalogu datasets/v3.

Katalogi plots i results zawierają pliki z wynikami przedstawionymi w formie wykresów w istnotności cech i formie tekstowej w przypadku trafności, F1 i ROC.

Project from a blog post:
https://medium.com/@wieczorekpatryk98/4-important-things-ive-learned-from-my-first-big-data-science-project-and-how-can-they-save-you-dfad06f9304e
