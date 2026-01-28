# Projet Requirements – Maison Intelligente

## Présentation du groupe

Ce projet est réalisé par **Paul Crosnier** et **Roxana Grosfils** dans le cadre du module de *Requirements Engineering*.

Nous travaillons en binôme sur un sujet commun afin de mettre en pratique les méthodes vues en cours : expression des besoins, structuration des exigences et formalisation selon le modèle **PEGS**.

## Contexte du projet

Le projet **Maison Intelligente** consiste à définir et formaliser les exigences d’un système de maison connectée. Dans notre cas nous nous pachons sur le systeme d'alarme. Le système de sécurité surveille le domicile en continu pour détecter les intrusions, les incendies ou les urgences médicales et alerter automatiquement les services de secours appropriés (police, pompiers, SAMU).

L’objectif principal est de produire une **documentation claire, structurée et exploitable**, décrivant les exigences du système selon le formalisme PEGS. Cette documentation est générée automatiquement à partir de fichiers **Markdown**, puis transformée en **HTML** (et potentiellement en PDF) via un script et une chaîne d’intégration continue.

Le dépôt GitHub sert à la fois de support de travail collaboratif et de point d’accès à la documentation générée.

## Objectif du dépôt

Ce dépôt permet de :

* Rédiger les exigences du projet Maison Intelligente en Markdown
* Générer automatiquement une documentation structurée
* Centraliser le travail du groupe
* Faciliter la consultation des exigences via un rendu HTML

## Installation

### Prérequis

* Git
* Python 3.x
* Un environnement compatible avec GitHub Actions (aucune configuration locale spécifique requise pour la génération automatique)

### Étapes d’installation

Clonez le dépôt :

```bash
git clone https://github.com/FormalRequirements/re-2026-roxana-paul.git
```

Accédez au dossier du projet :

```bash
cd re-2026-roxana-paul
```

*(Les dépendances Python éventuelles peuvent être installées si nécessaire selon l’évolution du projet.)*

## Utilisation du projet

Le mode d’utilisation principal du projet repose sur **GitHub Actions** pour générer automatiquement la documentation.

### Génération de la documentation PEGS

1. Rendez-vous sur le dépôt GitHub du projet
2. Cliquez sur l’onglet **Actions**
3. Sélectionnez le workflow **Déployer Documentation PEGS**
4. Cliquez sur **Run workflow**
5. Lancez l’exécution du workflow

Une fois le workflow terminé :

* Ouvrez l’exécution correspondante
* Descendez jusqu’à la section **Artifacts**
* Vous y trouverez le **fichier HTML généré**, correspondant à la documentation PEGS du projet

Ce fichier contient la version rendue et consultable des exigences.

La documentation HTML est également accessible directement en ligne à l’adresse suivante :
[https://formalrequirements.github.io/re-2026-roxana-paul/](https://formalrequirements.github.io/re-2026-roxana-paul/)

## Auteurs

* **Crosnier Paul**
* **Grosfils Roxana**

Lien du projet :
[https://github.com/FormalRequirements/re-2026-roxana-paul.git](https://github.com/FormalRequirements/re-2026-roxana-paul.git)
