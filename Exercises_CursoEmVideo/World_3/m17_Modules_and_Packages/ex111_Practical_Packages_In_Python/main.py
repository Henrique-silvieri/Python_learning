# Create a package called utilitiesCeV that has two internal modules called currency and data. Transfer all the functions 
# developed in challenges 107, 108, and 109 to the first package and keep everything working.

from utilitiesCeV.currency import currency

value = float(input('Digite um valor em R$'))
currency.summary(value, 80, 25)