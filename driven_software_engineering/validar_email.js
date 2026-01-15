// Gerado com o prompt: "Crie uma função que valida se um e-mail é válido usando regex"
function validarEmail(email) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}

module.exports = validarEmail;
