#ffplay -fflags nobuffer -flags low_delay -framedrop -strict experimental   udp://127.0.0.1:5555

# ffplay -probesize 128 -sync video -an -sn -fast -infbuf -f mpegts -i udp://127.1.1.0:10000