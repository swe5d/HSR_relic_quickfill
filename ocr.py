from cnocr import CnOcr
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from relic import Relic
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)

ocr = CnOcr(det_model_name='naive_det') 

x = 40
set_name_pos = [[792, 330], [1047, 362]]
set_piece_pos = [[552, 723], [638, 750]]
main_stat_name_pos = [[790+x, 401], [925+x, 429]]
main_stat_value_pos = [[1370, 400], [1445, 432]]
sub_stat_1_name_pos = [[790+x, 442], [925+x, 470]]
sub_stat_1_value_pos = [[1370, 444], [1445, 472]]
sub_stat_2_name_pos = [[790+x, 472], [925+x, 512]]
sub_stat_2_value_pos = [[1370, 480], [1445, 509]]
sub_stat_3_name_pos = [[790+x, 514], [925+x, 542]]
sub_stat_3_value_pos = [[1370, 516], [1445, 545]]
sub_stat_4_name_pos = [[790+x, 550], [925+x, 583]]
sub_stat_4_value_pos = [[1370, 552], [1445, 581]]

def crop_image(img, pos):
    return img.crop((pos[0][0],pos[0][1],pos[1][0],pos[1][1]))

def scan(img):
    r = Relic()
    set_name = ocr.ocr(crop_image(img, set_name_pos))
    set_piece = ocr.ocr(crop_image(img, set_piece_pos))
    main_stat_name = ocr.ocr(crop_image(img, main_stat_name_pos))
    main_stat_value = ocr.ocr(crop_image(img, main_stat_value_pos))
    logger.info(set_name)
    logger.info(set_piece)
    logger.info(main_stat_name)
    logger.info(main_stat_value)
    r.set_name = set_name[0].get("text")
    r.set_piece = set_piece[0].get("text")
    r.main_stat_name = main_stat_name[0].get("text")
    r.main_stat_value = main_stat_value[0].get("text")

    sub_stat_1_name = ocr.ocr(crop_image(img, sub_stat_1_name_pos))
    sub_stat_1_value = ocr.ocr(crop_image(img, sub_stat_1_value_pos))
    logger.info(sub_stat_1_name)
    logger.info(sub_stat_1_value)

    if len(sub_stat_1_value) != 0 and sub_stat_1_value[0].get("score") >= 0.5:
        logger.info("sub stat 1 valid, continue")
        r.sub_stat_1_name = sub_stat_1_name[0].get("text")
        r.sub_stat_1_value = sub_stat_1_value[0].get("text")

        sub_stat_2_name = ocr.ocr(crop_image(img, sub_stat_2_name_pos))
        sub_stat_2_value = ocr.ocr(crop_image(img, sub_stat_2_value_pos))
        logger.info(sub_stat_2_name)
        logger.info(sub_stat_2_value)

        if len(sub_stat_2_value) != 0 and sub_stat_2_value[0].get("score") >= 0.5:
            logger.info("sub stat 2 valid, continue")
            r.sub_stat_2_name = sub_stat_2_name[0].get("text")
            r.sub_stat_2_value = sub_stat_2_value[0].get("text")

            sub_stat_3_name = ocr.ocr(crop_image(img, sub_stat_3_name_pos))
            sub_stat_3_value = ocr.ocr(crop_image(img, sub_stat_3_value_pos))
            logger.info(sub_stat_3_name)
            logger.info(sub_stat_3_value)
            if len(sub_stat_3_value) != 0 and sub_stat_3_value[0].get("score") >= 0.5:
                logger.info("sub stat 3 valid, continue")
                r.sub_stat_3_name = sub_stat_3_name[0].get("text")
                r.sub_stat_3_value = sub_stat_3_value[0].get("text")

                sub_stat_4_name = ocr.ocr(crop_image(img, sub_stat_4_name_pos))
                sub_stat_4_value = ocr.ocr(crop_image(img, sub_stat_4_value_pos))
                logger.info(sub_stat_4_name)
                logger.info(sub_stat_4_value)

                if len(sub_stat_4_value) != 0 and sub_stat_4_value[0].get("score") >= 0.5:
                    logger.info("sub stat 4 valid, continue")
                    r.sub_stat_4_name = sub_stat_4_name[0].get("text")
                    r.sub_stat_4_value = sub_stat_4_value[0].get("text")
    return r

