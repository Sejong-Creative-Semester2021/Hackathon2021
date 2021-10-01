const videoOutput = document.getElementById('video-output');

let mediaStream = null;
let mediaRecorder = null;
let recordedMediaURL = null;

// 유저의 카메라로 부터 입력을 사용할 수 있도록 요청
navigator.mediaDevices
  .getUserMedia({ video: true })
  .then(function (newMediaStream) {
    mediaStream = newMediaStream;

    // 카메라의 입력을 실시간으로 비디오 태그에서 확인
    videoOutput.srcObject = mediaStream;
    videoOutput.onloadedmetadata = function (e) {
      videoOutput.play();
    };
  });

// let recordedChunks = [];
// // 1.MediaStream을 매개변수로 MediaRecorder 생성자를 호출
// mediaRecorder = new MediaRecorder(mediaStream, {
// mimeType: 'video/webm; codecs=vp9',
// });

// // 2. 전달받는 데이터를 처리하는 이벤트 핸들러 등록
// mediaRecorder.ondataavailable = function (event) {
// if (event.data && event.data.size > 0) {
//     console.log('ondataavailable');
//     recordedChunks.push(event.data);
// }
// };