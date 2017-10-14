# Terraform infrastructure project

## Install dependencies

All dependencies are stored in `requirements.txt` in root directory.
Name and version separated by `=`.

For example:
```
terraform=0.10.7
vault=0.8.3
```

To install it run python script `./dependencies.py`

## Initial terraform project

```
terraform init
```

## Plan what apply to infrastructure

```
terraform plan
```

## Apply whore plan

```
terraform apply
```

## Apply one step

```
terraform apply -target=null_resource.upgrade-packages
```

## Inspect a state of infrastructure

```
terraform show
```
