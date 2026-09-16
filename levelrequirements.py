scaler = 1.5

levelreqs = {
    "1":200,
    "2":200*scaler,
    "3":200*(scaler**2),
    "4":200*(scaler**3),
    "5":200*(scaler**4),
    "6":200*(scaler**5),
    "7":200*(scaler**6),
    "8":200*(scaler**7),
    "9":200*(scaler**8),
    "10":200*(scaler**9)
}

def returnlevels():
    return levelreqs