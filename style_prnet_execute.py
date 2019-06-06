import os
import sys
import subprocess
import argparse

parser = argparse.ArgumentParser(description="argument parser")
parser.add_argument('-i','--inputDir') # absoulute path only !!
parser.add_argument('-o','--outputDir') # absoulute path only !!
parser.add_argument('-s','--smile', type=float)
parser.add_argument('-g','--gender', type=float)
parser.add_argument('-a','--age', type=float)
args=parser.parse_args()


def encode_img_to_npy(input_images):
    # raw_image preprocessing
    res = subprocess.call("cd stylegan-encoder/ ; python align_images.py " + input_images + " aligned_images/",shell = True)
    if res == 0:
        print("align_images pass")
    else:
        sys.exit(0)

    res = subprocess.call("cd stylegan-encoder/ ; python encode_images.py aligned_images/ generated_images/ latent_representations/", shell = True)
    if res == 0:
        print("encode_images pass")
    else:
        sys.exit(0)


def generate_img_with_stylegan():
    # generate image with stylegan
    ENCODE_OUTPUT_DIR = 'stylegan-encoder/latent_representations/'
    for img_name in os.listdir(ENCODE_OUTPUT_DIR):
        img_path = os.path.join(ENCODE_OUTPUT_DIR, img_name)
        img_path = img_path.replace('stylegan-encoder/','',1)

        cmd = "cd stylegan-encoder/ ; python play_with_latent_directions.py --input {}".format(img_path)
        if args.smile: cmd += " -s {}".format(args.smile)
        if args.gender: cmd += " -g {}".format(args.gender)
        if args.age: cmd += " -a {}".format(args.age)
        res = subprocess.call(cmd, shell = True)

        if res == 0:
            print(img_path + ' pass')
        else:
            sys.exit(0)
    print("generate with stylegan pass")


def generate_3d_with_prnet():
    #generate 3D model with PRNET
    GENERATED_OUTPUT_DIR = '../stylegan-encoder/results'
    cmd = "cd PRNet/ ; python demo.py -i {} -o {} --isDlib True".format(GENERATED_OUTPUT_DIR, outputDir)
    res = subprocess.call(cmd, shell = True)

    if res == 0:
        print("PRNet 3D genertated pass")


if __name__ == "__main__":

    inputDir ='raw_images/'
    if args.inputDir :
        inputDir = args.inputDir
    outputDir = '../results/3DGenerated_results'
    if args.outputDir:
        outputDir = '../results/' + args.outputDir

    encode_img_to_npy(inputDir)
    generate_img_with_stylegan()
    generate_3d_with_prnet()
