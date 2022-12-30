def convertTemperature(celsius):
    k=celsius+273.15
    f=celsius*1.80+32.00
    return [k,f]


print(f'outside: function.py __name__: {__name__}')

if __name__=="__main__":
   k,f=convertTemperature(100)
   print(f"inside: k={k}, f={f}")
