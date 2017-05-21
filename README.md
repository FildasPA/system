# README

## Auteurs

- Julien BOGE
- Adrien SARTORI

## Librairies utilisées

- os
- psutil
- socket
- time
- datetime
- sqlite3
- feedparser
- flask
- requests
- pygal


Pour les différentes parties :
1)
	Les informations collectées sont :
		nombre d'utilisateurs connectés & nombre de processus
		% utilisation CPU, RAM, disque
2)
	Utilisation d'une base de données sqlite.
	script de sauvegarde fait, script de suppression des données anciennes fait.
	(il me semble) Pas de modification à faire en cas d'ajout d'une machine.

3)
	Affichage en couleur disponible.
	Critère de crise configurable (situation de crise si :
		30 min sans réponse
		CPU = 100%
		RAM = 100%
		Disque > 95% ).
	Contenu de l'email paramétrable (voir fichier config).
	Envoie des emails via le serveur smtp de l'université possible (a ajouter dans le fichier config, exemple déjà disponible) .

4)
