var FooterMenuView = Backbone.View.extend({
	events: {
		'click' : 'onClickButton'
	},
	
	initialize: function () {
		console.log(this.$el)
		this.$el.find('button')
	},


	onClickButton: function (e) {
		console.log(e)
	}
});