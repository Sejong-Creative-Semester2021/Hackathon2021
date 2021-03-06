window.onload = () => {
    const startBtn = document.getElementById('startBtn');
    const stopBtn = document.getElementById('stopBtn');
    const download = document.getElementById('download');

    let blobs;
    let blob; // 데이터
    let rec; // 스트림을 기반으로 동작하는 mediarecorder 객체
    let stream; // 통합
    let voiceStream; // 오디오스트림
    let desktopStream; // 비디오스트림
    let recordedMediaURL = null;

    const mergeAudioStreams = (desktopStream, voiceStream) => { // 비디오, 오디오스트림 연결
      const context = new AudioContext();
      const destination = context.createMediaStreamDestination();
      let hasDesktop = false;
      let hasVoice = false;
      if (desktopStream && desktopStream.getAudioTracks().length > 0) {
        const source1 = context.createMediaStreamSource(desktopStream);
        const desktopGain = context.createGain();
        desktopGain.gain.value = 0.7;
        source1.connect(desktopGain).connect(destination);
        hasDesktop = true;
      }

      if (voiceStream && voiceStream.getAudioTracks().length > 0) {
        const source2 = context.createMediaStreamSource(voiceStream);
        const voiceGain = context.createGain();
        voiceGain.gain.value = 0.7;
        source2.connect(voiceGain).connect(destination);
        hasVoice = true;
      }

      return (hasDesktop || hasVoice) ? destination.stream.getAudioTracks() : [];
    };

    startBtn.onclick = async () => { // 녹화 시작 버튼을 누른 경우
      desktopStream = await navigator.mediaDevices.getDisplayMedia({ video: { width: 640 , height: 480 }, audio: true }); // 비디오스트림 생성
      voiceStream = await navigator.mediaDevices.getUserMedia({ video: false, audio: true }); // 오디오스트림 생성

      const tracks = [
        ...desktopStream.getVideoTracks(),
        ...mergeAudioStreams(desktopStream, voiceStream)
      ];

      stream = new MediaStream(tracks);

      blobs = [];

      rec = new MediaRecorder(stream, {mimeType: 'video/webm; codecs=vp9,opus'}); // mediaRecorder객체 생성
      rec.ondataavailable = (e) => blobs.push(e.data);
      rec.onstop = async () => {
        // 다운로드
        // blob = new Blob(blobs, {type: 'video/webm'});
        // let url = window.URL.createObjectURL(blob);
        // download.href = url;
        // download.download = 'test.webm';
        // download.style.display = 'block';
        blob = new Blob(blobs, {type: 'video/webm'})
        const link = document.createElement("a");
        document.body.appendChild(link);
        // 녹화된 영상의 URL을 href 속성으로 설정
        link.href = window.URL.createObjectURL(blob);
        // 저장할 파일명 설정
        link.download = "video.avi";
        link.click();
        document.body.removeChild(link);
      };
      startBtn.disabled = true; // 시작 버튼 비활성화
      stopBtn.disabled = false; // 종료 버튼 활성화
      rec.start(); // 녹화 시작
    };


    stopBtn.onclick = () => { // 종료 버튼을 누른 경우
      // 버튼 비활성화
      startBtn.disabled = true;
      stopBtn.disabled = true;

      rec.stop(); // 화면녹화 종료 및 녹화된 영상 다운로드

      desktopStream.getTracks().forEach(s=>s.stop())
      voiceStream.getTracks().forEach(s=>s.stop())
      desktopStream = null;
      voiceStream = null;

      startBtn.disabled = false; // 시작 버튼 활성화
    };
  };


//   downloadBtn.addEventListener('click', function () {
//     blobs.push(e.data)
//     blob = new Blob(blobs, {type: 'video/webm'});
//     url = window.URL.createObjectURL(blob);
//     recordedMediaURL = url
//     console.log('recordedMediaURL : ', recordedMediaURL);
//     if (recordedMediaURL) {
//       const link = document.createElement('a');
//       document.body.appendChild(link);
//       link.href = recordedMediaURL;
//       link.download = 'video.webm';
//       link.click();
//       document.body.removeChild(link);
//     }
//   });


