# 🔥 SnapchBot - Bot d'Envoi Automatique pour Snapchat

<div align="center">

![Version](https://img.shields.io/badge/version-3.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.11+-yellow.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

**Bot d'envoi automatique de snaps avec statistiques en temps réel**

[Installation](#-installation) • [Configuration](#-configuration) • [Utilisation](#-utilisation) • [Fonctionnalités](#-fonctionnalités)

<img src="https://media.discordapp.net/attachments/1468704863247536229/1468741081586995396/IMG_7730.png?ex=69851f39&is=6983cdb9&hm=8b343d72dbeb9e62a038b769235c6e093e80e789a03e7e6945219c8922670c12&=&format=webp&quality=lossless&width=900&height=1246" width="200" alt="Description" />

</div>

---

## 📋 Table des matières

- [✨ Fonctionnalités](#-fonctionnalités)
- [📦 Prérequis](#-prérequis)
- [⚙️ Configuration Snapchat](#️-configuration-snapchat)
- [🐛 Résolution de problèmes](#-résolution-de-problèmes)

---

## ✨ Fonctionnalités

- 🔥 **Envoi automatique** de snaps à plusieurs groupes simultanément
- 📊 **Statistiques en temps réel** avec design moderne
- 🎯 **Sélection intelligente** des groupes via raccourcis flamme
- 🔄 **Gestion automatique** des erreurs et rechargements
- 🎨 **Interface colorée** et intuitive dans le terminal
- ⚡ **Animations fluides** et compteurs en direct
- 🛡️ **Mode furtif** pour éviter la détection

---

## 📦 Prérequis

### Logiciels requis

| Logiciel | Version | Téléchargement |
|----------|---------|----------------|
| **Python** | 3.11+ | [python.org](https://www.python.org/downloads/) |
| **OBS Studio** | Dernière | [obsproject.com](https://obsproject.com/) |


---





### ✨ Configurer vos identifiants

Créez un fichier `config.txt` à la racine du projet :

```txt
username=votre_username_snapchat
password=votre_mot_de_passe
```

> 🔒 **Sécurité** : Ne partagez JAMAIS votre fichier `config.txt` !

---

## ⚙️ Configuration Snapchat

### 📱 Étapes AVANT de lancer le bot

#### 1. Créer le raccourci flamme 🔥

> ⚠️ **ÉTAPE CRUCIALE** : Sans cette configuration, le bot ne fonctionnera pas !

**Sur Snapchat Web :**

1. Allez sur [web.snapchat.com](https://web.snapchat.com)
2. Connectez-vous à votre compte
3. Faite les 3 petit points en haut à droite.
4. Cliquez sur le bouton **"Nouveau raccourci"**
5. Ajoutez les Groupe et Perssones à spam et nommez le raccourci "🔥".
6. C'est Fini.

**Capture d'écran :**

```
┌─────────────────────────────┐
│  Créer un raccourci          │
├─────────────────────────────┤
│  Nom : 🔥                    │
│                              │
│  Groupes sélectionnés :      │
│  ✓ Groupe 1                  │
│  ✓ Mes potes                 │
│  ✓ Famille                   │
│                              │
│      [Créer]    [Annuler]    │
└─────────────────────────────┘
```

> 💡 **Astuce** : Le bot détectera automatiquement ce raccourci et enverra les snaps à tous les groupes qu'il contient !

#### 2. Configuration OBS Studio 📹

**Pourquoi OBS ?** Snapchat Web nécessite une caméra pour prendre des snaps. OBS crée une caméra virtuelle que le bot peut utiliser.

**Configuration :**

1. Téléchargez et installez **OBS Studio** : [obsproject.com](https://obsproject.com/)
2. Lancez OBS Studio
3. Allez dans le menu **"Outils"** (Tools)
4. Cliquez sur **"Démarrer la caméra virtuelle"** (Start Virtual Camera)
5. Vous devriez voir un message indiquant que la caméra virtuelle est active
6. **Laissez OBS ouvert en arrière-plan**

**Indicateur visuel :**

```
OBS Studio
┌────────────────────────────────┐
│ Outils                          │
│  ✓ Caméra virtuelle démarrée   │
│                                 │
│  [Arrêter la caméra virtuelle] │
└────────────────────────────────┘
```

> ⚠️ **IMPORTANT** : OBS doit être lancé et la caméra virtuelle activée AVANT de lancer le bot !

---

# 🚀 Installation et Lancement

Suivez ces étapes pour installer et configurer le projet correctement une fois snap et obs config.

### 1️⃣ Préparation
* **Télécharger** l'archive du projet (ZIP).
* **Extraire** tous les fichiers dans un dossier local.

### 2️⃣ Installation des dépendances
* **Lancer setup.bat**
* **Lancer start.bat**

---

## 🐛 Résolution de problèmes

### Problèmes fréquents et solutions

<details>
<summary><b>❌ Le bot ne démarre pas</b></summary>

**Symptôme :**
```
'python' n'est pas reconnu en tant que commande...
```

**Causes possibles :**
- Python non installé
- Python pas dans le PATH
- Mauvaise version de Python

**Solutions :**

1. Vérifiez l'installation de Python :
```bash
python --version
# Doit afficher : Python 3.11.x ou supérieur
```

2. Si Python n'est pas trouvé, réinstallez-le en cochant **"Add Python to PATH"**

3. Réinstallez les dépendances :
```bash
pip install --upgrade selenium colorama
```
</details>

<details>
<summary><b>❌ "ChromeDriver not found"</b></summary>

**Symptôme :**
```
selenium.common.exceptions.WebDriverException: 'chromedriver' 
executable needs to be in PATH
```

**Cause :** ChromeDriver manquant ou incompatible avec votre version de Chrome

**Solutions :**

1. Vérifiez votre version de Chrome :
   - Allez dans Chrome
   - Menu → Aide → À propos de Google Chrome
   - Notez le numéro de version (ex: 120.0.6099.109)

2. Téléchargez le ChromeDriver correspondant :
   - [chromedriver.chromium.org](https://chromedriver.chromium.org/)
   - Choisissez la version qui correspond

3. Installation :
   - **Windows** : Placez `chromedriver.exe` dans `C:\Windows\System32\` ou le dossier du projet
   - **Linux/Mac** : `sudo mv chromedriver /usr/local/bin/`

4. Vérifiez l'installation :
```bash
chromedriver --version
```
</details>

<details>
<summary><b>❌ "config.txt introuvable"</b></summary>

**Symptôme :**
```
✗ Fichier config.txt introuvable!
```

**Cause :** Fichier de configuration manquant

**Solution :**

1. Créez un fichier nommé **exactement** `config.txt` (pas `config.txt.txt` !)
2. Placez-le dans le **même dossier** que `snap.py`
3. Contenu du fichier :
```txt
username=votre_username_snapchat
password=votre_mot_de_passe
```

**Vérification :**
- Le fichier doit être dans le même dossier que le script
- Pas d'espaces avant/après le `=`
- Pas de guillemets autour des valeurs
</details>

<details>
<summary><b>❌ Aucun groupe détecté</b></summary>

**Symptôme :**
```
✗ Aucun groupe trouvé!
⚠ Vérifiez que vous avez des groupes avec flamme
```

**Causes possibles :**
- Raccourci flamme 🔥 non créé
- Aucun groupe dans le raccourci
- Mauvais nom de raccourci
- XPath modifié par Snapchat

**Solutions :**

1. **Vérifiez le raccourci :**
   - Allez sur Snapchat Web
   - Prenez un snap
   - Cliquez "Envoyer à" → "Raccourcis"
   - Le raccourci doit s'appeler **exactement** `🔥` (juste l'emoji flamme)

2. **Ajoutez des groupes :**
   - Éditez le raccourci 🔥
   - Ajoutez au moins 1 groupe
   - Sauvegardez

3. **Si le problème persiste :**
   - Supprimez l'ancien raccourci
   - Recréez-en un nouveau nommé 🔥
   - Ajoutez vos groupes
   - Relancez le bot
</details>

<details>
<summary><b>❌ Caméra non détectée</b></summary>

**Symptôme :**
```
✗ Erreur: Camera not found
```

**Cause :** OBS Studio non lancé ou caméra virtuelle non démarrée

**Solution :**

1. Lancez **OBS Studio**
2. Menu **Outils** → **Démarrer la caméra virtuelle**
3. Vérifiez que le message "Caméra virtuelle démarrée" apparaît
4. Laissez OBS **ouvert en arrière-plan**
5. Relancez le bot

**Vérification alternative :**
- Allez sur [web.snapchat.com](https://web.snapchat.com)
- Essayez de prendre un snap manuellement
- Si la caméra fonctionne sur Snapchat, elle fonctionnera avec le bot
</details>

<details>
<summary><b>❌ "Raccourcis" / "Sélectionner" apparaît dans les groupes</b></summary>

**Symptôme :**
Les éléments de menu apparaissent comme des groupes

**Cause :** Bug d'affichage (normalement corrigé en v3.0)

**Solutions :**

1. **Mettez à jour** vers la dernière version :
```bash
git pull origin main
```

2. Si vous utilisez déjà v3.0, le filtrage devrait être automatique

3. Ces éléments sont **automatiquement ignorés** et ne seront pas utilisés pour l'envoi
</details>

<details>
<summary><b>❌ Le bot s'arrête après 3 bugs</b></summary>

**Symptôme :**
```
✗ Trop de bugs consécutifs, actualisation...
```

**Cause :** Problème récurrent (connexion instable, Snapchat laggy, etc.)

**Solutions :**

1. **C'est normal !** Le bot recharge automatiquement la page pour corriger les bugs

2. Si ça arrive trop souvent :
   - Vérifiez votre connexion internet
   - Fermez d'autres onglets Chrome
   - Redémarrez le bot

3. Augmentez les délais dans le code (ligne ~400) :
```python
sleep(3.0)  # Au lieu de 2.5
```
</details>

<details>
<summary><b>❌ CAPTCHA bloque le bot</b></summary>

**Symptôme :**
Snapchat demande de vérifier que vous êtes humain

**Solution :**

1. **Ne paniquez pas !** Le bot attend automatiquement 30 secondes

2. **Résolvez le CAPTCHA manuellement** dans la fenêtre Chrome

3. Appuyez sur ENTRÉE pour continuer

4. Si CAPTCHA apparaît trop souvent :
   - Espacez davantage vos sessions
   - Réduisez le nombre de snaps par session
   - Utilisez un compte moins récent
</details>

---

## 📁 Structure du projet

```
snapchbot/
│
├── 📄 snap.py              # Script principal du bot
├── 📄 config.txt           # Configuration 
│
├── 🔧 setup.bat            # Installation auto 
├── 🚀 start.bat            # Lancement rapide 
│
├── 📖 README.md            # Cette documentation
└── 📜 Star.gif              # Licence MIT
```


## 📜 Changelog

### 🆕 v1.0 (Février 2025)
- ✨ Nouveau design moderne sans tableaux
- 🔥 Animations fluides pour les barres de progression
- 🎯 Meilleur filtrage des groupes (ignore "Raccourcis", "Sélectionner", etc.)
- 📊 Statistiques en temps réel améliorées avec cards
- 🐛 Correction du bug d'affichage des éléments de menu
- ⚡ Optimisation des performances
- 🎨 Interface plus intuitive et agréable


---

## 📄 License

Ce projet est sous licence **MIT**.

**Vous êtes libre de :**
- ✓ Utiliser le code pour un usage personnel ou commercial
- ✓ Modifier le code selon vos besoins
- ✓ Distribuer le code
- ✓ Utiliser le code dans des projets privés

**Conditions :**
- Conserver la notice de copyright
- Fournir une copie de la licence

Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## ⚖️ Disclaimer

> **⚠️ AVERTISSEMENT LÉGAL**

Ce bot est fourni **à des fins éducatives uniquement**. 

**L'auteur n'est PAS responsable de :**
- ❌ Tout ban ou suspension de compte Snapchat
- ❌ Toute utilisation abusive, illégale ou contraire aux ToS
- ❌ Tout dommage direct ou indirect causé par l'utilisation du bot
- ❌ Toute perte de données ou de contacts
- ❌ Tout problème lié à l'automatisation

**En utilisant ce bot, vous acceptez :**
- ✓ D'utiliser le bot **à vos propres risques**
- ✓ De respecter les [Conditions d'Utilisation de Snapchat](https://snap.com/fr-FR/terms)
- ✓ De ne pas utiliser le bot pour du spam ou du harcèlement
- ✓ D'assumer l'entière responsabilité de vos actions

**Note importante :**
L'automatisation peut enfreindre les conditions d'utilisation de Snapchat et entraîner la suspension ou le bannissement de votre compte. Utilisez ce bot de manière responsable et éthique.

---

## 💬 Support et Contact

### 🐛 Signaler un bug

Si vous rencontrez un problème :

1. Vérifiez d'abord la section [Résolution de problèmes](#-résolution-de-problèmes)
2. Si le problème persiste, ouvrez une [issue](https://discord.gg/dKgC3dgGat)


### 📧 Contact direct


- **Discord** : 1s0e
- **Link** : [Dawa-Tools](https://discord.gg/dKgC3dgGat)

---

## 🌟 Remerciements

Merci à tous ceux qui ont contribué à ce projet !

**Technologies utilisées :**
- [Selenium](https://www.selenium.dev/) - Automatisation navigateur
- [Colorama](https://pypi.org/project/colorama/) - Couleurs terminal
- [OBS Studio](https://obsproject.com/) - Caméra virtuelle
- [Python](https://www.python.org/) - Langage principal

---

<div align="center">

### ⭐ Si ce projet vous a aidé, n'hésitez pas à lui donner une étoile ! ⭐

**Made with ❤️ for the Snapchat community**

</div>

---

<div align="center">

**📱 Suivez-moi sur les réseaux !**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/dawa4real)
[![Discord](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)]([https://discord.gg/votre-serveur](https://discord.gg/dKgC3dgGat))

</div>
