 function initMap() {
        var uluru = {lat: -25.363, lng: 131.044};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 4,
          center: ({lat: 40.70645880000001, lng: -73.9447634})
        });
        var marker = new google.maps.Marker({
          position: ({lat: 40.70645880000001, lng: -73.9447634}),
          map: map
        });
      }
    </script>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyB1Udy3X-6-BGZaJt-SIT0OrvUWo_i4uWs&callback=initMap">