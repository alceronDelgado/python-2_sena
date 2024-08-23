import pandas as pd

sdata1 = {
    "Valle grande": 1900,
    "Buga": 7003,
    "Santa Fe": 5257,
    "Puerto Arandano": 4829,
}
sdata2 = {
    "Valle grande": 12500,
    "Floralia": 400,
    "Santa Fe": 983,
    "Puerto Arandano": 3400,
}


index = ["Puerto Arandano", "Valle grande", "Buga", "Santa Fe"]
index2 = ["Puerto Arandano", "Floralia grande", "Valle grande", "Santa Fe"]



objeto1 = pd.Series(sdata1, index = index)
objeto2 = pd.Series(sdata2, index = index2)

print(objeto1)
print("\n")
print(objeto2)