#%%
import tiledb
from tiledb.bioimg.converters.openslide import OpenSlideConverter
import os
import urllib, urllib.request

#%%
if not os.path.isfile("JP2K-33003-2.svs"):
  print("Downloading sample image...")
  urllib.request.urlretrieve("https://openslide.cs.cmu.edu/download/openslide-testdata/Aperio/JP2K-33003-2.svs", "JP2K-33003-2.svs")

#%%
if not os.path.isfile("JP2K-33003-2.tiledb"):
  print("Converting image 1, levels 1-3 to TileDB...")
  OpenSlideConverter.to_tiledb(
    "JP2K-33003-2.svs", "JP2K-33003-2.tiledb",
    compressor=tiledb.WebpFilter(lossless=False, quality=70)
  )