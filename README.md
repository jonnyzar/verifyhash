# verifyhash
Quick verification of correspondance of a file to its hash.

The idea is to have a quick script ready to be used after downloading some file.

verifyhash.py contains function "identhashtype" to identify the hash type if it is unknown and the function "hashfile" to hash the input file according.

Right now only MD5, SHA256 and SHA512 are supported.

Only python 3 is supported.

Basic use of verifyhash:

$python3 verifyhash.py 'reference hash string' 'path to the file that should be checked'

example:
$python3 verifyhash.py d2998c0cdf381724ad5c8fe3b825e54d ./path_to/foo_file
