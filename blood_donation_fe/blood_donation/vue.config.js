// vue.config.js
module.exports = {
    // options...
    devServer: {
        disableHostCheck: true,
	proxy: 'http://blooddonorbackend.ddns.net:8000/',
	 host: '0.0.0.0',
    	hot: true,
    }
}
