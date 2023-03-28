from goprocam import GoProCamera, constants
gpc = GoProCamera.GoPro()
gpc.stream("udp://127.0.0.1:10000")