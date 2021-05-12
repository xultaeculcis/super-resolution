# super-resolution

This repo contains a sample web application that explains what super-resolution is, presents image enhancement history,
SR usage scenarios, DL architectures and a SR demo with SRCNN.

## Local Env Installation

Run:
```bash
conda env create -f environment.yml
docker build -t sr .
docker run -d --name sr -p 8501:8501 sr
```
