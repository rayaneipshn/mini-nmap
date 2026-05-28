# Python Multi-Threaded Port Scanner 🚀

Un scanner de ports TCP rapide et léger écrit en Python, utilisant le multi-threading pour analyser une large plage de ports en quelques secondes. Ce projet a été développé dans le cadre de mon apprentissage en cybersécurité pour comprendre la programmation concurrente et les sockets réseaux.

---

## ✨ Fonctionnalités

* ⚡ **Multi-threading** : Utilisation de `threading` et `queue.Queue` pour scanner jusqu'à 100 ports en simultané sans blocage.
* 🎯 **Précision** : Analyse approfondie des connexions TCP via la bibliothèque native `socket`.
* ⏱️ **Mesure du temps** : Calcul précis et affichage de la durée totale de l'analyse.

---

## 🛠️ Installation & Utilisation

### 1. Cloner le projet
Ouvrez votre terminal et clonez le dépôt GitHub :

```bash
git clone [https://github.com/rayaneipshn/mini-nmap.git](https://github.com/rayaneipshn/mini-nmap.git)
cd mini-nmap

