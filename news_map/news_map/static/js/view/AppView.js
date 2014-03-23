var AppView = Backbone.View.extend({
	initialize: function () {
		
	}
})

$(function () {
	App = new App();
	
	AppView = new AppView({
		model: App
	});
})