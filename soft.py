import matplotlib.image as mpimg
import numpy as np
import copy

import subprocess

from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

from fonction import *


class Image:
    def __init__(self):
        self.chemin = ""
        self.nom = ""
        self.matrice = []
        self.nbreLigne = -1
        self.nbreColonne = -1

    def setMatrice(self):
        self.matrice = mpimg.imread(self.chemin+self.nom)
        self.matrice = (self.matrice * 255).astype(np.uint8)

        self.nbreLigne = len(self.matrice)
        self.nbreColonne = len(self.matrice[0])

    def extractionNom(self, chemin):
        i = 3
        while (chemin[len(chemin)-1-i] != '/'):
            i += 1
        self.nom = chemin[len(chemin)-i:]
        self.chemin = chemin[:len(chemin)-i]

    def pres(self):
        """
            Utile pour déboguer.
        """
        print(self.nom)
        print(self.nbreColonne)
        print(self.nbreLigne)
        print(self.chemin)
        print("--Fin--")


def actionBouton(typeImage, image, texteImage):
    chemin = askopenfilename(title="Sélectionner l'image " + typeImage, filetypes=[
        ('Fichiers en png', '.png'), ('Tous les fichiers', '.*')])
    if (len(chemin) != 0):
        if (chemin[len(chemin)-4:].upper() == ".PNG"):
            image.extractionNom(chemin)
            image.setMatrice()
            if (typeImage != "fusionnée"):
                verificationFusion()
            texteImage.set("Image sélectionnée\n" + image.nom)
            fenetre.update_idletasks()

        else:
            showerror("Erreur dans la sélection",
                      "Ce programme ne prend que des images en .png", icon="error")


def actionRetourOriginal(typeImage, image, texteImage):
    actionBouton(typeImage, image, texteImage)
    selectionSauvegarde(image)

    texteImage.set("Défusion en cours ...")

    pourcentage = 0
    ancien = 0

    for i in range(image.nbreLigne):
        for v in range(image.nbreColonne):
            for k in range(3):
                image.matrice[i][v][k] = fromOctetToDec(octetFromPoidsForts(
                    extractionPoidsFaibles(fromDecToOctet(image.matrice[i][v][k]), 4)))

        pourcentage = int(i/image.nbreLigne*100)
        if (pourcentage != ancien):
            ancien = pourcentage
            texteChargement.set("État : " + str(pourcentage) + " %")
            fenetre.update_idletasks()

    texteChargement.set("Aucune fusion en cours")
    texteImage.set("Fusion terminée.\nSélectionner une nouvelle image.")
    fenetre.update_idletasks()

    mpimg.imsave(image.chemin+image.nom, image.matrice)

    chemin = image.chemin[:-1]
    cheminFinal = ""

    for i in chemin:
        if i == '/':
            cheminFinal += '\\'
        else:
            cheminFinal += i
    subprocess.Popen(r'explorer ' + cheminFinal)


def verificationFusion():
    if (imageCachee.nbreColonne != -1 and imageVisible.nbreColonne != -1):
        if(imageCachee.nbreColonne != imageVisible.nbreColonne or imageCachee.nbreLigne != imageVisible.nbreLigne):
            showwarning("Images de tailles différentes",
                        "Attention les images choisies sont de tailles différentes.\nLors de la fusion, l'image sera rognée.", icon="warning")
            texteImageFusion.set(
                "Prêt pour la fusion des images.\nAttention l'image finale sera rognée.")
            fenetre.update_idletasks()
        else:
            texteImageFusion.set("Prêt pour la fusion des images.")
            fenetre.update_idletasks()


