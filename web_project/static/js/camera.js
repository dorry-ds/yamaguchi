function startDetection() {
    const videoContainer = document.getElementById('video-container');
    videoContainer.innerHTML = '<img src="/detect" alt="Detection Video Stream">';
}

function cameraoff(){
    fetch('/cameraoff', {
        method: 'POST'
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        // 可以在这里处理成功的响应
        console.log('Camera turned off successfully');
    })
    .catch(error => {
        console.error('There was a problem with the cameraoff request:', error);
    });
}