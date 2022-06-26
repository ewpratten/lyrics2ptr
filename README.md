# lyrics2ptr
Utility script for converting song lyrics to host/hostname pairs for HE.net DNS records

## Usage

```text
usage: lyrics2ptr [-h] [--addr-prefix ADDR_PREFIX] [--addr-suffix ADDR_SUFFIX] text_file

positional arguments:
  text_file             Text file containing lyrics

options:
  -h, --help            show this help message and exit
  --addr-prefix ADDR_PREFIX
                        Optional prefix for the generated address byte
  --addr-suffix ADDR_SUFFIX
                        Optional suffix for the generated address byte
```
