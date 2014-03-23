var MainPage = Page.extend({
	initialize: function () {
		this.setRouter();

		this.setMap();
		this.setFooterMenu();
		this.bindEvents();
	},

	setRouter: function () {
		
	},

	setMap: function () {
		var mapComponent = new MapComponent({
			center: new google.maps.LatLng(-30.0468953361564, -51.21174639076344),
			zoom: 14,
			mapTypeId: google.maps.MapTypeId.ROADMAP
		});

		var mapView = new MapComponentView({
			model: mapComponent,
			$el: $('#map-container')
		});

		this.set('mapComponent', mapComponent)
		this.set('mapView', mapView)
	},

	setFooterMenu: function () {
		var footerMenu = new FooterMenu();

		var footerMenuView = new FooterMenuView({
			model: footerMenu,
			$el: $('.footer-menu'),
			el: '.footer-menu'
		});
	},

	bindEvents: function () {

	}
});