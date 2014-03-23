var MapComponentView = Backbone.View.extend({
	initialize: function () {
		//this.listenTo(this.model, "change", this.render);
		this.render();
	},

	render: function () {
		var settings = this.model.get('settings');

		this.map = new google.maps.Map($("#map-container")[0], settings);

		this.bindEvents();
	},

	bindEvents: function () {
		var self = this;

		google.maps.event.addListener(this.map, 'click', function(e) {
			console.log(e)
		});
	}
});