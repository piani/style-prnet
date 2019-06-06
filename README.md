##Usage

1. Clone the repository
```bash
git clone https://github.com/piani/style-prnet.git
cd style-prnet
```

2. Clone PRNet in style-prnet/
```bash
git clone https://github.com/piani/PRNet.git
```

3. Clone stylegan-encoder in style-prnet/
```bash
git clone https://github.com/piani/stylegan-encoder.git 
```

then you have this 
```
style-prnet
│   README.md
│   style_prnet_execute.py
│
└───stylegan-encoder
│
└───PRNet
```

4. Run with your own images
```bash
python style_prnet_execute.py -i <inputDir> -o <outputDir> -g <float::gender_degree> -a <float::age_degree> -s <float::smile_degree>
```
- defalut inputDir: /stylegan-encoder/raw_images/
- `<inputDir>` is absolute path only.
- default `<outputDir>`: /results/3DGenerated_results 
- output will be saved /results/<outputDir>
- We have now 3 style latent: smile, age, gender


