document.addEventListener('DOMContentLoaded', () => {
  const fileInput = document.getElementById('file');
  const previewImg = document.getElementById('preview');
  const previewContainer = document.querySelector('.preview-container');
  const title = document.querySelector('.uploader_title');
  const ratingSpan = document.querySelector('.rating');
  const form = document.querySelector('.uploader_form');

  fileInput.addEventListener('change', () => {
    const file = fileInput.files[0];
    if (!file) return resetPreview();
    if (!file.type.startsWith('image/')) {
      alert('Please choose a valid image file.');
      return resetPreview();
    }

    const reader = new FileReader();
    reader.onload = e => {
      previewImg.src = e.target.result;
      title.style.display = 'none';
      previewContainer.classList.remove('empty-state');
      previewContainer.classList.add('has-image');
    };
    reader.readAsDataURL(file);
  });

  form.addEventListener('submit', async e => {
    e.preventDefault();
    const file = fileInput.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('photo', file);

    try {
      const response = await fetch('/upload', { method: 'POST', body: formData });
      if (!response.ok) throw new Error('Request failed');

      const data = await response.json();
      ratingSpan.textContent = Number(data.rating).toFixed(2);
    } catch (err) {
      console.error(err);
      alert('Unable to rate the photo.');
    }
  });

  function resetPreview() {
    previewImg.src = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGNgYAQAAgAB9HF5pQAAAABJRU5ErkJggg==';
    title.style.display = 'block';
    previewContainer.classList.remove('has-image');
    previewContainer.classList.add('empty-state');
    ratingSpan.textContent = 'Unknown';
  }
});
