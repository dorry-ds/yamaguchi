const video = document.getElementById('video');

// 检查浏览器是否支持getUserMedia API
if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    // 请求访问用户的摄像头
    navigator.mediaDevices.getUserMedia({ video: true })
    .then(function(stream) {
        // 将视频流设置为视频元素的源
        video.srcObject = stream;
        video.play();
    })
    .catch(function(error) {
        console.error("摄像头访问被拒绝或出现错误:", error);
    });
} else {
    alert("您的浏览器不支持getUserMedia API");
}

