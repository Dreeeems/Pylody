


document.querySelectorAll('.play-btn').forEach(button => {
    button.addEventListener('click', function() {
        const audioPlayer = document.getElementById('audio-player');
        const musicPlayer = document.getElementById('music-player');

        audioPlayer.src = this.getAttribute('data-src'); 
        musicPlayer.classList.remove('hidden'); 
        audioPlayer.play();
    });
});

