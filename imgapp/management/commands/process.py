import cv2
import numpy as mp
import time

from django.core.management.base import BaseCommand
from imgapp.models import UnprocessedImg, ProcessedImg


class Command(BaseCommand):
    help = "Start polling for green screen processing"

    def process_image(self, path):
        imgBGR = cv2.imread(path)
        imgYCC = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2YCR_CB)
        # TODO: convert image to YCbCr
        # TODO: find faces
        # TODO: create ROI around bodies
        # TODO:


    def handle(self, *args, **options):
        while True:
            ulist = UnprocessedImg.objects.filter(processed__exact=False)
            for u in ulist:
                score = self.process_image(u.get_path())
            # TODO: poll model and process images
            time.sleep(15)
