from osgeo import gdal, gdalconst
from gdal2numpy import GDAL2Numpy, Numpy2GTiff
filedem = r"c:\Users\vlr20\Downloads\bassaromagna_builds_2m.tif"


def increase_dem(dem, m,n):

    for i in range(m):
        for j in range(n):
            dem[i,j] += 1
    return dem
    


def main():
    
    # ds = gdal.Open(filedem, gdalconst.GA_ReadOnly)
    # if ds:
    #     m = ds.RasterYSize
    #     n = ds.RasterXSize
    #     nbands = ds.RasterCount
    #     band = ds.GetRasterBand(1)
    #     data = band.ReadAsArray()
    #     print("m,n", m, n)
    #     print("data", data.shape)
    #     ds = None

    data, gt, prj = GDAL2Numpy(filedem, load_nodata_as=0)
    x0, px, rx, y0, ry, py = gt
    dem =increase_dem(data, data.shape[0], data.shape[1])
    Numpy2GTiff(data, gt, prj, fileout="test2.tif")

    print(prj)



if __name__ == "__main__":
    main()  
