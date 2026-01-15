# IA na prática: Acelerando o desenvolvimento e garantindo a qualidade com um fluxo de trabalho automatizado por IA

## 📌 Análise do Problema
A empresa fictícia **TechGestão**, responsável por uma ferramenta de colaboração online, enfrenta um dilema entre **velocidade e qualidade** no desenvolvimento de software.  
Nos últimos meses, a pressão para entregar novas funcionalidades aumentou devido a campanhas de marketing e demandas de clientes. Porém, ao acelerar os ciclos de entrega, a equipe reduziu a cobertura de testes e passou a introduzir mais bugs em produção.  

O cenário atual mostra gargalos claros:
- **Desenvolvimento repetitivo**: os desenvolvedores gastam tempo escrevendo código básico e redundante.  
- **Baixa cobertura de testes**: escrever testes é visto como tarefa demorada e pouco gratificante.  
- **Ciclo de feedback lento**: erros só são descobertos em QA manual ou pelos usuários em produção.  
- **Inconsistência no código**: diferentes desenvolvedores resolvem problemas de formas distintas, aumentando a complexidade da base.  

Esse contexto evidencia a necessidade de um novo fluxo de trabalho que equilibre velocidade e qualidade.

---

## 💡 Papel da IA no Ciclo de Desenvolvimento
A **Inteligência Artificial** tem se tornado uma aliada estratégica no desenvolvimento de software moderno. Ferramentas como o **GitHub Copilot** e o **GitHub Actions** atuam em pontos críticos do ciclo de desenvolvimento:

- **GitHub Copilot**: acelera a criação de funções e componentes, reduzindo o tempo gasto em tarefas repetitivas e permitindo que os desenvolvedores foquem em lógica de negócio. Também sugere testes unitários, aumentando a cobertura e garantindo que funcionalidades sejam validadas desde o início.  
- **GitHub Actions**: automatiza a execução dos testes a cada push, fornecendo feedback imediato sobre a qualidade do código. Isso elimina o ciclo lento de QA manual e garante consistência no processo de validação.  

Em conjunto, essas ferramentas permitem que equipes juniores e plenas mantenham **produtividade alta sem sacrificar qualidade**, resolvendo o dilema central do desafio.

---

## 📚 Caso Real de Referência
Um exemplo concreto e muito relevante de aplicação do **GitHub Copilot** no mercado é o caso da **HP (Hewlett-Packard)**.  
Segundo a Microsoft, a HP adotou o Copilot como parte de sua estratégia de modernização do desenvolvimento de software, com o objetivo de **aumentar a velocidade de entrega de novas funcionalidades** e **reduzir o tempo gasto em tarefas repetitivas**.  

### 🚀 Impacto na HP
- **Produtividade**: os desenvolvedores passaram a escrever código mais rápido, já que o Copilot sugere trechos prontos e reduz o esforço em tarefas repetitivas.  
- **Qualidade**: ao gerar testes automatizados, o Copilot ajudou a aumentar a cobertura de testes e reduzir bugs em produção.  
- **Inovação**: com menos tempo gasto em código básico, os times puderam focar em funcionalidades estratégicas e inovadoras.  
- **Velocidade de entrega**: a integração do Copilot ao fluxo de trabalho permitiu que novas funcionalidades chegassem ao mercado em menos tempo, acompanhando a pressão competitiva.  

### 🌍 Reflexão mais ampla
O caso da HP mostra que o uso de IA no desenvolvimento não é apenas uma tendência acadêmica ou experimental, mas uma **realidade em grandes empresas globais**.  
Organizações que precisam equilibrar velocidade e qualidade encontram no Copilot e no GitHub Actions ferramentas poderosas para:
- Automatizar tarefas repetitivas.  
- Garantir consistência no código.  
- Reduzir gargalos de QA manual.  
- Aumentar a confiança na entrega contínua.  

Além da HP, outras empresas de tecnologia e até startups têm relatado ganhos semelhantes. Times de desenvolvimento open source, por exemplo, usam **GitHub Actions** para rodar testes automaticamente em cada pull request, garantindo que contribuições externas não quebrem o projeto. Isso mostra que a combinação de **Copilot + Actions** é aplicável tanto em grandes corporações quanto em equipes menores.

### 🔗 Fonte oficial
Você pode conferir o artigo completo da Microsoft sobre a adoção do Copilot pela HP aqui:  
[HP adota GitHub Copilot e aumenta a inovação e a velocidade do software](https://news.microsoft.com/pt-br/hp-adota-github-copilot-e-aumenta-a-inovacao-e-a-velocidade-do-software/)

---

## 🛠️ Parte Prática

### Função principal

Arquivo: `validarEmail.js`  
Prompt utilizado:

```js
// Prompt: "Crie uma função em Node.js chamada validarEmail que receba uma string representando um e-mail.
// A função deve retornar true se o e-mail for válido e false caso contrário.
// Use regex para validar o formato do e-mail e considere casos comuns de erro."
```

Testes automatizados
Arquivo: validarEmail.test.js  
Prompt utilizado:

```js
// Prompt: "Crie testes unitários usando Jest para a função validarEmail.
// Os testes devem cobrir e-mails válidos, inválidos, com subdomínios e casos com caracteres especiais."
```

Workflow de CI/CD
Arquivo: .github/workflows/ci.yml  
Prompt utilizado:

```yaml
# Prompt: "Crie um workflow GitHub Actions que rode os testes automatizados com Jest em cada push ou pull request.
// Configure Node.js versão 18, instale dependências e execute os testes."
```

⚙️Pipeline Automatizado
O GitHub Actions foi configurado para:

Instalar dependências.
Rodar os testes unitários.
Exibir o status do build no repositório.

📊 Status do Build
https://github.com/ddqueiro/gestao_tecnologia_da_informacao/actions/workflows/ci.yml/badge.svg

✅ Conclusão
A análise do problema mostra que a equipe fictícia sofre com baixa cobertura de testes e lentidão no ciclo de feedback.
A discussão conceitual evidencia como a IA, por meio do Copilot e do Actions, pode transformar esse cenário.
E o caso real da HP comprova que essa abordagem já está trazendo resultados positivos em empresas globais.

Este trabalho demonstra, na prática, como a IA pode acelerar o desenvolvimento e garantir qualidade em fluxos de trabalho modernos de engenharia de software.
