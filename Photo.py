from goprocam import GoProCamera, constants
gopro = GoProCamera.GoPro(constants.gpcontrol)
gopro.take_photo()
gopro.downloadLastMedia("pic.JPG")