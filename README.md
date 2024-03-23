# video_to_cartoon
The program has a cartoon effect on the original mp4 image using opencv.

해당 프로그램은 opencv를 활용하여 만화적인 효과를 주는 프로그램이다.

사용한 기술 : 
1. 엣지 감지를 위한 Laplacian 기법
2. 이미지 블러링을 통한 노이즈 제거
3. 이진화 + 절댓값 취하기

위의 기술들을 사용한 이유 :
엣지 감지 기술에는 1. Canny 2. Sobel 3. Laplacian 들이 있다.
3가지를 모두 테스트해본 결과 
1. Canny는 노이즈에 강하지만 엣지라인을 찾는 과정에서 선명하게 찾지 못한다
2. Sobel은 노이즈에 약하기 때문에 지저분하게 엣지라인을 찾게된다.
3. Laplacian은 노이즈에 어느정도 강하고 엣지라인도 부드럽게 찾는것을 확인할 수 있었다.

만화적인 느낌을 잘 표현할 수 있는 영상은 다음과 같다.
1. 배경이 단순하다
2. 윤곽선이 잘 보인다
3. 카메라의 움직임이 적다

<원본 영상 이미지>

![readme01](https://github.com/Hongyooungi/video_to_cartoon/assets/127743990/c0dac823-7b44-4391-921a-bc0d73f985e9)

<수정된 이미지>

위의 이미지에 Laplacian keysize = 5, MedianBlur 7 , 이진화 65, 255 로 변수를 설정했다.

![readme02](https://github.com/Hongyooungi/video_to_cartoon/assets/127743990/d418250e-3725-494c-8a54-b1da9c83b6b8)


<2차 수정된 이미지>

위의 이미지에서 노이즈가 발생하는 것 같아 MedianBlur 9, 이진화 115, 255 로 변수를 설정했다.

![readme03](https://github.com/Hongyooungi/video_to_cartoon/assets/127743990/ac8bf8ce-4f55-477a-baf6-dacc306e4524)


<알고리즘의 한계>

- 해당 알고리즘은 변수가 지정된 상태로 영상에 들어간다.
- 따라서, 고정된 위치에서는 앞에서 했던 것처럼 변수를 바꿔가며 수정을 할 수가 있다.
- 하지만, 카메라의 위치가 고정이 되어 있지 않고, 편집기술이 많이 들어간 영상에서는 만화적인 효과가 안정적이지 못하다.
- 예시로 드라마 영상에서의 만화적인 효과를 보도록 하자

![GIFMaker_me](https://github.com/Hongyooungi/video_to_cartoon/assets/127743990/151f4e9c-d46c-4119-be59-1c4c2e997d1c)



- 위의 영상에서 볼 수 있듯이 카메라에 따라 카툰화가 잘되는 지점이 있고, 잘 안되는 지점이 있다.
- 이를통해 실시간으로 카툰화를 해줄 수 있는 알고리즘의 필요성을 느꼈다.
