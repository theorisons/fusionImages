def fromDecToOctet(nombre):
    """
        Prend un entier entre 0 et 255.

        Renvoie l'octet correspondant. 
        Liste de 8 éléments : de droite -> gauche, LMS (bit de poids faible) -> MSB (bit de poids fort).

        >>> fromDecToOctet(125)
        [0, 1, 1, 1, 1, 1, 0, 1]
    """
    octet = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(7, -1, -1):
        octet[i] = nombre % 2
        nombre //= 2
    return(octet)

def fromOctetToDec(octet):
    """
        Prend un octet.
        Liste de 8 éléments : de droite -> gauche, LMS (bit de poids faible) -> MSB (bit de poids fort).

        Renvoie l'entier en décimal correspondant.

        >>> fromOctetToDec([0, 1, 1, 1, 1, 1, 0, 1])
        125
    """
    nombre = 0
    for i in range(7, -1, -1):
        nombre += octet[i]*2**(7-i)
    return(nombre)


def extractionPoidsFaibles(octet, nbre):
    """
        Prend un octet.
        Liste de 8 éléments : de droite -> gauche, LMS (bit de poids faible) -> MSB (bit de poids fort).
        Un entier compris entre 0 et 8.

        Renvoie le nombre de bits de poids faibles de l'octet considéré.

        >>> extractionPoidsFaibles([0, 1, 1, 1, 1, 1, 0, 1], 3)
        [1, 0, 1]
    """
    extraction = []
    for i in range(nbre-1, -1, -1):
        extraction += [octet[7-i]]
    return(extraction)

def extractionPoidsForts(octet, nbre):
    """
        Prend un octet.
        Liste de 8 éléments : de droite -> gauche, LMS (bit de poids faible) -> MSB (bit de poids fort).
        Un entier compris entre 0 et 8.

        Renvoie le nombre de bits de poids forts de l'octet considéré.

        >>> extractionPoidsForts([0, 1, 1, 1, 1, 1, 0, 1], 3)
        [0, 1, 1]
    """
    extraction = []
    for i in range(nbre):
        extraction += [octet[i]]
    return(extraction)


def insertionPoidsFaible(octet, sequence):
    """
        Prend un octet.
        Liste de 8 éléments : de droite -> gauche, LMS (bit de poids faible) -> MSB (bit de poids fort).
        Prend une liste d'éléments composés de 0 et 1 de taille inférieure ou égale à 8.

        Renvoie l'octet en remplacant ses bits de poids faible par la séquence.
        Liste de 8 éléments : de droite -> gauche, LMS (bit de poids faible) -> MSB (bit de poids fort).

        >>> insertionPoidsFaible([0, 1, 1, 1, 1, 1, 0, 1], [0, 1, 0])
        [0, 1, 1, 1, 1, 0, 1, 0]
    """
    nouveauOctet = octet.copy()
    for i in range(len(sequence)):
        nouveauOctet[7-i] = sequence[len(sequence)-1-i]
    return(nouveauOctet)

def octetFromPoidsForts(sequence):
    """
        Prend une liste d'éléments composés de 0 et 1 de taille inférieure ou égale à 8.

        Renvoi un octet en considérant la séquence comme étant des bits de poids forts.
        Liste de 8 éléments : de droite -> gauche, LMS (bit de poids faible) -> MSB (bit de poids fort).

        >>> octetFromPoidsForts([0, 1, 0])
        [0, 1, 0, 0, 0, 0, 0, 0]
    """
    octet = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(sequence)):
        octet[i] = sequence[i]
    return(octet)