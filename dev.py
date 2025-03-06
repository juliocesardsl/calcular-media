aluno = input('Nome do aluno: ')

qtd_notas = int(input('Quantas notas você quer calcular? '))
notas = []

for i in range(qtd_notas):
    nota = float(input('Nota: '))
    notas.append(nota)

media = sum(notas) / qtd_notas

if media >= 5:
    print(f'O aluno {aluno} está aprovado na disciplina com a média {media:.2f}')
else:
    print(f'O aluno {aluno} está reprovado na disciplina com a média {media:.2f}')