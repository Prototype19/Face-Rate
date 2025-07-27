document.addEventListener('DOMContentLoaded', () => {
  const fileInput = document.getElementById('file');
  const previewImg = document.getElementById('preview');
  const previewContainer = document.querySelector('.preview-container');
  const title = document.querySelector('.uploader_title');

  fileInput.addEventListener('change', handleFileChange);

  function handleFileChange() {
    const file = this.files[0];

    if (!file) {
      // No file selected - reset to original state
      resetPreview();
      return;
    }

    if (!file.type.startsWith('image/')) {
      alert('Please choose a valid image file.');
      resetPreview();
      return;
    }

    const reader = new FileReader();

    reader.onload = e => {
      previewImg.src = e.target.result;
      title.style.display = 'none';
      
      // Add classadd('has-image');
      previewContainer.classList.remove('empty-state');
    };

    reader.onerror = () => {
      console.error('File could not be read');
      alert('Failed to preview image. Try another file.');
      resetPreview();
    };

    reader.readAsDataURL(file);
  }

  function resetPreview() {
    previewImg.src = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGNgYAQAAgAB9HF5pQAAAABJRU5ErkJggg==';
    title.style.display = 'block';
    
    // Remove upload state classes and add empty state
    previewContainer.classList.remove('has-image');
    previewContainer.classList.add('empty-state');
  }
});
