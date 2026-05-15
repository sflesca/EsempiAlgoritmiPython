# Dynamic Programming implementation of LCS problem

def lcs(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in range(m + 1)]

    # Following steps build L[m+1][n+1] in bottom up fashion
    # Note: L[i][j] contains length of LCS of X[0..i-1]
    # and Y[0..j-1]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # --- Ricostruzione della sottosequenza ---
    lcs_str = []
    i, j = m, n

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            # Questo carattere fa parte della LCS
            lcs_str.append(X[i - 1])
            i -= 1
            j -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            # Veniamo dalla riga sopra
            i -= 1
        else:
            # Veniamo dalla colonna a sinistra
            j -= 1

    # I caratteri sono stati aggiunti al contrario, quindi invertiamo
    lcs_str.reverse()

    return L[m][n], "".join(lcs_str)




# end of function lcs


# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print("X=", X)
print("Y=", Y)
print("Length of LCS is ", lcs(X, Y))
