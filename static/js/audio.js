document.addEventListener("DOMContentLoaded", () => {
    const audioPlayer = document.getElementById("audio-player");
    const musicPlayer = document.getElementById("music-player");
    const playPauseBtn = document.getElementById("play-pause-btn");
    const prevBtn = document.getElementById("prev-btn");
    const nextBtn = document.getElementById("next-btn");
    const progressBar = document.getElementById("progress-bar");
    const playerCover = document.getElementById("player-cover");
    const playerTitle = document.getElementById("player-title");
    const playerArtist = document.getElementById("player-artist");

    let currentTrackIndex = 0;
    let tracks = [];
    console.log(tracks)

    const playButtons = document.querySelectorAll('.play-btn');

    playButtons.forEach((button, index) => {
        
        tracks.push({
            src: button.getAttribute('data-src'),
            title: button.getAttribute('data-title'),
            artist: button.getAttribute('data-artist'),
            cover: button.getAttribute('data-cover')
        });console.log(currentTrackIndex)

        button.addEventListener('click', () => {
            if(currentTrackIndex !== 0){
            currentTrackIndex = index;
            loadTrack(currentTrackIndex);
            musicPlayer.classList.remove("hidden");
            audioPlayer.play();
        }
        });
    });


    function loadTrack(index) {
        let track = tracks[index];
        audioPlayer.src = track.src;
        playerTitle.innerText = track.title;
        playerArtist.innerText = track.artist;
        playerCover.src = track.cover;
        playPauseBtn.innerText = "⏸"; 
    }


    playPauseBtn.addEventListener("click", () => {
        if (audioPlayer.paused) {
            audioPlayer.play();
            playPauseBtn.innerText = "⏸";
        } else {
            audioPlayer.pause();
            playPauseBtn.innerText = "▶";
        }
    });

    nextBtn.addEventListener("click", () => {
        currentTrackIndex = (currentTrackIndex + 1) % tracks.length;
        loadTrack(currentTrackIndex);
        audioPlayer.play();
    });

    prevBtn.addEventListener("click", () => {
        currentTrackIndex = (currentTrackIndex - 1 + tracks.length) % tracks.length;
        loadTrack(currentTrackIndex);
        audioPlayer.play();
    });

    audioPlayer.addEventListener("timeupdate", () => {
        if (audioPlayer.duration) {
            progressBar.value = (audioPlayer.currentTime / audioPlayer.duration) * 100;
        }
    });

    progressBar.addEventListener("input", () => {
        if (audioPlayer.duration) {
            audioPlayer.currentTime = (progressBar.value / 100) * audioPlayer.duration;
        }
    });

    if (tracks.length > 0) {
        loadTrack(currentTrackIndex);
    }
});
