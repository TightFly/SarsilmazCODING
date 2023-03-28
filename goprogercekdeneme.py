from goprocam import GoProCamera, constants
gpc= GoProCamera.GoPro()
gpc.KeepAlive()
# ffplay -probesize 128 -sync video -an -sn -fast -infbuf -f mpegts -i udp://127.1.1.0:10000

"""

ffplay udp://192.168.1.20:8080 -vf "transpose=2,transpose=2" -fflags nobuffer -flags low_delay -framedrop

commands = (
    ffplay 
    .output('udp://10.42.0.1:8080')
    .fflags(nobuffer)
    .flags(low_delay)
    .vf
)

command = "ffmpeg -i '{video}' -ac 1  -f flac -vn '{output}'"

-vf "transpose=2,transpose=2" 
command= "ffplay udp://192.168.1.20:8080 -fflags nobuffer -flags low_delay -framedrop"
"""