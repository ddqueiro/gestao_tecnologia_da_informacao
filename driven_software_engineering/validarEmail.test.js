// Gerado com o prompt: "Crie testes unitários para a função validarEmail usando Jest"
const validarEmail = require('./validar_email');

test('retorna true para e-mail válido simples', () => {
  expect(validarEmail('teste@exemplo.com')).toBe(true);
});

test('retorna false para e-mail sem @', () => {
  expect(validarEmail('testeexemplo.com')).toBe(false);
});

test('retorna false para e-mail sem domínio', () => {
  expect(validarEmail('teste@')).toBe(false);
});

test('retorna true para e-mail com subdomínio', () => {
  expect(validarEmail('usuario@mail.exemplo.com')).toBe(true);
});
