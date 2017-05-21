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



Pour la configuration du mail, utiliser send_mail pour créer le fichier config et les informations sont:
- title pour le titre de la config du mail (exemple université ou gmail etc)
- sender pour l'expéditeur
- password pour le mot de passe
- receiver pour le destinataire du mail
- smtp pour l'adresse du serveur smtp
- port pour le port par lequel passe le seveur smtp
- message pour le message qui sera affiché

Exemple pour Gmail:
- title = Gmail
- sender = L3avignonessai@gmail.com
- password = mdp
- receiver = L3avignonessai@gmail.com
- smtp = smtp.gmail.com
- port = 465
- message = Une situation de crise a ete rencontree !
