"""
example use of this package

"""
import argparse
import verifyhash


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('srcHash', type=str)
    parser.add_argument('srcFilePath', type=str)

    args = parser.parse_args()

    srcHash = args.srcHash
    srcFilePath = args.srcFilePath

    hashType = verifyhash.identhashtype(srcHash)
    calculatedHash = verifyhash.hashfile(srcFilePath, hashType)

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
