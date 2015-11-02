var config = require('./bootstrap.config.js')
config.styleLoader = require('extract-text-webpack-plugin').extract('style-loader', 'css-loader!less-loader')
module.exports = config
