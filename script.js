
var map = L.map('map-container')
.setView([20,10],2);



L.tileLayer(
'https://tile.openstreetmap.org/{z}/{x}/{y}.png'
)
.addTo(map);



L.marker([57.7089,11.9746])
.addTo(map)
.bindPopup(
"Ocean Infinity - Gothenburg Sweden<br>Hydrographic Data Processing"
);



L.marker([55.7058,13.1930])
.addTo(map)
.bindPopup(
"Lund University<br>Master Degree in Geomatics"
);



L.marker([-1.9403,29.8739])
.addTo(map)
.bindPopup(
"Rwanda<br>GIS and Geological Mapping Experience"
);
