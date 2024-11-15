import json
import os
from pycocotools import mask as maskUtils
import cv2
import numpy as np

# Load the uploaded JSON file
file_path = 'instances_default.json'
with open(file_path, 'r') as file:
    coco_data = json.load(file)

spt = ['train', 'val', 'test']

for s in spt:

    # Define the folder path
    folder_path = f'{s}/images'

    # Selected images to retain
    selected_img = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]

    
    # Filter images based on selected_img
    filtered_images = [img for img in coco_data['images'] if img['file_name'] in selected_img]
    for img in filtered_images:
        img['file_name'] = f"images/{img['file_name']}"
        

    # Collect the image IDs of the filtered images
    selected_image_ids = {img['id'] for img in filtered_images}

    # Filter annotations based on selected image IDs
    filtered_annotations = [anno for anno in coco_data['annotations'] if anno['image_id'] in selected_image_ids]

    # Modify annotations to have a single category "object" with id 0
    for anno in filtered_annotations:
        anno['category_id'] = 1
        if anno['iscrowd'] == 1:
            rle = anno['segmentation']
            # RLE를 마스크로 디코딩
            # counts 필드를 압축된 RLE 형식으로 변환
            rle_compressed = maskUtils.frPyObjects(rle, rle['size'][0], rle['size'][1])

            # 단일 객체이므로 첫 번째 요소 선택
            if isinstance(rle_compressed, list):
                rle_compressed = rle_compressed[0]



            mask = maskUtils.decode(rle_compressed)
            


            # 마스크를 0~255로 변환 (uint8 타입)
            mask = mask.astype(np.uint8) * 255

            # 외곽선 추출
            contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # 폴리곤 좌표 추출
            polygons = []
            for contour in contours:
                contour = contour.flatten().tolist()
                if len(contour) > 4:  # 최소한 2개의 점이 있어야 함
                    polygons.append(contour)
            anno['segmentation'] = polygons
            anno['iscrowd'] = 0
            anno['attributes']['occluded'] = False
            
            

    # Modify categories to include only "object" with id 0
    filtered_categories = [{'id': 1, 'name': 'object'}]

    # Create the new COCO JSON structure
    filtered_coco_data = {
        'images': filtered_images,
        'annotations': filtered_annotations,
        'categories': filtered_categories,
    }

    # Save the filtered and modified JSON
    output_path = f'{s}/annotation_coco.json'
    with open(output_path, 'w') as file:
        json.dump(filtered_coco_data, file, indent=4)

