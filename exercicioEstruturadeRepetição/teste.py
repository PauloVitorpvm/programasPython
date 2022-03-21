
A = 80000
B = 200000
taxaA = 0.03
taxaB = 0.015

anos = 0
while A < B:
    A = A + (A * taxaA)
    B = B + (B * taxaB)
    anos = anos + 1

print ("SerÃ£o necessÃ¡rios " + str(anos) + " anos para que a populaÃ§Ã£o do paÃ­s A ultrapasse ou iguale a populaÃ§Ã£o do paÃ­s B")