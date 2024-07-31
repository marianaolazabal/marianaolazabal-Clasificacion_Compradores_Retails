

from test_import import test
from test_import import test2
from test_import import plots
import pandas as p 
test.resta(3,1)

#plots.grafico()


test.suma(4,3)

test.division(3,6)

test.multi(7)



test2.multi(7)


def restaMulti(a,b):
    resultadResta=test.resta(a,b)
    resultadoMulti = test2.multi(b)
    resultadoTotal = resultadoMulti - resultadResta
    return resultadoTotal

restaMulti(4,2)

