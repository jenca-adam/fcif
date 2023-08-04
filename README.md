# fcif
The Few Colors Image Format compression algorithm
> FCIF(few colors image format) is a lossy image compression alghoritm, mostly focused on graphics that don't use many colors(like icons or simple logos). It uses a combination of reducing color palette using K-means clustering and run-length encoding of color sequences to provide up to 30% the size for certain images.

Yeah. It's what it says on the tin.
# Installation
Only from GitHub for now, as the CLI is unpolished. This probably won't be getting an official release very soon.
# Usage
```
python -m fcif <img> [--palette N]
```
is used for both compression and decompressionn of images.
The more colors you add on to the palette, the better the image will look, however, the efficiency of the compression will drop drastically.
# Contribution
do anything with it, really. It's open-source. Just submit a PR if you don't feel like making a fork.

also i know i misspelled "palette" in the code but who cares.

