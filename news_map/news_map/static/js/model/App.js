var Router = new MainRouter();

var Ev = {};

_.extend(Ev, Backbone.Events);

var App = Backbone.Model.extend({
	initialize: function () {
		var mainPage;

		mainPage = new MainPage();
	},
});