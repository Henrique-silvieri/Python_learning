# Within the utilidadesCeV package we created in challenge 111, the data module has a function called readMoney() that is capable 
# of functioning like the input() function, but with data validation to accept only values that are monetary.

from utilitiesCeV.currency import currency
from utilitiesCeV.data import data

value = data.readMoney('Digite um valor em R$')
currency.summary(value, 80, 25)