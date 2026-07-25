var map = L.map('mapid')
.setView([20,10],2);


L.tileLayer(
'https://tile.openstreetmap.org/{z}/{x}/{y}.png'
)
.addTo(map);



var projects=[


{
name:"Sweden - Hydrographic Data Processing",
lat:59.3,
lon:18.0
},


{
name:"Rwanda - Geological GIS Mapping",
lat:-1.9,
lon:29.8
},


{
name:"Offshore Survey Projects",
lat:55,
lon:5
}


];



projects.forEach(function(p){


L.marker([p.lat,p.lon])
.addTo(map)
.bindPopup(p.name);


});
