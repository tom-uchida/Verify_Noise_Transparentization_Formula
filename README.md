# Verify_Noise_Transparentization_Formula

## Step1｜Generate a original noise model point cloud
```
$ cd Generate_Point_Cloud/
$ ./generate_point_cloud 10000000 128 1600
```

## Step2｜Apply alphaControl
```
$ cd alphaControl4PLY_v005/
$ ./alphaControl4ply -a 0.5 -l 1 -i 512 [input_point_cloud.spbr]
```

## Step3｜Create L ensemble point clouds
```
$ ./analyzeIntermediateImages [input_point_cloud.spbr] [output_path]
```

## Step4｜Automatically, snap L intermediate images
```
$ python spbr_continuously.py [spbr_file_path] [spbr_header_file] [repeat_level]
```

## Step5｜Evaluate images quantitatively
```
$ cd py/
$ python calc_*.py
$ python create_*_figure.py
```