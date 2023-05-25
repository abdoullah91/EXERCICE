#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));  // Initialisation du générateur de nombres aléatoires

    char lettreCachee = 'A' + rand() % 26;  // Génère une lettre aléatoire entre 'A' et 'Z'

    char lettresTrouvees[26] = {0};  // Tableau pour stocker les lettres trouvées
    int nbLettresTrouvees = 0;

    int nbTentatives = 0;
    int maxTentatives = 10;

    printf("Bienvenue dans le jeu de recherche de lettre !\n");

    while (nbTentatives < maxTentatives) {
        printf("Veuillez entrer une lettre : ");
        char lettre;
        scanf(" %c", &lettre);

        // Vérifier si la lettre a déjà été trouvée
        int dejaTrouvee = 0;
        for (int i = 0; i < nbLettresTrouvees; i++) {
            if (lettresTrouvees[i] == lettre) {
                dejaTrouvee = 1;
                break;
            }
        }

        if (dejaTrouvee) {
            printf("Vous avez déjà trouvé cette lettre !\n");
            continue;  // Ignorer le reste de la boucle et passer à l'itération suivante
        }

        nbTentatives++;

        if (lettre == lettreCachee) {
            printf("Félicitations ! Vous avez trouvé la lettre cachée (%c) en %d tentative(s) !\n", lettre, nbTentatives);
            break;  // Sortir de la boucle
        } else {
            printf("Dommage ! La lettre que vous avez entrée n'est pas la bonne.\n");

            if (lettre < lettreCachee) {
                printf("La lettre recherchée est plus grande.\n");
            } else {
                printf("La lettre recherchée est plus petite.\n");
            }
        }

        lettresTrouvees[nbLettresTrouvees] = lettre;
        nbLettresTrouvees++;

        if (nbTentatives == maxTentatives) {
            printf("Vous avez épuisé toutes vos tentatives. La lettre cachée était : %c\n", lettreCachee);
        }
    }

    return 0;
}
