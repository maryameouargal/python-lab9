import numpy as np

# ETAPE 2
# Créer un tableau 1D (vecteur)
tableau_id = np.array([1, 2, 3, 4, 5])
print("tableau 1D:", tableau_id)

# Créer un tableau 2D (matrice)
tableau_2d = np.array([[1, 2, 3],[4, 5, 6]])
print("tableau 2D :\n", tableau_2d)

# Tableau rempli de zéros
zeros = np.zeros((2, 3)) 
print("zeros :\n", zeros)

# Tableau rempli de uns
ones = np.ones((3, 2))  
print("ones :\n", ones)

# Suite arithmétique
progression = np.arange(0, 10, 2)  
print("np.arange :", progression)  


# Division d'un intervalle en parties égales
linspace = np.linspace(0, 1, 5)  
print("np.linspace :", linspace)  

# ETAPE 3
# Examiner les propriétés des tableaux créés
print("tableau_id:")
print("dtype :", tableau_id.dtype)  # type des éléments (int64, float64…)
print("ndim  :", tableau_id.ndim)   # nombre de dimensions
print("shape :", tableau_id.shape)  # tuple de dimensions
print("size  :", tableau_id.size)   # nombre total d'éléments

#ETAPE 4
# Création d'un vecteur de 1 à 9
vecteur = np.arange(1, 10)
print("vecteur :", vecteur)

# Transformation en matrice 3x3
matrice = vecteur.reshape((3, 3))
print("Matrice 3×3 :\n", matrice)

# Vérification des dimensions
print("Shape :", matrice.shape)
print("Size :", matrice.size)

#4.2
#Utiliser  pour calculer automatiquement une dimension
matrice_auto = vecteur.reshape((3, -1))
print("Shape auto :", matrice_auto.shape) 

# ETAPE 5
# Création avec type spécifique
tableau_specifique = np.array([1, 2, 3], dtype=np.float32)
print("Tableau avec dtype=np.float32:", tableau_specifique)
print("dtype:", tableau_specifique.dtype)

# Conversion de type
tableau_convertis = tableau_specifique.astype(np.int32)
print("Modifié avec .astype(np.int32):", tableau_convertis)
print("dtype:", tableau_convertis.dtype)

# Comparez la mémoire utilisée 
print("Mémoire (float32):", tableau_specifique.nbytes, "octets")
print("Mémoire (int32):", tableau_convertis.nbytes, "octets")

#5.2
# Matrice identité 
matrice_identite = np.eye(4)
print("Matrice identité np.eye(4):\n", matrice_identite)

# Tableau rempli d'une valeur constante
tableau_constant = np.full((2, 2), 7)
print("Tableau constant np.full((2, 2), 7):\n", tableau_constant)

# Test d'autres formes
print("\nTester  de reshape avec np.arange(12).reshape((4, 3)):")
autre_forme = np.arange(12).reshape((4, 3))
print(autre_forme)

#5.3
# Réutilisation de la matrice 3x3
vecteur = np.arange(1, 10)
matrice = vecteur.reshape((3, 3))

# Multiplication de chaque élément
print("Matrice originale :\n", matrice)
print("\nMatrice * 10 :\n", matrice * 10)

print("\nVecteur original :", vecteur)
print("np.sqrt(vecteur) :", np.sqrt(vecteur))

#INTÉRÊT DES OPÉRATIONS VECTORISÉES :
#- Performance : beaucoup plus rapide que les boucles Python
#- Concision : code plus court et plus lisible
#- Pas de boucle nécessaire 
