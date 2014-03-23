var MainRouter = Backbone.Router.extend({

  	routes: {
    	"help":                 "help",
    	"search/:query":        "search",
		"search/:query/p:page": "search"
  	},

	help: function() {
		console.log('help')
  	},

  	search: function(query, page) {
    	console.log('search')
  	}

});