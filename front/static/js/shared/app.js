(() => {
  const sidebar = document.getElementById('sidebar');
  const toggle = document.getElementById('menuToggle');
  if (toggle && sidebar) toggle.addEventListener('click', () => sidebar.classList.toggle('open'));
  document.addEventListener('click', event => {
    if (sidebar?.classList.contains('open') && !sidebar.contains(event.target) && !toggle?.contains(event.target)) sidebar.classList.remove('open');
  });
  document.querySelectorAll('form[data-loading]').forEach(form => form.addEventListener('submit', () => {
    const button = form.querySelector('button[type="submit"],button:not([type])');
    if (button && form.reportValidity()) { button.disabled = true; button.dataset.original = button.innerHTML; button.innerHTML = `<span class="spinner"></span>${form.dataset.loading}`; }
  }));
  document.querySelectorAll('.show-password').forEach(button => button.addEventListener('click', () => {
    const input = button.parentElement.querySelector('input');
    input.type = input.type === 'password' ? 'text' : 'password';
    button.innerHTML = `<i class="bi ${input.type === 'password' ? 'bi-eye' : 'bi-eye-slash'}"></i>`;
  }));
  document.querySelectorAll('.toast').forEach(toast => setTimeout(() => { toast.classList.add('toast-out'); setTimeout(() => toast.remove(), 350); }, 5500));
})();
