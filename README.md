# upec-its-333

Ce répertoire contient les supports de cours ITS 333 présentés en séance (voir slides/,  mis à jour à chaque fin de séance) ainsi que les trames d'exercices à compléter correspondantes.

Chapitres abordés:
* CM1-2 Développement d'APIs aux formats webApi et MCV
* CM3-4 Les bases de données
* CM5 - Swagger UI


# Publication de votre premier projet Git sur votre propre compte GitHub
## Étape 1 – Créer votre dépôt GitHub

1.    Connectez-vous à votre compte GitHub
2.    Cliquez sur New repository
3.    Nom du dépôt : tp-its-333-nom-prenom
4.    Ne cochez aucune option (README, .gitignore, licence)
5.    Cliquez sur Create repository

Vous obtenez une URL de type : https://github.com/ /tp1-its-333-nom-prenom.git
## Étape 2 – Dans le dossier cloné localement :

```
git remote -v
git remote set-url origin https://github.com/<votre-pseudo>/tp1-its-333-nom-prenom.git
git add .
git commit -m "Premier commit"
git push -u origin main ## OU si la branche s'appelle master, git push -u origin master 
``` 
