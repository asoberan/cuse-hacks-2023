from folium.plugins import FastMarkerCluster
import folium as f
import pandas as pd
import os.path
import webbrowser

DATASETS_PATH = "datasets/"
CNY = (43.0481221, -76.1474244)

PANTRY_DATA = pd.read_csv(os.path.join(DATASETS_PATH,
                                       "2019/"
                                       "onondaga-food-resources.csv"),
                          encoding = 'unicode_escape',
                          engine = 'python')

def fast_marker_cluster(data):
    callback = ('''

       function(row) {
            var colors = {
                "Food Pantry": "yellow",
                "Community Garden": "green",
                "Grocery Store": "blue"
            };

            var marker = L.marker(new L.LatLng(row[0], row[1]), {color: "red"});

            var icon = L.AwesomeMarkers.icon({
                icon: 'info-sign',
                markerColor: colors[row[2]],
                prefix: 'glyphicon',
                extraClasses: 'fa-rotate-0'});

            marker.setIcon(icon);
            var popupName = "<p class='popup-name'>" + row[3] + "</p>";
            var popupAddress = "<p class='popup-address'>" +
                                row[4] + ", " +
                                row[5] + " " +
                                row[6] + "</p>";
            var popupDirs = "<a target='_blank' href='https://www.google.com/maps?saddr=My+Location&daddr=" + row[0] + "," + row[1] + "'>Directions</a>";
            var popupHours = "<p class='popup-hours-title'><strong>Hours:</strong></p><p class='popup-hours'>" + row[7] + "</p>";
            marker.bindPopup(popupName + popupAddress + popupDirs + popupHours);
            marker.bindTooltip(row[3]);
            return marker
       };

    ''')

    marker_data = data[["Lat", "Lon", "Type", "Name", "Street", "City", "Zip", "Hours"]].values.tolist()

    fast_marker_cluster = FastMarkerCluster(marker_data,
                                            callback=callback,
                                            disable_clustering_at_zoom=14,
                                            spiderfyOnMaxZoom=False)

    return fast_marker_cluster

def create_map():
    fol_map = f.Map(location=CNY, max_zoom=19, zoom_start=12)
    fol_map.add_child(fast_marker_cluster(PANTRY_DATA))

    return fol_map

def main():
    fol_map = create_map()
    fol_map.save("templates/map/index.html")
    webbrowser.open("templates/map/index.html")

if __name__ == "__main__":
    main()
