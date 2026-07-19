# CPU 중심 오픈소스 VLA 실행 환경 개발

산업 현장에서 고성능 GPU 없이도 Vision Language Action 모델을 실행하고 검증할 수 있는 CPU 중심 오픈소스 실행 환경을 개발하는 프로젝트입니다.

## 현재 목표

- OpenVINO 기반 CPU 추론 환경 구성
- MuJoCo 기반 로봇 시뮬레이션 검증 환경 구성
- ONNX 및 OpenVINO 변환 파이프라인 실험
- CPU 환경에서의 추론 성능 측정

## 개발 환경

- OS: Windows 11 Home 64-bit
- Python: 3.11.9
- 가상환경: `vla`
- CPU: Intel Core Ultra X7 358H
- RAM: 약 32GB
- GPU: Intel Arc B390 GPU

## 빠른 시작

PowerShell에서 프로젝트 폴더로 이동한 뒤 가상환경을 활성화합니다.

```powershell
.\vla\Scripts\activate
```

필요한 패키지를 설치합니다.

```powershell
pip install -r requirements.txt
```

MuJoCo 시뮬레이션을 확인합니다.

```powershell
python scripts\test_mujoco.py
```

MuJoCo 장면을 이미지로 렌더링합니다.

```powershell
python scripts\render_mujoco_scene.py
```

MuJoCo 움직임을 GIF로 렌더링합니다.

```powershell
python scripts\render_mujoco_motion.py
```

MuJoCo 실시간 viewer 창을 실행합니다.

```powershell
python scripts\view_mujoco_live.py
```

OpenVINO CPU 추론을 확인합니다.

```powershell
python scripts\test_openvino.py
```

## 검증 결과

현재 로컬 노트북에서 다음 항목을 확인했습니다.

- MuJoCo 3.10.0 시뮬레이션 실행 성공
- MuJoCo 장면 이미지 및 움직임 GIF 렌더링 성공
- OpenVINO 2026.2.1 CPU 추론 실행 성공
- NumPy 2.4.6 설치 및 import 성공

## 다음 단계

1. 간단한 MuJoCo 로봇 제어 예제 추가
2. 경량 모델을 OpenVINO로 실행하는 벤치마크 추가
3. 자연어 명령을 로봇 행동으로 연결하는 최소 VLA 유사 파이프라인 구현
