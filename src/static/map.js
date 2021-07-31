function initMap() {
  const origin = { lat: 37.7749, lng: -122.419 };
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 18,
    center: origin,
  });
  new ClickEventHandler(map, origin);
}

function isIconMouseEvent(e) {
  return "placeId" in e;
}

class ClickEventHandler {
  origin;
  map;
  directionsService;
  directionsRenderer;
  placesService;
  infowindow;
  infowindowContent;
  constructor(map, origin) {
    this.origin = origin;
    this.map = map;
    this.directionsService = new google.maps.DirectionsService();
    this.directionsRenderer = new google.maps.DirectionsRenderer();
    this.directionsRenderer.setMap(map);
    this.placesService = new google.maps.places.PlacesService(map);
    this.infowindow = new google.maps.InfoWindow();
    this.infowindowContent = document.getElementById("infowindow-content");
    this.foorm = document.getElementById("foorm");
    this.infowindow.setContent(this.infowindowContent);
    // Listen for clicks on the map.
    this.map.addListener("click", this.handleClick.bind(this));
  }
  handleClick(event) {
    console.log("You clicked on: " + event.latLng);

    // If the event has a placeId, use it.
    if (isIconMouseEvent(event)) {
      console.log("You clicked on place:" + event.placeId);
      // Calling e.stop() on the event prevents the default info window from
      // showing.
      // If you call stop here when there is no placeId you will prevent some
      // other map click event handlers from receiving the event.
      event.stop();

      if (event.placeId) {
        // this.calculateAndDisplayRoute(event.placeId);
        this.getPlaceInformation(event.placeId);
      }
    }
  }
  calculateAndDisplayRoute(placeId) {
    const me = this;
    this.directionsService.route(
      {
        origin: this.origin,
        destination: { placeId: placeId },
        travelMode: google.maps.TravelMode.WALKING,
      },
      (response, status) => {
        if (status === "OK") {
          me.directionsRenderer.setDirections(response);
        } else {
          console.log("status not set to ok");
          window.alert("Directions request failed due to " + status);
        }
      }
    );
  }
  getPlaceInformation(placeId) {
    const me = this;
    this.placesService.getDetails({ placeId: placeId }, (place, status) => {
      if (
        status === "OK" &&
        place &&
        place.geometry &&
        place.geometry.location
      ) {
        
        fetch(
          //"http://127.0.0.1:5000//mapclick?address=" +
          "//todo-loco.herokuapp.com//mapclick?address=" +
            place.formatted_address +
            "&name=" +
            place.name
        )
          .then((response) => {
            return response.json();
          })
          .then((myJson) => {
            console.log(myJson);
            me.infowindow.close();
            me.infowindow.setPosition(place.geometry.location);
            me.infowindowContent.children["place-icon"].src = place.icon;
            me.infowindowContent.children["place-name"].textContent =
              place.name;
            me.infowindowContent.children["place-id"].textContent =
              place.place_id;

            me.infowindowContent.children["place-address"].textContent =
              place.formatted_address;

            me.foorm.children["place-name"].children["in"].value = place.name;
            me.foorm.children["place-address"].children["in"].value =
              place.formatted_address;
            if (myJson.status !== "error") {
              me.foorm.children["traffic-data"].children["in"].value =
                JSON.stringify(myJson.analysis.map((x) => x.day_raw));
            }
          });
        $(".ui.modal").modal("hide");
      }
    });
  }
}
