# XPS-Pixel-to-Binding Energy
These set of code can be used for the conversion of X-ray Photoelectron Spectroscopy (XPS) image data to Binding Energy. In XPS image data, the acquisition window is limited.ie. Binding Energy window is limitied to certain value, such as 12 eV. And counts/ Intensity are given with respect to Pixel data. The binding energy windows can be caluculated using the XPS speactra of a species with shifted Kintec Energy (KE) value. i.e., Arsenic peak peak taken at 93 eV KE and 140eV photon energy, and another peak at 94 eV KE and 140eV photon energy. Then shift in pixel correspond to 1 eV. <br/>

* ```Pixel_per_eV.py``` can be used to find a rough estimate of Pixel/eV.<br/>
* ```Gauss_Center.py``` fit every species with a gaussian function and shows the center pixel position. Use shifted KE energy data to better estimate the Pixel/eV information.<br/>
* ```Norm_XPS_data.py```  normalize the pixel data into BE window, which can be used in CasaXPS for fitting and Binding Energy normalization wth respect to Carbon 1s. To use in CaseXPS one needs to convert the .txt file into .vms file and use the following equation to normalize the data with respect to Carbon 1s. <br/>

Binding Energy with respect to Carbon 1s: <br/>
&nbsp; &nbsp; &nbsp; &nbsp; BE<sub>2A</sub> = 285 - (E<sub>1</sub> - E<sub>2</sub>) - (KE<sub>2</sub> - KE<sub>1</sub>)   ± x
  
  where, 1 means Carbon 1s, 2 means any other species<br/>
         ```E``` is the photon energy<br/>
         ```KE``` is the kinetic energy<br/>
         ```x``` is the binding energy factor, that determine the shift with respect to Carbon 1s position<br/>
         
