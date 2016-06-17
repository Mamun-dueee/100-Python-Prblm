dest = {61:"Brasilia", 71:"Salvador", 11:"Sao Paulo",
        21:"Rio de Janeiro",
        32:"Juiz de Fora", 19:"Campinas", 27:"Victoria",
        31:"Belo Horizonte"
        }
key = [61, 71, 11, 21, 32, 19, 27, 31]
n = int(input())
print(dest[n] if n in key else "DDD nao cadastrado")
