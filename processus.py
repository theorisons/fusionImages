import matplotlib.image as mpimg
import numpy as np

from fonction import *


### ----------------------------------------- ###
### ----------------------------------------- ###
### --- Mettre à 0 un bit de poids faible --- ### 
### ----------------------------------------- ###
### ----------------------------------------- ###



# print("Mettre à 0 un bit de poids faible")
# print("--- Début ---")

# image = mpimg.imread("cubes.png")
# image = (image * 255).astype(np.uint8)

# nbreLigne = len(image)
# print(nbreLigne)

# for i in range (nbreLigne) :

#     print("Traitement en cours : {}%".format(i/nbreLigne*100))

#     for v in range (len(image[0])) :
#         for k in range (3) :

#             octet = fromDecToOctet(image[i][v][k])
#             octet = insertionPoidsFaible (octet, [0])
#             image[i][v][k] = fromOctetToDec(octet)

# mpimg.imsave("cubesMoins1b.png", image)
# print("--- Fin ---")



### -------------------------------------------- ###
### -------------------------------------------- ###
### --- Mettre à 0 deux bits de poids faible --- ### 
### -------------------------------------------- ###
### -------------------------------------------- ###




# print("Mettre à 0 deux bits de poids faible")
# print("--- Début ---")

# image = mpimg.imread("cubes.png")
# image = (image * 255).astype(np.uint8)

# nbreLigne = len(image)
# print(nbreLigne)

# for i in range (nbreLigne) :

#     print("Traitement en cours : {}%".format(i/nbreLigne*100))

#     for v in range (len(image[0])) :
#         for k in range (3) :

#             octet = fromDecToOctet(image[i][v][k])
#             octet = insertionPoidsFaible (octet, [0, 0])
#             image[i][v][k] = fromOctetToDec(octet)

# mpimg.imsave("cubesMoins2b.png", image)
# print("--- Fin ---")



### --------------------------------------------- ###
### --------------------------------------------- ###
### --- Mettre à 0 trois bits de poids faible --- ### 
### --------------------------------------------- ###
### --------------------------------------------- ###



# print("Mettre à 0 trois bits de poids faible")
# print("--- Début ---")

# image = mpimg.imread("cubes.png")
# image = (image * 255).astype(np.uint8)

# nbreLigne = len(image)
# print(nbreLigne)

# for i in range (nbreLigne) :

#     print("Traitement en cours : {}%".format(i/nbreLigne*100))

#     for v in range (len(image[0])) :
#         for k in range (3) :

#             octet = fromDecToOctet(image[i][v][k])
#             octet = insertionPoidsFaible (octet, [0, 0, 0])
#             image[i][v][k] = fromOctetToDec(octet)

# mpimg.imsave("cubesMoins3b.png", image)
# print("--- Fin ---")



### ---------------------------------------------- ###
### ---------------------------------------------- ###
### --- Mettre à 0 quatre bits de poids faible --- ### 
### ---------------------------------------------- ###
### ---------------------------------------------- ###



# print("Mettre à 0 quatre bits de poids faible")
# print("--- Début ---")

# image = mpimg.imread("cubes.png")
# image = (image * 255).astype(np.uint8)

# nbreLigne = len(image)
# print(nbreLigne)

# for i in range (nbreLigne) :

#     print("Traitement en cours : {}%".format(i/nbreLigne*100))

#     for v in range (len(image[0])) :
#         for k in range (3) :

#             octet = fromDecToOctet(image[i][v][k])
#             octet = insertionPoidsFaible (octet, [0, 0, 0, 0])
#             image[i][v][k] = fromOctetToDec(octet)

# mpimg.imsave("cubesMoins4b.png", image)
# print("--- Fin ---")



### ------------------------------------- ###
### ------------------------------------- ###
### --- Cacher une image dans l'autre --- ### 
### ------------------------------------- ###
### ------------------------------------- ###



# print("Cacher une image dans l'autre")
# print("--- Début ---")

# imageVisible = mpimg.imread("cubes.png")
# imageVisible = (imageVisible * 255).astype(np.uint8)

# imageCachee = mpimg.imread("cartes.png")
# imageCachee = (imageCachee * 255).astype(np.uint8)

# nbreLigne = len(imageVisible)

# for i in range (nbreLigne) :    #Attention aucune gestion des tailles. Les images doivent avoir la même taille.

#     print("Traitement en cours : {}%".format(i/nbreLigne*100))

#     for v in range (len(imageVisible[0])) :
#         for k in range (3) :

#             octetVisible = fromDecToOctet(imageVisible[i][v][k])
#             octetCachee = fromDecToOctet(imageCachee[i][v][k])

#             sequencePoidsFort = extractionPoidsForts(octetCachee, 4)

#             octetVisible = insertionPoidsFaible (octetVisible, sequencePoidsFort)

#             imageVisible[i][v][k] = fromOctetToDec(octetVisible)

# mpimg.imsave("imageFusion.png", imageVisible)
# print("--- Fin ---")



### ---------------------------------- ###
### ---------------------------------- ###
### --- Retrouver une image cachée --- ### 
### ---------------------------------- ###
### ---------------------------------- ###



# print("Processus de récupération")
# print("--- Début ---")

# imageFusion = mpimg.imread("imageFusion.png")
# imageFusion = (imageFusion * 255).astype(np.uint8)

# nbreLigne = len(imageFusion)

# for i in range (nbreLigne) :

#     print("Traitement en cours : {}%".format(i/nbreLigne*100))

#     for v in range (len(imageFusion[0])) :
#         for k in range (3) :

#             octet = fromDecToOctet(imageFusion[i][v][k])

#             poidsForts = extractionPoidsFaibles (octet, 4)

#             creationNouveauOctet = octetFromPoidsForts(poidsForts)

#             imageFusion[i][v][k] = fromOctetToDec(creationNouveauOctet)

# mpimg.imsave("imageRecuperee.png", imageFusion)
# print("--- Fin ---")



