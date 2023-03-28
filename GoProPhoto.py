from goprocam import GoProCamera, constants

gopro = GoProCamera.GoPro()


def take_photo_transfer_delete():
    gopro.take_photo(timer=20)
    gopro.downloadLastMedia(custom_filename="asd.jpg")
                            
def timelapse(interval):
    while True:
        gopro.downloadLastMedia(gopro.take_photo(timer=interval))
        
timelapse(3)
gopro.listMedia(True)