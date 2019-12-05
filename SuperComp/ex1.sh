#!/bin/bash
#SBATCH --job-name=example
#SBATCH --partition=general
#SBATCH -n 1
#SBATCH --output=example_%j.out
#SBATCH --error=example_%j.err
#SBATCH --mail-user=infostructuras@yahoo.com
#SBATCH --mail-type=ALL
 
srun hostname
