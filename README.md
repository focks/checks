# CHECKS

A micro check package. -- inspired from [is.js](https://github.com/arasatasaygin/is.js)


## Installation


Execute after moving into `checks/`
```
pip install --editable .
```

## Usage

### is_list

```
>>> import checks
>>> checks.is_list([])
True

>>> is_py.is_list([1,2,3])
True

>>> is_py.is_list("string")
False
```
