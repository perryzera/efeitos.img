const fileInput = document.getElementById('fileInput');
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
let img = new Image();
let originalImage = null;
let rotationAngle = 0;  // Var -> Ângulo da Rotação

// Evento para carregar a imagem ao selecionar um arquivo
fileInput.addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            img.src = e.target.result;
            img.onload = function() {
                const aspectRatio = img.width / img.height;
                const maxWidth = window.innerWidth * 0.8;
                const maxHeight = window.innerHeight * 0.6;

                let newWidth = maxWidth;
                let newHeight = maxWidth / aspectRatio;

                if (newHeight > maxHeight) {
                    newHeight = maxHeight;
                    newWidth = maxHeight * aspectRatio;
                }

                canvas.width = newWidth;
                canvas.height = newHeight;
                ctx.drawImage(img, 0, 0, newWidth, newHeight);
                canvas.style.display = 'block';
                originalImage = ctx.getImageData(0, 0, canvas.width, canvas.height);
            };
        };
        reader.readAsDataURL(file);
    }
});

// Função -> Blur
function applyBlur() {
    resetImage();
    ctx.filter = 'blur(5px)';
    ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
}

// Funçãoo -> Sharpening
function applySharpen() {
    resetImage();
    const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    const data = imageData.data;
    const kernel = [
        0, -1, 0,
        -1, 5, -1,
        0, -1, 0
    ];

    const w = canvas.width;
    const h = canvas.height;
    const copy = new Uint8ClampedArray(data);

    for (let y = 1; y < h - 1; y++) {
        for (let x = 1; x < w - 1; x++) {
            let r = 0, g = 0, b = 0;
            let i = (y * w + x) * 4;

            for (let ky = -1; ky <= 1; ky++) {
                for (let kx = -1; kx <= 1; kx++) {
                    let ni = ((y + ky) * w + (x + kx)) * 4;
                    let k = kernel[(ky + 1) * 3 + (kx + 1)];
                    r += copy[ni] * k;
                    g += copy[ni + 1] * k;
                    b += copy[ni + 2] * k;
                }
            }
            data[i] = Math.min(255, Math.max(0, r));
            data[i + 1] = Math.min(255, Math.max(0, g));
            data[i + 2] = Math.min(255, Math.max(0, b));
        }
    }
    ctx.putImageData(imageData, 0, 0);
}

// Função -> Rotação 45°
function rotateImage() {
    rotationAngle += 45; 
    resetImage();
    const tempCanvas = document.createElement('canvas');
    const tempCtx = tempCanvas.getContext('2d');

    // Calcula o tamanho necessário para o canvas rotacionado
    const angleInRadians = rotationAngle * Math.PI / 180;
    const cos = Math.abs(Math.cos(angleInRadians));
    const sin = Math.abs(Math.sin(angleInRadians));

    const newWidth = canvas.width * cos + canvas.height * sin;
    const newHeight = canvas.width * sin + canvas.height * cos;

    tempCanvas.width = newWidth;
    tempCanvas.height = newHeight;

    // Centraliza a imagem, no Canvas
    tempCtx.translate(newWidth / 2, newHeight / 2);
    tempCtx.rotate(angleInRadians);
    tempCtx.drawImage(canvas, -canvas.width / 2, -canvas.height / 2);

    canvas.width = newWidth;
    canvas.height = newHeight;
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(tempCanvas, 0, 0);
}

// Função -> Resetar imagem
function resetImage() {
    if (originalImage) {
        canvas.width = originalImage.width;
        canvas.height = originalImage.height;
        ctx.putImageData(originalImage, 0, 0);
    }
}
