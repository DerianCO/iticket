  var placeSearch, autocomplete;
  var componentForm = {
    street_number: 'short_name',
    route: 'long_name',
    locality: 'long_name',
    administrative_area_level_1: 'short_name',
    country: 'long_name',
    postal_code: 'short_name'
  };

  function initAutocomplete() {
    // Create the autocomplete object, restricting the search to geographical
    // location types.
    autocomplete = new google.maps.places.Autocomplete(
        /** @type {!HTMLInputElement} */(document.getElementById('autocomplete')),
        {types: []});

    // When the user selects an address from the dropdown, populate the address
    // fields in the form.
    autocomplete.addListener('place_changed', fillInAddress);
  }

  function fillInAddress() {
    var lat;
    var lng;
    // Get the place details from the autocomplete object.
    var place = autocomplete.getPlace();
    lat = place.geometry.location.lat();
    lng = place.geometry.location.lng();

    document.getElementById('lat').value = lat;
    document.getElementById('lng').value = lng;    

    for (var component in componentForm) {
      document.getElementById(component).value = '';
      document.getElementById(component).disabled = false;
    }


    for (var i = 0; i < place.address_components.length; i++) {
      var addressType = place.address_components[i].types[0];
      if (componentForm[addressType]) {
        var val = place.address_components[i][componentForm[addressType]];
        document.getElementById(addressType).value = val;
        document.getElementById(addressType).disabled = true;
      }
    }

    initmap(lat,lng);
  }

  // Bias the autocomplete object to the user's geographical location,
  // as supplied by the browser's 'navigator.geolocation' object.
  function geolocate() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function(position) {
        var geolocation = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };
        var circle = new google.maps.Circle({
          center: geolocation,
          radius: position.coords.accuracy
        });
        autocomplete.setBounds(circle.getBounds());
      });
    }
  }


  function initmap(lat,lng) {
    var mapOptions = {
      zoom: 17,
      center: new google.maps.LatLng(lat,lng),
      mapTypeId: google.maps.MapTypeId.ROADMAP,

      mapTypeControl: false,
      mapTypeControlOptions: {
        style: google.maps.MapTypeControlStyle.DROPDOWN_MENU,
        position: google.maps.ControlPosition.LEFT_CENTER
      },
      panControl: false,
      panControlOptions: {
        position: google.maps.ControlPosition.TOP_RIGHT
      },
      zoomControl: true,
      zoomControlOptions: {
        style: google.maps.ZoomControlStyle.LARGE,
        position: google.maps.ControlPosition.RIGHT_BOTTOM
      },
       scrollwheel: false,
      scaleControl: false,
      scaleControlOptions: {
        position: google.maps.ControlPosition.LEFT_CENTER
      },
      streetViewControl: true,
      streetViewControlOptions: {
        position: google.maps.ControlPosition.RIGHT_BOTTOM
      },
      styles: [
                     {
        "featureType": "landscape",
        "stylers": [
          {
            "hue": "#FFBB00"
          },
          {
            "saturation": 43.400000000000006
          },
          {
            "lightness": 37.599999999999994
          },
          {
            "gamma": 1
          }
        ]
      },
      {
        "featureType": "road.highway",
        "stylers": [
          {
            "hue": "#FFC200"
          },
          {
            "saturation": -61.8
          },
          {
            "lightness": 45.599999999999994
          },
          {
            "gamma": 1
          }
        ]
      },
      {
        "featureType": "road.arterial",
        "stylers": [
          {
            "hue": "#FF0300"
          },
          {
            "saturation": -100
          },
          {
            "lightness": 51.19999999999999
          },
          {
            "gamma": 1
          }
        ]
      },
      {
        "featureType": "road.local",
        "stylers": [
          {
            "hue": "#FF0300"
          },
          {
            "saturation": -100
          },
          {
            "lightness": 52
          },
          {
            "gamma": 1
          }
        ]
      },
      {
        "featureType": "water",
        "stylers": [
          {
            "hue": "#0078FF"
          },
          {
            "saturation": -13.200000000000003
          },
          {
            "lightness": 2.4000000000000057
          },
          {
            "gamma": 1
          }
        ]
      },
      {
        "featureType": "poi",
        "stylers": [
          {
            "hue": "#00FF6A"
          },
          {
            "saturation": -1.0989010989011234
          },
          {
            "lightness": 11.200000000000017
          },
          {
            "gamma": 1
          }
        ]
      }
      ]
    };

    document.getElementById("map_event").style.width = "100%";
    document.getElementById("map_event").style.height = "300px";
    var mapObject = new google.maps.Map(document.getElementById('map_event'), mapOptions);
    var marker = new google.maps.Marker({
      position: {lat: lat,lng: lng},
      map: mapObject
    });
  }
