## I'm the best coder! Challenge 2020

## Init
```
$ conda create --name shopee python=3.7.9
$ conda deactivate && conda activate shopee
$ pip install poetry
$ git clone https://github.com/allenyummy/ImBestCoder2020.git
$ poetry install
```

## Modify or Add package
```
$ vim pyproject.toml
$ poetry update
$ poetry export --without-hashes -f requirements.txt -o requirements.txt
```