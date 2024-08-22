metros = input(int("Insira um valor em metros para ser convertido em centímetros e milímetros: "))
cent = metros / 100
mili = cent / 100
k = metros / 1000
input(str(f"O valor de {metros:.2f} em centímetros é: {cent:.2f}, e em milímetros é: {mili:.2f}"))
