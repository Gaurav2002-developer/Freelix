const video = document.getElementById("movie");
const playPauseBtn = document.getElementById("playPause");
const progressBar = document.getElementById("progressBar");
const volume = document.getElementById("volume");
const fullscreenBtn = document.getElementById("fullscreen");

// Play / Pause
playPauseBtn.addEventListener("click", () => {
  if (video.paused) {
    video.play();
    playPauseBtn.textContent = "⏸️";
  } else {
    video.pause();
    playPauseBtn.textContent = "▶️";
  }
});

// Update progress bar
video.addEventListener("timeupdate", () => {
  progressBar.value = (video.currentTime / video.duration) * 100;
});

// Seek video
progressBar.addEventListener("input", () => {
  video.currentTime = (progressBar.value / 100) * video.duration;
});

// Volume control
volume.addEventListener("input", () => {
  video.volume = volume.value;
});

// Fullscreen toggle
fullscreenBtn.addEventListener("click", () => {
  if (!document.fullscreenElement) {
    video.requestFullscreen();
  } else {
    document.exitFullscreen();
  }
});
