# How to prepare dataset with labels

## CVAT
- Export json file for label after finishing annotation.
- Copy your image files on `test`, `train`, `val` depending on the type of dataset. Please do not change names of your data files.
-  Copy your json file once so that you can make class-agnostic version and the one for classwise version. The class-agnostic version will be used for training part segmentation and the other one is for training our GNN.
- For all annotation files, you need to make `annotation_coco.json` for train, test, valid split folders respectively.
    ```
    "images":[{"id":1,"width":349,"height":287,"file_name":"1105_traj_0.png","license":0,"flickr_url":"","coco_url":"","date_captured":0},{"id":2,"width":379,"height":310,"file_name":"1105_traj_1.png","license":0,"flickr_url":"","coco_url":"","date_captured":0},{"id":3,"width":402,"height":282,"file_name":"1105_traj_10.png","license":0,"flickr_url":"","coco_url":"","date_captured":0},{"id":4,"width":346,"height":211,"file_name":"1105_traj_11.png","license":0,"flickr_url":"","coco_url":"","date_captured":0},{"id":5,"width":289,"height":213,"file_name":"1105_traj_12.png","license":0,"flickr_url":"","coco_url":"","date_captured":0}
    ```

    ... 일단 해야하는게 json file에서 

    

- For class-agnostic version, you need to change 
    ```
    "categories":[{"id":1,"name":"base","supercategory":""},{"id":2,"name":"lid","supercategory":""}]
    ```
    
    by just running this script
    
    ```
    python src/filter.py
    ```


## MEMO
### 1114 test version split

```
Train files: ['1105_traj_5.png', '1105_traj_9.png', '1105_traj_2.png', '1105_traj_15.png', '1105_traj_19.png', '1105_traj_3.png', '1105_traj_17.png', '1105_traj_12.png', '1105_traj_0.png', '1105_traj_1.png', '1105_traj_7.png', '1105_traj_11.png', '1105_traj_16.png', '1105_traj_6.png']
Validation files: ['1105_traj_4.png', '1105_traj_18.png', '1105_traj_13.png']
Test files: ['1105_traj_10.png', '1105_traj_8.png', '1105_traj_14.png']
```
