# 🎙️ Installer Whisper — Guide pas-à-pas

> **Whisper** est un outil créé par OpenAI qui permet de **transcrire automatiquement un fichier audio en texte**.
>
> Ce guide vous accompagne de A à Z.

---

## 📋 Ce dont vous avez besoin avant de commencer

- ✅ Un ordinateur sous **Windows 10 ou 11**
- ✅ Une **connexion internet**
- ✅ Un **fichier audio** à transcrire (`.mp3`, `.wav`, `.m4a`, etc.)

---

## Étape 1 : Installer Python

Python est le programme qui fait tourner Whisper. Vous devez l'installer en premier.

1. Cliquer sur ce lien : 
   
    👉 **https://www.python.org/ftp/python/3.12.9/python-3.12.9-amd64.exe**

    > Le téléchargement de l'installateur python devrait se lancer automatiquement.

2. ⚠️ **TRÈS IMPORTANT** : Sur le premier écran de l'installateur, **cochez la case en bas** :

   ```
   ☑ Add python.exe to PATH 
   ```

   > *Si vous oubliez cette étape, rien ne fonctionnera par la suite.*

3. Cliquez sur **« Install Now »**

4. Attendez la fin de l'installation, puis cliquez sur **« Close »**

### ✅ Vérification

1. Appuyez sur les touches **`Windows` + `R`** en même temps
2. Tapez `cmd` puis appuyez sur **Entrée**
3. Dans la fenêtre noire qui s'ouvre, copiez-collez cette commande puis appuyez sur **Entrée** :

   ```
   python --version
   ```

4. Vous devriez voir apparaître quelque chose comme `Python 3.12.x` → c'est bon ✅
5. Si vous voyez une erreur, recommencez l'étape 1 en n'oubliant pas de cocher **« Add Python to PATH »**

---

## Étape 2 : Installer FFmpeg

FFmpeg est un outil qui permet à Whisper de lire les fichiers audio. On va l'installer via **Chocolatey**, un installateur de programmes en ligne de commande.

### Installer Chocolatey

1. Cliquez sur le bouton **Démarrer** (en bas à gauche), tapez **`PowerShell`**

2. Faites un **clic droit** sur **« Windows PowerShell »** et choisissez **« Exécuter en tant qu'administrateur »**

   > ⚠️ Si une fenêtre vous demande « Voulez-vous autoriser cette application... », cliquez sur **Oui**

3. Dans la fenêtre bleue qui s'ouvre, copiez-collez cette commande **en un seul bloc** puis appuyez sur **Entrée** :

   ```
   Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
   ```

4. ⏳ **Patientez** — du texte va défiler, c'est normal. Attendez que le curseur réapparaisse.

### Installer FFmpeg avec Chocolatey

5. **Dans la même fenêtre PowerShell (administrateur)**, copiez-collez cette commande puis appuyez sur **Entrée** :

   ```
   choco install ffmpeg -y
   ```

6. ⏳ **Patientez** — l'installation se fait toute seule. Quand c'est terminé, vous verrez un message indiquant que l'installation a réussi.

7. **Fermez** la fenêtre PowerShell

### ✅ Vérification

1. Ouvrez une **nouvelle** fenêtre de commande : **`Windows` + `R`** → tapez `cmd` → **Entrée**
2. Copiez-collez cette commande puis appuyez sur **Entrée** :

   ```
   ffmpeg -version
   ```

3. Vous devriez voir plusieurs lignes d'informations s'afficher → c'est bon ✅
4. Si vous voyez `'ffmpeg' n'est pas reconnu...`, fermez la fenêtre, rouvrez-en une nouvelle et réessayez. Si ça ne marche toujours pas, relancez la commande `choco install ffmpeg -y` dans un PowerShell administrateur.

---

## Étape 3 : Installer Whisper

Maintenant on installe Whisper lui-même.

1. Ouvrez une fenêtre de commande : **`Windows` + `R`** → tapez `cmd` → **Entrée**

2. Copiez-collez cette commande puis appuyez sur **Entrée** :

   ```
   pip install -U openai-whisper
   ```

3. ⏳ **Patientez** — l'installation peut prendre **plusieurs minutes**. Des lignes de texte vont défiler, c'est normal.

4. L'installation est terminée quand vous voyez à nouveau la ligne qui commence par `C:\Users\...>` et que le curseur clignote

### ✅ Vérification

Copiez-collez cette commande puis appuyez sur **Entrée** :

```
whisper --help
```

Vous devriez voir un long texte d'aide s'afficher → c'est bon ✅

---

## Étape 4 : Télécharger le script de transcription

On va utiliser un petit script Python prêt à l'emploi qui simplifie la transcription.

1. Téléchargez le fichier **`whisper_code.py`** (il vous a été fourni avec ce tutoriel)

2. **Placez-le dans le même dossier que vos fichiers audio** (par exemple sur le Bureau)

---

## Étape 5 : Transcrire un fichier audio 🎉

Vous y êtes ! Voici comment transcrire un fichier audio.

