
document.getElementById('weatherForm').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent form submission

    // Show the loader
    document.getElementById('loading').style.display = 'block';

    // Hide the weather content initially (it will be shown after data loads)
    document.getElementById('weatherContent').style.display = 'none';

})
