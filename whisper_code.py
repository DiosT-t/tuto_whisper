import whisper
import os

# ============================================================
# ⚙️ PARAMÈTRES À MODIFIER
# ============================================================

# Nom du fichier audio (avec son extension mp3, wav, mp4, etc...)
fichier_audio = "enregistrement.mp3"

# Dossier où se trouve le fichier audio
# Exemple : "C:/Users/MonNom/Desktop/Mes_Audios"
dossier_audio = "C:/Users/MonNom/Desktop"

# Langue de l'audio : "fr" pour français, "en" pour anglais
langue = "fr"

# Modèle Whisper : "tiny", "base", "small", "medium" ou "large"
# Plus le modèle est gros, plus la qualité est bonne mais plus c'est lent
modele_whisper = "large"

# ============================================================
# 🚀 NE RIEN MODIFIER EN DESSOUS DE CETTE LIGNE
# ============================================================

chemin_audio = os.path.join(dossier_audio, fichier_audio)
nom_sans_extension = os.path.splitext(fichier_audio)[0]

if not os.path.exists(chemin_audio):
    print(f"❌ ERREUR : le fichier '{chemin_audio}' n'existe pas.")
    print("Vérifiez le nom du fichier et le dossier dans les paramètres ci-dessus.")
    input("Appuyez sur Entrée pour fermer...")
    exit()

print(f"Chargement du modèle '{modele_whisper}'... (cela peut prendre un moment la première fois)")
model = whisper.load_model(modele_whisper)
print("Modèle chargé ✅")

print(f"Transcription de '{fichier_audio}' en cours...")
transcription = model.transcribe(chemin_audio, language=langue)
print("Transcription terminée ✅")

fichier_sortie = os.path.join(dossier_audio, f"transcription_{nom_sans_extension}.txt")
with open(fichier_sortie, "w", encoding="utf-8") as f:
    for segment in transcription["segments"]:
        f.write(f"{segment['text']}\n")

print(f"\n🎉 Le fichier texte a été créé : {fichier_sortie}")
input("Appuyez sur Entrée pour fermer...")