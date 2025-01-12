# from mmdet.apis import init_detector, inference_detector
# from mmengine.config import Config



# The new config inherits a base config to highlight the necessary modification
_base_ = ['../mask2former/mask2former_swin-t-p4-w7-224_8xb2-lsj-50e_coco.py']

# Set for class-agnostic instance segmentation
num_things_classes = 1  # Only one class (object) for all instances
num_stuff_classes = 0   # No stuff classes
num_classes = num_things_classes + num_stuff_classes

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    panoptic_head=dict(
        num_things_classes=num_things_classes,
        num_stuff_classes=num_stuff_classes,
        loss_cls=dict(class_weight=[1.0] * num_classes + [0.1])),
    panoptic_fusion_head=dict(
        num_things_classes=num_things_classes,
        num_stuff_classes=num_stuff_classes),
    test_cfg=dict(panoptic_on=False))
# Modify dataset related settings
data_root = '../../../arti_data/'
metainfo = {
    'classes': ('object', ), #class-agnostic
    'palette': [
        (220, 20, 60),
    ]
}
train_dataloader = dict(
    batch_size=8,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='train/annotation_coco.json',
        data_prefix=dict(img='train/')))
val_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='val/annotation_coco.json',
        data_prefix=dict(img='val/')))
# test_dataloader = dict(
#     dataset=dict(
#         data_root=data_root,
#         metainfo=metainfo,
#         ann_file='test/annotation_coco.json',
#         data_prefix=dict(img='test/')))

# Modify metric related settings
val_evaluator = dict(_delete_=True, type='CocoMetric',  metric=['bbox', 'segm'], ann_file=data_root + 'val/annotation_coco.json')
# test_evaluator = dict(_delete_=True, type='CocoMetric',  metric=['bbox', 'segm'], ann_file=data_root + 'test/annotation_coco.json')

# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = 'https://download.openmmlab.com/mmdetection/v3.0/mask2former/mask2former_swin-l-p4-w12-384-in21k_16xb1-lsj-100e_coco-panoptic/mask2former_swin-l-p4-w12-384-in21k_16xb1-lsj-100e_coco-panoptic_20220407_104949-82f8d28d.pth'
