<<<<<<< HEAD
pages = {}

import NumericCalculus as NC
import NBParser
import Playground

pages['Jupyter'] = {
    'Log' : lambda : NBParser.parseNB('C:\\Users\\victo\\Desktop\\Git\\MachineLearning\\notebooks\\MNIST.ipynb'),
    'Home' : lambda: NBParser.parseNB('https://raw.githubusercontent.com/VictorHerbert/MachineLearning/master/Notebooks/Logistic_Regresion.ipynb')
=======
pages = {}

import NumericCalculus as NC
import NBParser
import Playground

pages['Jupyter'] = {
    'Log' : lambda : NBParser.parseNB('C:\\Users\\victo\\Desktop\\Git\\MachineLearning\\notebooks\\MNIST.ipynb'),
    'Home' : lambda: NBParser.parseNB('https://raw.githubusercontent.com/VictorHerbert/MachineLearning/master/Notebooks/Logistic_Regresion.ipynb')
>>>>>>> 3d62429c56aab4cc084c7a673616583298c1139f
}