#011

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

print(f'Sua parede tem a dimensão de {larg} x {alt} e sua área é de {larg * alt}m\nPara pintar essa parede, você precisará de {(larg * alt) / 2:.1f}l de tinta.')