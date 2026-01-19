# pi-DiffNovo
This is the official repo for the paper: "When diffusion meets non-autoregressive transformers: introducing pi-DiffNovo for accurate peptide de novo sequencing"
<img width="1613" height="1125" alt="Figure 1 workflow" src="https://github.com/user-attachments/assets/d8ea8dd9-45fe-4a58-8e10-de5ae0daf81f" />
# Environment Setup
First is to set up environment for pi-PrimeNovo and InstaNovo.
Create a new conda environment for InstaNovo:

```
conda create --name DiffNovo python=3.10.0
```
This will create an anaconda environment. Activate this environment by running:

```
conda activate DiffNovo
```
Then install dependencies provided by below requirement file:

```
pip install -r ./IN_requirements.txt
```

Create a new conda environment for pi-PrimeNovo:

```
conda create --name PrimeNovo python=3.10.0
```

Activate this environment by running:

```
conda activate PrimeNovo
```

Then install dependencies provided by below requirement file:

```
pip install -r ./pi_requirements.txt
```
# pi-PrimeNovo prediction and Scores

First activate environment：
```
conda activate PrimeNovo
```

We provided a sample data containing 20000+ spectrums in SampleData_Muslus.zip.
unzip this file to attain the mgf file peaks.db.mgf. This is the Mouse dataset in MSV000090982.

Run the following command to obtain pi-PrimeNovo prediction and beam scores:
```
python -m PrimeNovo.PrimeNovo --mode=denovo --peak_path=./peaks.db.mgf --model=./model_massive.ckpt
```

This will produce a denovo.tsv file which contains the prediction and beam scores.
Run 1_ConvertPiResutls.py to attain converted results.
Run 2_changeModificationFormat.py to exchange pi-PrimNovo format modification into InstaNovo format.
Run 3_tokenizePipreds.py to attain toknized pi-PrimeNovo results for further evaluation in InstaNovo.

Eventually we obtain Mouse_tokenized.csv.

# InstaNovo+ prediction 

Activate environment:

```
conda activate DiffNovo
```

Run the following command:










