# 🎨 G-SARiko - Image Enhancement Application

G-SARiko est une application web alimentée par l'IA pour améliorer vos photos comme le ferait Google Pixel. Elle offre des fonctionnalités telles que l'ajustement de la luminosité, du contraste, de la netteté et bien d'autres !

## ✨ Fonctionnalités

- 📸 **Téléchargement d'images** : Supportez JPG, JPEG, PNG
- 🎚️ **Ajustements en temps réel** : Luminosité, Contraste, Netteté
- 👀 **Aperçu côte à côte** : Comparez l'image originale et améliorée
- 📥 **Téléchargement facile** : Récupérez votre image améliorée en un clic

## 🚀 Installation

### Prérequis
- Python 3.8+
- pip (gestionnaire de paquets Python)

### Étapes

1. **Clonez le dépôt**
```bash
git clone https://github.com/Dals100/G-SARiko.git
cd G-SARiko
```

2. **Installez les dépendances**
```bash
pip install -r requirements.txt
```

3. **Lancez l'application**
```bash
streamlit run app.py
```

4. **Ouvrez votre navigateur**
L'application s'ouvrira automatiquement sur `http://localhost:8501`

## 📖 Guide d'utilisation

1. Cliquez sur **"Téléchargez votre image"** pour sélectionner une photo
2. Utilisez les curseurs dans la barre latérale pour ajuster :
   - **Luminosité** : De 0.5 (plus sombre) à 2.0 (plus clair)
   - **Contraste** : De 0.5 (moins contrasté) à 2.0 (plus contrasté)
   - **Netteté** : De 0.0 (flou) à 2.0 (très net)
3. Observez les changements en temps réel dans la colonne de droite
4. Cliquez sur **"Télécharger l'image améliorée"** pour enregistrer votre image

## 📦 Dépendances

- **Streamlit** : Framework web pour Python
- **Pillow (PIL)** : Traitement d'images
- **OpenCV** : Vision par ordinateur
- **NumPy** : Calculs numériques

## 🛠️ Technologies

- Python 3
- Streamlit
- OpenCV
- PIL/Pillow
- NumPy

## 📝 Licence

Ce projet est sous licence MIT.

## 👨‍💻 Auteur

Créé par **Dals100**

## 🤝 Contribution

Les contributions sont bienvenues ! N'hésitez pas à créer une issue ou une pull request.

---

**Amusez-vous bien avec G-SARiko ! 🎉**