# XPS-Pixel-to-Binding Energy
These sets of codes can be used for the conversion of X-ray Photoelectron Spectroscopy (XPS) image data to Binding Energy (BE). In XPS image data, the acquisition window is limited. i.e., the binding energy window is limited to a certain value, such as 12 eV. And, counts/ Intensity are given with respect to Pixel data. The binding energy windows can be calculated using the XPS spectra of a species with shifted Kintec Energy (KE) value. i.e., Arsenic peak taken at ```93 eV KE and 140eV``` photon energy, and another peak at ```94 eV KE and 140eV``` photon energy. Then a shift in pixel corresponds to 1 eV. <br/>

* ```Pixel_per_eV.py``` can be used to find a rough estimate of Pixel/eV.<br/>
* ```Gauss_Center.py``` fit every species with a gaussian function and shows the center pixel position. Use shifted KE energy data to better estimate the Pixel/eV information. The process is not automated in the current version. One need to run two files that has shifted kintic energy. i.e., 93 eV and 94 eV. <br/>
* ```Norm_XPS_data.py```  normalize the pixel data into BE (or, KE) window, which can be used in CasaXPS for fitting and binding energy normalization wth respect to Carbon 1s. To use in CaseXPS one needs to convert the .txt file into .vms file and use the following equation to normalize the data with respect to Carbon 1s. <br/>

For constant Kinetic Energy type XPS, <br/>
Binding Energy with respect to Carbon 1s: <br/>
&nbsp; &nbsp; &nbsp; &nbsp; BE<sub>2A</sub> = 285 - (E<sub>1</sub> - E<sub>2</sub>) - (KE<sub>2</sub> - KE<sub>1</sub>)   ± x
  
&nbsp; &nbsp; &nbsp; &nbsp;  where, 1 means Carbon 1s, 2 means any other species<br/>
&nbsp; &nbsp; &nbsp; &nbsp; ```E``` is the photon energy<br/>
&nbsp; &nbsp; &nbsp; &nbsp; ```KE``` is the kinetic energy<br/>
&nbsp; &nbsp; &nbsp; &nbsp; ```x``` is the binding energy factor, that determine the shift with respect to Carbon 1s position<br/>


For constant Photon Energy type XPS, <br/>
Binding Energy with respect to Carbon 1s: <br/>
&nbsp; &nbsp; &nbsp; &nbsp; BE<sub>2A</sub> = 285 - (KE<sub>2</sub> - KE<sub>1</sub>)   ± x
         
## Prerequisites:

* Python 3, or higher
* or Pycharm with Proper Packages (i.e., NumPy, lmfit, matplotlib)

## Author

 * **Jyoti Biswas**
 
## Acknowledgments

Great appreciation to BNL scientist **Dr. Jerzy T. Sadowski** for his valuable and constructive suggestions. 
 
