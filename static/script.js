document.getElementById('image').addEventListener('change', function (event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const preview = document.getElementById('preview');
            preview.src = e.target.result;
            preview.style.display = 'block';
        }
        reader.readAsDataURL(file);
    }
});

// document.addEventListener("DOMContentLoaded", function () {
//     const images = document.querySelectorAll('.slider img');
//     let index = 0;

//     function showImage() {
//         images.forEach(img => img.classList.remove('active'));
//         images[index].classList.add('active');
//         index = (index + 1) % images.length;
//     }

//     setInterval(showImage, 2000); // Change slide every 2 seconds
// });

