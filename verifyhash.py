"""
Please use this tool for checking any files that you download.
And have fun coding!
Please e-mail me if anything goes wrong.

Mail: yan.zaripov@gmail.com

Author: Yan Zaripov
"""

import argparse
import hashlib

def identhashtype(srcHash):
    """
    Identifies the hash function type
    Now supports: MD5, SHA256, SHA512

    :param srcHash: hasf as a string with hexadecimal digits
    :return: hash type -MD5, SHA256 or SHA512- as a string
    """

    #calculation of bits length of the hexdigest
    try:
        lenBits = len(srcHash) * 4

        if lenBits == 128:
            return 'MD5'
        elif lenBits == 256:
            return 'SHA256'
        elif lenBits == 512:
            return 'SHA512'
        else:
            print('unsupported hash type')
            exit(0)
    except Exception as e:
        print(e)
        exit(1)


def hashfile(srcFilePath, hashType, BLOCK_SIZE=65536):
    """
    Hash any give file in its hash

    :param srcFilePath: path to the file from which the reference
    hash is supposed to originate from
    :param hashType: hash type to use
    :param BLOCK_SIZE:
    default is 65536; change to any other size using power of 2
    :return: string with decimal hash characters
    """

    # hash the source file according to hash type, BLOCKSIZE is to avoid buffer overflow
    # internal var should have _ in their name

    try:
        if hashType == 'MD5':
            file_hash = hashlib.md5()
        elif hashType == 'SHA256':
            file_hash = hashlib.sha256()
        elif hashType == 'SHA512':
            file_hash = hashlib.sha256()
        else:
            exit(0)

        with open(srcFilePath, 'rb') as f:  # open file to read its bytes
            fb = f.read(BLOCK_SIZE)
            while len(fb) > 0:
                file_hash.update(fb)
                fb = f.read(BLOCK_SIZE)
        return file_hash.hexdigest()
    except Exception as e:
        print(e)
        exit(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('srcHash', type=str)
    parser.add_argument('srcFilePath', type=str)

    args = parser.parse_args()

    srcHash = args.srcHash
    srcFilePath = args.srcFilePath

    hashType = identhashtype(srcHash)
    calculatedHash = hashfile(srcFilePath, hashType)

    if srcHash == calculatedHash:
        print(f"\n Hashes are equal! Everything is fine. \n"
              f"\n Reference hash type is {hashType}."
              f"\n Input file hash is: {calculatedHash} "
              f"\n Reference hash is: {srcHash}")
    else:
        print("Hashes do not correspond! \n")
        print(f"\n Reference hash type is {hashType}."
              f"\n Input file hash is: {calculatedHash} "
              f"\n Reference hash is: {srcHash}")

    return 0


if __name__ == '__main__':
    main()
