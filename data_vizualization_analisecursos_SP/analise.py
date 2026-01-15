import pandas as pd

df = pd.read_csv('base_cursos.csv')
print("Colunas disponíveis:", df.columns)

# Quantidade de faculdades distintas
qtd_faculdades = df['universidade_nome'].nunique()
print(f"Quantidade de faculdades distintas: {qtd_faculdades}")

# Quantidade de cursos distintos
qtd_cursos = df['curso_nome'].nunique()
print(f"Quantidade de cursos distintos: {qtd_cursos}")

# Cursos com maior e menor mensalidade
try:
    curso_mais_caro = df.loc[df['mensalidade'].idxmax()]    
    curso_mais_barato = df.loc[df['mensalidade'].idxmin()]  
    print(f"Curso mais caro: {curso_mais_caro['curso_nome']} - Mensalidade: {curso_mais_caro['mensalidade']}")
    print(f"Curso mais barato: {curso_mais_barato['curso_nome']} - Mensalidade: {curso_mais_barato['mensalidade']}")
except Exception as e:
    print("Erro nas mensalidades:", e)

# Cursos com maior e menor nota integral ampla
try:
    curso_melhor_nota_integral_ampla = df.loc[df['nota_integral_ampla'].idxmax()]
    curso_pior_nota_integral_ampla = df.loc[df['nota_integral_ampla'].idxmin()]
    print(f"Curso com melhor nota integral ampla: {curso_melhor_nota_integral_ampla['curso_nome']} - Nota: {curso_melhor_nota_integral_ampla['nota_integral_ampla']}")
    print(f"Curso com pior nota integral ampla: {curso_pior_nota_integral_ampla['curso_nome']} - Nota: {curso_pior_nota_integral_ampla['nota_integral_ampla']}")
except Exception as e:
    print("Erro nas notas integrais amplas:", e)


print("Colunas disponíveis:", df.columns.tolist())
