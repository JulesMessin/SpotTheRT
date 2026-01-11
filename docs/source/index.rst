.. SpotTheRT documentation master file, created by
   sphinx-quickstart on Wed Nov  5 10:51:14 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

SpotTheRT
=========

Résumé du projet
----------------

SpotTheRT est un projet étudiant réalisé par un groupe de quatre membres. 
Il s'agit d'un jeu inspiré du "Dobble", où les joueurs doivent identifier rapidement des symboles communs entre deux cartes.

Objectifs
---------

- Créer un jeu pour plusieurs joueurs.
- Appliquer les notions de programmation orientée objet et de gestion d'événements.
- Concevoir une interface graphique.
- Implémenter la logique du jeu Dobble.
- Travailler en équipe et gérer un projet.

Membres du groupe
-----------------

- Jules Messin
- Bastien Avignon
- Nolann Carrée
- Clement Billon

Fonctionnalités principales
---------------------------

- Génération automatique des cartes Dobble avec symboles uniques.
- Détection et validation des symboles communs entre les cartes.
- Affichage du score en temps réel.
- Interface graphique

Technologies utilisées
---------------------

- Python 3.x
- PyQt5 pour l'interface graphique
- Bibliothèques standard pour la gestion du jeu et des cartes



.. toctree::
   :maxdepth: 2
   :caption: Contents:

---

Architecture générale
---------------------

Le projet est structuré selon une architecture MVC :

- **Model** : gestion des données et de la logique du jeu
- **View** : interfaces graphiques PyQt5 et affichage console
- **Controller** : communication réseau et orchestration du jeu

---

Modules Client
==============

client.model
------------

ClientModel
^^^^^^^^^^^

.. class:: ClientModel

    Modèle représentant l’état du client

    .. method:: __init__()

        Initialise le socket client et l’état de connexion

---

client.view.login_view
----------------------

LoginView
^^^^^^^^^

.. class:: LoginView(QMainWindow)

    Fenêtre principale de connexion au serveur

    .. method:: __init__()

        Initialise la fenêtre de connexion

    .. method:: setup_ui_bkiou()

        Construit l’interface graphique de connexion

    .. method:: set_controller(controller)

        Associe le contrôleur à la vue

    .. method:: on_connect()

        Lance la connexion au serveur et affiche le choix host / join

    .. method:: update_status(status)

        Met à jour le statut de connexion affiché

    .. method:: closeEvent(event)

        Gère la fermeture propre du client

---

client.view.join_host_view
--------------------------

RoomDialog
^^^^^^^^^^

.. class:: RoomDialog(QDialog)

    Fenêtre permettant de créer ou rejoindre une salle

    .. method:: __init__(mode, parent=None)

        Initialise la fenêtre selon le mode host ou join

    .. method:: setup_ui_bkiou()

        Construit l’interface graphique de la boîte de dialogue

    .. method:: validate()

        Vérifie le nom de la salle et valide l’action

---

client.view.waiting_room_view
-----------------------------

WaitingRoom
^^^^^^^^^^^

.. class:: WaitingRoom(QMainWindow)

    Salle d’attente avant le lancement de la partie

    .. method:: __init__(username, room_name, is_host, parent=None)

        Initialise la salle d’attente

    .. method:: setup_ui_bkiou()

        Construit l’interface graphique de la salle d’attente

    .. method:: set_controller(controller)

        Associe le contrôleur et connecte les boutons

    .. method:: update_timer()

        Met à jour le timer d’attente

    .. method:: update_player_list(new_players)

        Met à jour la liste des joueurs connectés

    .. method:: on_launch_clicked()

        Envoie la demande de lancement de partie au serveur

---

Modules Serveur
===============

server.socket_utils
-------------------

create_server_socket
^^^^^^^^^^^^^^^^^^^^

.. function:: create_server_socket(host, port)

    Crée et configure le socket serveur TCP

---

server.model.client_thread
--------------------------

ClientThread
^^^^^^^^^^^^

.. class:: ClientThread(Thread)

    Thread gérant un client connecté au serveur

    .. method:: __init__(client_socket, client_address, client_username, controller)

        Initialise le thread client

    .. method:: run()

        Écoute les messages du client et les transmet au contrôleur

---

server.controller.server_controller
------------------------------------

ServerController
^^^^^^^^^^^^^^^^

.. class:: ServerController

    Contrôleur principal du serveur

    .. method:: __init__(server_socket, view)

        Initialise le serveur et les contrôleurs de
```
