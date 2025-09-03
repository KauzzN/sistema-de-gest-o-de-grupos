const toggleBtn = document.getElementById('toggle-btn');
const backBtn = document.getElementById('back-btn');
const signupRight = document.querySelector('.signup-right');
const signupText = document.getElementById('signup-text');
const container = document.querySelector('.login-box');

toggleBtn.addEventListener('click', () => {
  // Esconde a parte do login e mostra a parte do registro
  container.classList.add('hide-signin');
  signupRight.classList.add('visible');
  signupText.textContent = 'Faça o Login para ter acesso a sua Gestão';
});

backBtn.addEventListener('click', () => {
  // Volta para a tela inicial, mostrando login e ocultando o registro
  container.classList.remove('hide-signin');
  signupRight.classList.remove('visible');
  signupText.textContent = 'Cadastre-se para acessar todos os recursos de Gestão';
});
