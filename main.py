import logging
import ocr
import os
import csv
from datetime import datetime

from PIL import Image


IMG_DIR = r"./"  
OUTPUT_CSV_NAME = "quickfill_" + datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + ".csv"

logging.basicConfig(filename= "quickfill_" + datetime.now().strftime("%Y_%m_%d") + ".log",
                    format='%(asctime)s %(message)s',
                    filemode='a+')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

for f in os.listdir(IMG_DIR):
    if f.startswith("Snipaste"):
        logging.info("===========================================================")
        logger.info("start processing image: %s", f)
        img = Image.open(IMG_DIR + f) 
        relic = ocr.scan(img)
        with open(OUTPUT_CSV_NAME, 'a+', newline='') as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow(relic.to_csv_row())
        logger.info("")
        