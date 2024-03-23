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