### Configurer le script

1. Faites un **clic droit** sur le fichier **`whisper_code.py`** → **« Ouvrir avec »** → **« Bloc-notes »**

2. Tout en haut du fichier, vous verrez une section **⚙️ PARAMÈTRES À MODIFIER**. Modifiez les 4 lignes suivantes :

   ```python
   # Nom du fichier audio (avec son extension)
   fichier_audio = "enregistrement.mp3"

   # Dossier où se trouve le fichier audio
   dossier_audio = "C:/Users/MonNom/Desktop"

   # Langue de l'audio : "fr" pour français, "en" pour anglais
   langue = "fr"

   # Modèle Whisper : "tiny", "base", "small", "medium" ou "large"
   modele_whisper = "medium"
   ```

   **Ce qu'il faut changer :**
   - Remplacez `enregistrement.mp3` par le **nom exact** de votre fichier audio
   - Remplacez `C:/Users/MonNom/Desktop` par le **chemin du dossier** où se trouve votre fichier audio
   - Changez la langue si besoin (`"fr"` ou `"en"`)
   - Changez le modèle si besoin (voir le tableau des modèles plus bas)

   > 💡 **Pour trouver le chemin de votre dossier** : ouvrez l'Explorateur de fichiers, allez dans le dossier, cliquez dans la barre d'adresse en haut et copiez le chemin. Remplacez les `\` par des `/`.

3. **Enregistrez** le fichier : **`Ctrl` + `S`**

4. Fermez le Bloc-notes

### Lancer la transcription

5. **Double-cliquez** sur le fichier **`whisper_code.py`**

   > Une fenêtre noire s'ouvre avec des messages de progression.

6. ⏳ **Patientez** — la transcription peut prendre **de quelques minutes à plusieurs dizaines de minutes** selon la durée de l'audio. Vous verrez les messages suivants :
   - `Chargement du modèle...` → le programme se prépare
   - `Transcription en cours...` → ça travaille
   - `🎉 Le fichier texte a été créé` → c'est terminé !

7. Appuyez sur **Entrée** pour fermer la fenêtre

8. Allez dans le dossier de votre fichier audio : vous y trouverez un nouveau fichier **`transcription_NomDuFichier.txt`**

9. Ouvrez-le avec le **Bloc-notes** pour lire votre transcription 🎉

> 💡 **Pour transcrire un autre fichier** : rouvrez `whisper_code.py` avec le Bloc-notes, changez le nom du fichier audio dans les paramètres, enregistrez, et double-cliquez à nouveau dessus.

---

## 📌 Récapitulatif des modèles

| Modèle | Qualité | Vitesse | RAM nécessaire |
|--------|---------|---------|----------------|
| `tiny` | ⭐ | Très rapide | ~1 Go |
| `base` | ⭐⭐ | Rapide | ~1 Go |
| `small` | ⭐⭐⭐ | Moyen | ~2 Go |
| `medium` | ⭐⭐⭐⭐ | Lent | ~5 Go |
| `large` | ⭐⭐⭐⭐⭐ | Très lent | ~10 Go |

> **Conseil** : commencez avec `medium`. Si c'est trop long ou que votre PC rame, essayez `small` ou `base`.
>
> Pour changer de modèle, remplacez `--model medium` par `--model small` (ou autre) dans la commande.

---

## ❓ En cas de problème

### « 'python' n'est pas reconnu comme commande interne »
→ Vous avez oublié de cocher **« Add Python to PATH »** à l'étape 1. Désinstallez Python (dans Paramètres > Applications) et recommencez l'étape 1.

### « 'pip' n'est pas reconnu comme commande interne »
→ Même problème que ci-dessus. Désinstallez et réinstallez Python en cochant bien la case PATH.

### « 'ffmpeg' n'est pas reconnu comme commande interne »
→ FFmpeg n'est pas bien installé. Ouvrez un **PowerShell en administrateur** et relancez `choco install ffmpeg -y`. N'oubliez pas de **fermer et rouvrir** la fenêtre de commande après l'installation.

### « No module named 'whisper' »
→ Whisper ne s'est pas installé correctement. Relancez la commande de l'étape 3 :
```
pip install -U openai-whisper
```

### La transcription est de mauvaise qualité
→ Essayez un modèle plus gros : remplacez `--model medium` par `--model large` dans la commande.
→ Assurez-vous que l'audio est de bonne qualité (pas trop de bruit de fond).

### Mon PC est très lent pendant la transcription
→ C'est normal, Whisper utilise beaucoup de ressources. Essayez un modèle plus petit (`small` ou `base`).
→ Fermez les autres programmes pendant la transcription.

### J'ai une erreur que je ne comprends pas
→ Copiez le message d'erreur complet et recherchez-le sur Google. Vous trouverez souvent la solution sur des forums.

---

> 💡 **Astuce** : une fois que tout est installé, vous n'avez plus besoin de refaire les étapes 1 à 3. Pour transcrire un nouveau fichier, reprenez directement à l'**étape 5**.
