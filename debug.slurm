#!/bin/bash
#SBATCH -J hf
#SBATCH -p HGX
#SBATCH --qos=lv0b
#SBATCH --time=10:00:00
#SBATCH -o %j.out
#SBATCH -e %j.err
#SBATCH --gres=gpu:1

module load cuda11.8/toolkit/11.8.0
module load cudnn8.6-cuda11.8/8.6.0.163  

source /home/zhuxuekai/miniconda3/bin/activate reasoning

python test_eof_error_new.py