#leia o valor em metros e converta para centimetros e milímetros
n = float(input('Digite a distância em metros: '))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000
print(f'A medida de {n:.0f}m corresponde a:\n{km} Km\n{hm} hm\n{dam} dam\n{dm:.0f} dm\n{cm:.0f} cm\n{mm:.0f} mm')
