import cv2
import numpy as np

def cartoonize_video(input_video):
    # 비디오 파일 열기
    cap = cv2.VideoCapture(input_video)
    
    # 비디오 프레임의 너비와 높이 가져오기
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
            
        # 카툰 효과 적용
        cartoon = apply_cartoon_effect(frame)
        
        
        # 비디오 출력
        cv2.imshow('Cartoonized Video with Line Art', cartoon)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()


def apply_cartoon_effect(frame):
    # 색상 이미지를 회색조 이미지로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 엣지 감지
    edges = cv2.Laplacian(gray, cv2.CV_8U, ksize=5)
    #edges = cv2.Canny(blurred, threshold1=10, threshold2=50)
        
    # 이미지 블러링을 통해 부드럽게 만들기
    gray = cv2.medianBlur(gray, 9)
    #blurred = cv2.GaussianBlur(gray, (3, 3), 0)
        
    weights = np.array([[1, 1, 1],
                        [1, 10, 1],
                        [1, 1, 1]])
    weights_sum = np.sum(weights)
    weighted_laplacian = cv2.filter2D(edges, -1, weights / weights_sum)
    
    # 절대값 취하기
    edges = np.abs(weighted_laplacian)
    
    # 이진화
    ret, mask = cv2.threshold(edges, 115, 255, cv2.THRESH_BINARY_INV)
    
    # 이미지에 필터 적용
    filtered = cv2.bilateralFilter(frame, 9, 300, 300)
    
    # 마스크와 필터된 이미지 조합
    cartoon = cv2.bitwise_and(filtered, filtered, mask=mask)
    
    return cartoon

# 예제 실행
input_video = 'simple_background01.mp4'
cartoonize_video(input_video)