def actionFusion():
    if (imageCachee.nbreColonne != -1 and imageVisible.nbreColonne != -1):
        fusion = gestionDesTailles(imageVisible, imageCachee)
        selectionSauvegarde(fusion)

        texteImageFusion.set("Fusion en cours ...")

        pourcentage = 0
        ancien = 0

        for i in range(fusion.nbreLigne):
            for v in range(fusion.nbreColonne):
                for k in range(3):
                    octetImageVisible = fromDecToOctet(
                        imageVisible.matrice[i][v][k])
                    octetImageCachee = fromDecToOctet(
                        imageCachee.matrice[i][v][k])

                    octetImageFusion = insertionPoidsFaible(
                        octetImageVisible, extractionPoidsForts(octetImageCachee, 4))

                    fusion.matrice[i][v][k] = fromOctetToDec(
                        octetImageFusion)

            pourcentage = int(i/fusion.nbreLigne*100)
            if (pourcentage != ancien):
                ancien = pourcentage
                texteChargement.set("État : " + str(pourcentage) + " %")
                fenetre.update_idletasks()

        texteChargement.set("Aucune fusion en cours")
        texteImageFusion.set(
            "Fusion terminée.\nSélectionner des nouvelles images.")
        fenetre.update_idletasks()

        mpimg.imsave(fusion.chemin+fusion.nom, fusion.matrice)

        chemin = fusion.chemin[:-1]
        cheminFinal = ""

        for i in chemin:
            if i == '/':
                cheminFinal += '\\'
            else:
                cheminFinal += i
        subprocess.Popen(r'explorer ' + cheminFinal)

    else:
        showerror("Erreur dans la sélection",
                  "Il faut sélectionner deux images pour pouvoir les fusionner", icon="error")


def selectionSauvegarde(image):

    chemin = asksaveasfilename(title="Choix de l'emplacement de sauvegarde", filetypes=(
        ('Fichiers png', '.png'), ("Tous les fichiers", "*.*")))
    image.extractionNom(chemin)


def gestionDesTailles(imageUn, imageDeux):
    if (imageUn.nbreColonne < imageDeux.nbreColonne):
        fusion = copy.copy(imageUn)
    else:
        fusion = copy.copy(imageDeux)
    val = min(imageUn.nbreLigne, imageDeux.nbreLigne)
    fusion.matrice = fusion.matrice[:val]
    fusion.nbreLigne = len(fusion.matrice)
    return(fusion)


imageVisible = Image()
imageCachee = Image()
imageRetourOriginal = Image()


fenetre = Tk()
fenetre.title("Fusionner des images || Youtube : Théorisons")

texteImageVisible = StringVar()
texteImageCachee = StringVar()
texteImageFusion = StringVar()
texteImageRetourOriginal = StringVar()
texteChargement = StringVar()


cadreFusion = LabelFrame(
    fenetre, text="Fusionner des images", padx=50, pady=50, labelanchor="n")
cadreFusion.grid(row=1, column=1)

boutonImageVisible = Button(cadreFusion, text="Sélectionner l'image visible",
                            command=lambda: actionBouton("visible", imageVisible, texteImageVisible)).grid(row=1, column=1)
Label(cadreFusion, textvariable=texteImageVisible).grid(row=2, column=1)
texteImageVisible.set("Aucune image sélectionnée")

Label(cadreFusion, padx=25).grid(row=1, column=2)  # Séparateur vertical

boutonImageCachee = Button(cadreFusion, text="Sélectionner l'image à cacher",
                           command=lambda: actionBouton("à cacher", imageCachee, texteImageCachee)).grid(row=1, column=3)
Label(cadreFusion, textvariable=texteImageCachee).grid(row=2, column=3)
texteImageCachee.set("Aucune image sélectionnée")

Label(cadreFusion, pady=15).grid(row=3, column=2)  # Séparateur horizontal

boutonFusion = Button(cadreFusion, text="Cliquer pour fusionner les images",
                      command=actionFusion).grid(row=4, column=1, columnspan=3)
Label(cadreFusion, textvariable=texteImageFusion).grid(
    row=5, column=1, columnspan=3)
texteImageFusion.set("Sélectionner les images à fusionner")


cadreRetourOriginal = LabelFrame(fenetre,  padx=50, pady=50)
cadreRetourOriginal.grid(row=2, column=1)

boutonExtractionImageCachee = Button(
    cadreRetourOriginal, text="Retrouver l'image cachée", command=lambda: actionRetourOriginal("fusionnée", imageRetourOriginal, texteImageRetourOriginal)).grid(row=1, column=1)
Label(cadreRetourOriginal, textvariable=texteImageRetourOriginal).grid(
    row=2, column=1)
texteImageRetourOriginal.set("Aucune image sélectionnée")


cadreEtatAvancement = LabelFrame(
    fenetre, text="État de l'avancement", padx=50, pady=50, labelanchor="n")
cadreEtatAvancement.grid(row=3, column=1)


Label(cadreEtatAvancement, textvariable=texteChargement).grid(row=1, column=1)
texteChargement.set("Aucune fusion en cours")


fenetre.mainloop()
